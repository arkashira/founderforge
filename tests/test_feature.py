from feature import Feature, Roadmap, Priority
import pytest

def test_feature():
    feature = Feature("Test Feature", "This is a test feature", 5, Priority.HIGH)
    assert feature.name == "Test Feature"
    assert feature.description == "This is a test feature"
    assert feature.effort == 5
    assert feature.priority == Priority.HIGH

def test_roadmap():
    roadmap = Roadmap()
    feature1 = Feature("Feature 1", "This is feature 1", 3, Priority.HIGH)
    feature2 = Feature("Feature 2", "This is feature 2", 5, Priority.MEDIUM)
    roadmap.add_feature(feature1)
    roadmap.add_feature(feature2)
    assert len(roadmap.features) == 2
    assert roadmap.features[0].name == "Feature 1"
    assert roadmap.features[1].name == "Feature 2"

def test_export_csv(tmp_path):
    roadmap = Roadmap()
    feature1 = Feature("Feature 1", "This is feature 1", 3, Priority.HIGH)
    feature2 = Feature("Feature 2", "This is feature 2", 5, Priority.MEDIUM)
    roadmap.add_feature(feature1)
    roadmap.add_feature(feature2)
    filename = tmp_path / "roadmap.csv"
    roadmap.export_csv(str(filename))
    with open(filename, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 3
        assert lines[0].strip() == "Name,Description,Effort,Priority"
        assert lines[1].strip() == "Feature 1,This is feature 1,3,HIGH"
        assert lines[2].strip() == "Feature 2,This is feature 2,5,MEDIUM"

def test_export_pdf(tmp_path):
    roadmap = Roadmap()
    feature1 = Feature("Feature 1", "This is feature 1", 3, Priority.HIGH)
    feature2 = Feature("Feature 2", "This is feature 2", 5, Priority.MEDIUM)
    roadmap.add_feature(feature1)
    roadmap.add_feature(feature2)
    filename = tmp_path / "roadmap.pdf"
    roadmap.export_pdf(str(filename))
    with open(filename, 'r') as f:
        lines = f.readlines()
        assert len(lines) == 3
        assert lines[0].strip() == "Name\tDescription\tEffort\tPriority"
        assert lines[1].strip() == "Feature 1\tThis is feature 1\t3\tHIGH"
        assert lines[2].strip() == "Feature 2\tThis is feature 2\t5\tMEDIUM"
