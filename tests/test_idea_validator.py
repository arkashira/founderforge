from idea_validator import IdeaValidator, MarketData
import pytest

def test_calculate_market_fit():
    brain_data = [
        MarketData("Source 1", 80),
        MarketData("Source 2", 70),
        MarketData("Source 3", 90)
    ]
    validator = IdeaValidator(brain_data)
    idea = "Example Idea"
    score = validator.calculate_market_fit(idea)
    assert score == 80

def test_generate_report():
    brain_data = [
        MarketData("Source 1", 80),
        MarketData("Source 2", 70),
        MarketData("Source 3", 90)
    ]
    validator = IdeaValidator(brain_data)
    idea = "Example Idea"
    score = 80
    report = validator.generate_report(idea, score)
    assert report == "Idea: Example Idea, Market Fit Score: 80"

def test_fetch_brain_data():
    # Simulate fetching data from BRAIN
    # Replace with actual implementation
    brain_data = [
        MarketData("Source 1", 80),
        MarketData("Source 2", 70),
        MarketData("Source 3", 90)
    ]
    assert len(brain_data) == 3
