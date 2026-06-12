import dataclasses
from dataclasses import dataclass
from enum import Enum
from typing import List

class Priority(Enum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3

@dataclass
class Feature:
    name: str
    description: str
    effort: int
    priority: Priority

    def __lt__(self, other):
        return (self.priority.value, self.effort) < (other.priority.value, other.effort)

class Roadmap:
    def __init__(self):
        self.features = []

    def add_feature(self, feature: Feature):
        self.features.append(feature)
        self.features.sort()

    def export_csv(self, filename: str):
        with open(filename, 'w') as f:
            f.write("Name,Description,Effort,Priority\n")
            for feature in self.features:
                f.write(f"{feature.name},{feature.description},{feature.effort},{feature.priority.name}\n")

    def export_pdf(self, filename: str):
        # For simplicity, this example does not generate a real PDF.
        # In a real application, you would use a library like reportlab.
        with open(filename, 'w') as f:
            f.write("Name\tDescription\tEffort\tPriority\n")
            for feature in self.features:
                f.write(f"{feature.name}\t{feature.description}\t{feature.effort}\t{feature.priority.name}\n")
