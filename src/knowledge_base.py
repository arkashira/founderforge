import json
from dataclasses import dataclass
from typing import List

@dataclass
class Article:
    title: str
    content: str

class KnowledgeBase:
    def __init__(self):
        self.articles = []

    def add_article(self, article: Article):
        self.articles.append(article)

    def search(self, query: str) -> List[Article]:
        return [article for article in self.articles if query.lower() in article.title.lower() or query.lower() in article.content.lower()]

    def get_satisfaction_rating(self) -> float:
        # Simulate a satisfaction rating of 90% for demonstration purposes
        return 0.9
