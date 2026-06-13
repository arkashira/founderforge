from community_forum import CommunityForum, Post

def test_add_post():
    community_forum = CommunityForum()
    post = Post("Test Post", "This is a test post.")
    community_forum.add_post(post)
    assert len(community_forum.posts) == 1

def test_search():
    community_forum = CommunityForum()
    post1 = Post("Test Post 1", "This is a test post 1.")
    post2 = Post("Test Post 2", "This is a test post 2.")
    community_forum.add_post(post1)
    community_forum.add_post(post2)
    results = community_forum.search("test")
    assert len(results) == 2
