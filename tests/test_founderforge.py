import json
import re
from pathlib import Path

from founderforge import Wizard, DatabaseConfig, OAuthConfig, DeploymentConfig


def test_create_database():
    wiz = Wizard()
    db_cfg = wiz.create_database()
    assert isinstance(db_cfg, DatabaseConfig)
    # Provider must be postgres
    assert db_cfg.provider == "postgresql"
    # Instance id format
    assert re.fullmatch(r"postgresql-[0-9a-f]{8}", db_cfg.instance_id)
    # URL must contain the instance id
    assert db_cfg.instance_id in db_cfg.connection_url
    # State stored correctly
    assert wiz.state["database"]["connection_url"] == db_cfg.connection_url


def test_configure_oauth():
    wiz = Wizard()
    # Need a database first because later steps depend on it
    wiz.create_database()
    oauth_cfg = wiz.configure_oauth()
    assert isinstance(oauth_cfg, OAuthConfig)
    assert oauth_cfg.provider == "github"
    assert oauth_cfg.client_id.startswith("github_client_")
    assert len(oauth_cfg.client_secret) == 32  # uuid4 hex length
    assert oauth_cfg.redirect_uri == "https://myapp.example.com/auth/callback"
    # State stored
    assert wiz.state["oauth"]["client_id"] == oauth_cfg.client_id


def test_generate_deployment_includes_env():
    wiz = Wizard()
    db = wiz.create_database()
    oauth = wiz.configure_oauth()
    dep_cfg = wiz.generate_deployment()
    assert isinstance(dep_cfg, DeploymentConfig)
    assert dep_cfg.platform == "render"
    # Environment must contain the values from previous steps
    env = dep_cfg.env
    assert env["DATABASE_URL"] == db.connection_url
    assert env["OAUTH_CLIENT_ID"] == oauth.client_id
    assert env["OAUTH_CLIENT_SECRET"] == oauth.client_secret
    assert env["OAUTH_REDIRECT_URI"] == oauth.redirect_uri


def test_save_state_writes_valid_json(tmp_path: Path):
    wiz = Wizard(output_dir=tmp_path)
    wiz.create_database()
    wiz.configure_oauth()
    wiz.generate_deployment()
    state_file = wiz.save_state()
    assert state_file == tmp_path / "founderforge_state.json"
    content = state_file.read_text()
    data = json.loads(content)
    # All three sections must be present
    assert set(data.keys()) == {"database", "oauth", "deployment"}
