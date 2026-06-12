import argparse
import json
import sys
import uuid
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Any


@dataclass
class DatabaseConfig:
    provider: str
    instance_id: str
    connection_url: str


@dataclass
class OAuthConfig:
    provider: str
    client_id: str
    client_secret: str
    redirect_uri: str


@dataclass
class DeploymentConfig:
    platform: str
    service_name: str
    env: Dict[str, str]


class Wizard:
    """A very small, self‑contained wizard that pretends to provision resources."""

    def __init__(self, output_dir: Path | None = None):
        self.output_dir = output_dir or Path.cwd()
        self.state: Dict[str, Any] = {}

    # --------------------------------------------------------------------- #
    # Step 1 – Database
    # --------------------------------------------------------------------- #
    def create_database(self, provider: str = "postgresql") -> DatabaseConfig:
        """Simulate creation of a cloud PostgreSQL instance."""
        instance_id = f"{provider}-{uuid.uuid4().hex[:8]}"
        connection_url = f"postgresql://{instance_id}.example.com:5432/mydb"
        db_cfg = DatabaseConfig(provider=provider, instance_id=instance_id, connection_url=connection_url)
        self.state["database"] = asdict(db_cfg)
        return db_cfg

    # --------------------------------------------------------------------- #
    # Step 2 – OAuth2
    # --------------------------------------------------------------------- #
    def configure_oauth(self, provider: str = "github") -> OAuthConfig:
        """Simulate OAuth2 client registration."""
        client_id = f"{provider}_client_{uuid.uuid4().hex[:6]}"
        client_secret = uuid.uuid4().hex
        redirect_uri = "https://myapp.example.com/auth/callback"
        oauth_cfg = OAuthConfig(
            provider=provider,
            client_id=client_id,
            client_secret=client_secret,
            redirect_uri=redirect_uri,
        )
        self.state["oauth"] = asdict(oauth_cfg)
        return oauth_cfg

    # --------------------------------------------------------------------- #
    # Step 3 – Deployment
    # --------------------------------------------------------------------- #
    def generate_deployment(self, platform: str = "render", service_name: str = "my-mvp") -> DeploymentConfig:
        """Generate a minimal deployment configuration."""
        env = {
            "DATABASE_URL": self.state["database"]["connection_url"],
            "OAUTH_CLIENT_ID": self.state["oauth"]["client_id"],
            "OAUTH_CLIENT_SECRET": self.state["oauth"]["client_secret"],
            "OAUTH_REDIRECT_URI": self.state["oauth"]["redirect_uri"],
        }
        dep_cfg = DeploymentConfig(platform=platform, service_name=service_name, env=env)
        self.state["deployment"] = asdict(dep_cfg)
        return dep_cfg

    # --------------------------------------------------------------------- #
    # Persistence helpers
    # --------------------------------------------------------------------- #
    def save_state(self) -> Path:
        """Write the accumulated state as JSON to the output directory."""
        out_path = self.output_dir / "founderforge_state.json"
        out_path.write_text(json.dumps(self.state, indent=2))
        return out_path

    # --------------------------------------------------------------------- #
    # CLI entry point
    # --------------------------------------------------------------------- #
    @staticmethod
    def _build_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            prog="founderforge",
            description="Interactive wizard that simulates MVP setup."
        )
        parser.add_argument(
            "--output-dir",
            type=Path,
            default=".",
            help="Directory where the wizard will write its state file."
        )
        return parser

    @classmethod
    def cli(cls) -> None:
        parser = cls._build_parser()
        args = parser.parse_args()
        wizard = cls(output_dir=args.output_dir)

        print("=== Step 1: Creating PostgreSQL database ===")
        db_cfg = wizard.create_database()
        print(json.dumps(asdict(db_cfg), indent=2))

        print("\n=== Step 2: Configuring OAuth2 ===")
        oauth_cfg = wizard.configure_oauth()
        print(json.dumps(asdict(oauth_cfg), indent=2))

        print("\n=== Step 3: Generating deployment config ===")
        dep_cfg = wizard.generate_deployment()
        print(json.dumps(asdict(dep_cfg), indent=2))

        state_path = wizard.save_state()
        print(f"\nWizard state saved to {state_path}")


if __name__ == "__main__":
    # When executed as a script, run the CLI.
    Wizard.cli()
