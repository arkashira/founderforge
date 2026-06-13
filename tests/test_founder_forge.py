from founder_forge import FounderForge
from knowledge_base import KnowledgeBase, Article
from community_forum import CommunityForum, Post

def test_get_knowledge_base_articles():
    founder_forge = FounderForge()
    knowledge_base = KnowledgeBase()
    article = Article("Test Article", "This is a test article.")
    knowledge_base.add_article(article)
    founder_forge.knowledge_base = knowledge_base
    assert len(founder_forge.get_knowledge_base_articles()) == 1

def test_get_community_forum_posts():
    founder_forge = FounderForge()
    community_forum = CommunityForum()
    post = Post("Test Post", "This is a test post.")
    community_forum.add_post(post)
    founder_forge.community_forum = community_forum
    assert len(founder_forge.get_community_forum_posts()) == 1

def test_search():
    founder_forge = FounderForge()
    knowledge_base = KnowledgeBase()
    article = Article("Test Article", "This is a test article.")
    knowledge_base.add_article(article)
    founder_forge.knowledge_base = knowledge_base
    community_forum = CommunityForum()
    post = Post("Test Post", "This is a test post.")
    community_forum.add_post(post)
    founder_forge.community_forum = community_forum
    results = founder_forge.search("test")
    assert len(results) == 2
