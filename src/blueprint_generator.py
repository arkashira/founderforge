import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class Blueprint:
    name: str
    tech_stack: str
    readme: str
    dockerfile: str
    ci_cd_pipeline: str

def generate_blueprint(name: str, tech_stack: str) -> Blueprint:
    if not isinstance(name, str) or not isinstance(tech_stack, str):
        raise TypeError("Both name and tech_stack must be strings")
    readme = f"# {name} README"
    dockerfile = f"FROM {tech_stack.lower()}"
    ci_cd_pipeline = f"pipeline for {name}"
    return Blueprint(name, tech_stack, readme, dockerfile, ci_cd_pipeline)

def compile_blueprint(blueprint: Blueprint) -> bool:
    if blueprint.readme is None:
        raise AttributeError("readme cannot be None")
    # Simulate compilation and linting
    return True

def version_blueprint(blueprint: Blueprint) -> str:
    return f"v1.0 - {blueprint.name}"

def store_blueprint(blueprint: Blueprint) -> str:
    # Simulate storing in a Git repo
    return f"Blueprint stored in Git repo for {blueprint.name}"
