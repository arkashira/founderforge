import os
import pytest
from src.blueprint_generator import generate_blueprint, create_readme, create_dockerfile, create_cicd_pipeline, generate_code

def test_generate_blueprint():
    blueprint = generate_blueprint("test_project", "This is a test project", ["React", "Node", "PostgreSQL"])
    assert blueprint.name == "test_project"
    assert blueprint.description == "This is a test project"
    assert blueprint.tech_stack == ["React", "Node", "PostgreSQL"]

def test_create_readme():
    blueprint = generate_blueprint("test_project", "This is a test project", ["React", "Node", "PostgreSQL"])
    readme_content = create_readme(blueprint)
    assert readme_content == "# test_project\nThis is a test project"

def test_create_dockerfile():
    blueprint = generate_blueprint("test_project", "This is a test project", ["React", "Node", "PostgreSQL"])
    dockerfile_content = create_dockerfile(blueprint)
    assert dockerfile_content == "FROM node:latest\nRUN npm install\nCMD [\"npm\", \"start\"]"

def test_create_cicd_pipeline():
    blueprint = generate_blueprint("test_project", "This is a test project", ["React", "Node", "PostgreSQL"])
    cicd_pipeline_content = create_cicd_pipeline(blueprint)
    assert cicd_pipeline_content == "version: '3'\nservices:\n test_project:\n build: .\n ports:\n - '3000:3000'"

def test_generate_code(tmp_path):
    blueprint = generate_blueprint("test_project", "This is a test project", ["React", "Node", "PostgreSQL"])
    generate_code(blueprint, tmp_path)
    assert os.path.exists(os.path.join(tmp_path, "test_project", "README.md"))
    assert os.path.exists(os.path.join(tmp_path, "test_project", "Dockerfile"))
    assert os.path.exists(os.path.join(tmp_path, "test_project", "docker-compose.yml"))
