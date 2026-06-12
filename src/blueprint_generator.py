import argparse
import json
import os
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Blueprint:
    name: str
    description: str
    tech_stack: list

def generate_blueprint(name, description, tech_stack):
    blueprint = Blueprint(name, description, tech_stack)
    return blueprint

def create_readme(blueprint):
    readme_content = f"# {blueprint.name}\n{blueprint.description}"
    return readme_content

def create_dockerfile(blueprint):
    dockerfile_content = f"FROM node:latest\nRUN npm install\nCMD [\"npm\", \"start\"]"
    return dockerfile_content

def create_cicd_pipeline(blueprint):
    cicd_pipeline_content = f"version: '3'\nservices:\n {blueprint.name}:\n build: .\n ports:\n - '3000:3000'"
    return cicd_pipeline_content

def generate_code(blueprint, output_dir):
    os.mkdir(os.path.join(output_dir, blueprint.name))
    with open(os.path.join(output_dir, blueprint.name, "README.md"), "w") as f:
        f.write(create_readme(blueprint))
    with open(os.path.join(output_dir, blueprint.name, "Dockerfile"), "w") as f:
        f.write(create_dockerfile(blueprint))
    with open(os.path.join(output_dir, blueprint.name, "docker-compose.yml"), "w") as f:
        f.write(create_cicd_pipeline(blueprint))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", help="Name of the project")
    parser.add_argument("--description", help="Description of the project")
    parser.add_argument("--tech_stack", nargs="+", help="Tech stack of the project")
    args = parser.parse_args()
    blueprint = generate_blueprint(args.name, args.description, args.tech_stack)
    generate_code(blueprint, ".")

if __name__ == "__main__":
    main()
