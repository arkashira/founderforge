from src.blueprint_generator import generate_blueprint, compile_blueprint, version_blueprint, store_blueprint
import pytest

def test_generate_blueprint():
    blueprint = generate_blueprint("My App", "Node")
    assert blueprint.name == "My App"
    assert blueprint.tech_stack == "Node"
    assert blueprint.readme == "# My App README"
    assert blueprint.dockerfile == "FROM node"
    assert blueprint.ci_cd_pipeline == "pipeline for My App"

def test_compile_blueprint():
    blueprint = generate_blueprint("My App", "Node")
    assert compile_blueprint(blueprint) == True

def test_version_blueprint():
    blueprint = generate_blueprint("My App", "Node")
    assert version_blueprint(blueprint) == "v1.0 - My App"

def test_store_blueprint():
    blueprint = generate_blueprint("My App", "Node")
    assert store_blueprint(blueprint) == "Blueprint stored in Git repo for My App"

def test_generate_blueprint_edge_case():
    with pytest.raises(TypeError):
        generate_blueprint(123, "Node")

def test_compile_blueprint_edge_case():
    blueprint = generate_blueprint("My App", "Node")
    blueprint.readme = None
    with pytest.raises(AttributeError):
        compile_blueprint(blueprint)
