import json
from dataclasses import dataclass
from urllib.request import urlopen
from argparse import ArgumentParser

@dataclass
class MarketFitScore:
    score: int
    report: str

def get_data_from_brain():
    # Simulate fetching data from BRAIN
    return {
        "source1": 0.8,
        "source2": 0.7,
        "source3": 0.9
    }

def calculate_market_fit_score(data):
    # Calculate market fit score based on data from BRAIN
    score = sum(data.values()) / len(data)
    return score * 100

def generate_report(score):
    # Generate a concise report with actionable insights
    if score > 80:
        report = "High market fit. Proceed with confidence."
    elif score > 50:
        report = "Medium market fit. Consider iterating on your idea."
    else:
        report = "Low market fit. Reconsider your idea."
    return report

def submit_idea():
    # Submit product idea and return market fit score
    data = get_data_from_brain()
    score = calculate_market_fit_score(data)
    report = generate_report(score)
    return MarketFitScore(int(score), report)

def main():
    parser = ArgumentParser()
    parser.add_argument("--idea", help="Product idea")
    args = parser.parse_args()
    if args.idea:
        result = submit_idea()
        print(json.dumps({"score": result.score, "report": result.report}))
    else:
        print("Please provide a product idea")

if __name__ == "__main__":
    main()
