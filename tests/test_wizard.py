from src.wizard import create_database, configure_oauth2, deploy_to_managed_platform
import json

def test_create_database():
    config = {
        "username": "test_user",
        "password": "test_password",
        "host": "test_host",
        "port": 5432,
        "database": "test_database",
    }
    database_config = create_database(config)
    assert database_config == config

def test_configure_oauth2():
    config = {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret",
        "authorization_url": "https://test_authorization_url",
        "token_url": "https://test_token_url",
    }
    oauth2_config = configure_oauth2(config)
    assert oauth2_config == config

def test_deploy_to_managed_platform():
    database_config = {
        "username": "test_user",
        "password": "test_password",
        "host": "test_host",
        "port": 5432,
        "database": "test_database",
    }
    oauth2_config = {
        "client_id": "test_client_id",
        "client_secret": "test_client_secret",
        "authorization_url": "https://test_authorization_url",
        "token_url": "https://test_token_url",
    }
    deployment_config = deploy_to_managed_platform(database_config, oauth2_config)
    assert deployment_config["database_config"] == database_config
    assert deployment_config["oauth2_config"] == oauth2_config
