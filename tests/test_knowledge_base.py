from knowledge_base import KnowledgeBase, Article

def test_add_article():
    knowledge_base = KnowledgeBase()
    article = Article("Test Article", "This is a test article.")
    knowledge_base.add_article(article)
    assert len(knowledge_base.articles) == 1

def test_search():
    knowledge_base = KnowledgeBase()
    article1 = Article("Test Article 1", "This is a test article 1.")
    article2 = Article("Test Article 2", "This is a test article 2.")
    knowledge_base.add_article(article1)
    knowledge_base.add_article(article2)
    results = knowledge_base.search("test")
    assert len(results) == 2

def test_get_satisfaction_rating():
    knowledge_base = KnowledgeBase()
    assert knowledge_base.get_satisfaction_rating() == 0.9
