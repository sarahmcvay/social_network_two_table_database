from lib.post_repository import PostRepository
from lib.post import *
# we are testing the behaviour of the PostRepository, typical responsibilities 
# all() return all posts -- find(id) return one post -- create(post) insert post
# we should make sure we map to user stories: 
# --I'd like to create posts associated with my user account.
#         Implies that posts table has a user_id(foreign key) 
#         Test that the repository correctly stores and retrieves the relationship

# --I'd like each of my posts to have a title and a content.
#         Implies that retrieved objects contain title and content

# --I'd like each of my posts to have a number of views.
#         Implies views can be read and potentially updated

"""
Test that all posts can be read from the database 
Showing that title content views and user_id is mapped correctly
"""

def test_all_returns_all_posts(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    posts = repository.all()

    assert posts == [
        Post(1, 'today', 'great day', 100, 1),
        Post(2, 'monday', 'fun trip', 200, 1),
        Post(3, 'tuesday', 'bad trip', 50, 1),
        Post(4, 'recipe1', 'chocolate cake', 70, 2),
        Post(5, 'recipe2', 'salad', 10, 2),
        Post(6, 'recipe3', 'fish pie', 60, 2),
        Post(7, 'travel1', 'London', 90, 3),
        Post(8, 'travel2', 'San Fran', 180, 3),
        Post(9, 'travel3', 'Tokyo', 300, 3),
    ] 

"""
Test we can find a single post 
and that it has a title and contents and a user association
"""
def test_can_find_single_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = repository.find(1)

    assert post == Post(1, 'today', 'great day', 100, 1)

"""
Test that posts can be created and associated with a user
shows title, content and views are stored
"""

def test_create_adds_new_post(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = PostRepository(db_connection)

    post = Post(None, 'recipe4', 'bread', 150, 2)
    repository.create(post)

    posts = repository.all()
    assert posts[-1] == Post(10, 'recipe4', 'bread', 150, 2)
