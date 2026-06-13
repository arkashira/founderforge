from knowledge_base import KnowledgeBase
from community_forum import CommunityForum
from typing import List

class FounderForge:
    def __init__(self):
        self.knowledge_base = KnowledgeBase()
        self.community_forum = CommunityForum()

    def get_knowledge_base_articles(self) -> List:
        return self.knowledge_base.articles

    def get_community_forum_posts(self) -> List:
        return self.community_forum.posts

    def search(self, query: str) -> List:
        knowledge_base_results = self.knowledge_base.search(query)
        community_forum_results = self.community_forum.search(query)
        return knowledge_base_results + community_forum_results
