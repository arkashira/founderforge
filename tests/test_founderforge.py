import pytest
from founderforge import submit_idea, MarketFitScore, generate_report

def test_submit_idea():
    result = submit_idea()
    assert isinstance(result, MarketFitScore)
    assert 0 <= result.score <= 100
    assert isinstance(result.report, str)

def test_calculate_market_fit_score():
    data = {"source1": 0.8, "source2": 0.7, "source3": 0.9}
    score = submit_idea().score
    assert score == int((0.8 + 0.7 + 0.9) / 3 * 100)

def test_generate_report():
    score = 90
    report = generate_report(score)
    assert report == "High market fit. Proceed with confidence."

def test_main():
    # Test main function with idea
    import sys
    import io
    from contextlib import redirect_stdout
    with redirect_stdout(io.StringIO()) as f:
        sys.argv = ["founderforge", "--idea", "test_idea"]
        from src.founderforge import main
        main()
        output = f.getvalue()
        assert "score" in output
        assert "report" in output
