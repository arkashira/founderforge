import json
from dataclasses import dataclass
from typing import List

@dataclass
class Post:
    title: str
    content: str

class CommunityForum:
    def __init__(self):
        self.posts = []

    def add_post(self, post: Post):
        self.posts.append(post)

    def search(self, query: str) -> List[Post]:
        return [post for post in self.posts if query.lower() in post.title.lower() or query.lower() in post.content.lower()]
