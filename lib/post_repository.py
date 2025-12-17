from lib.post import *

class PostRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute('SELECT * from posts')
        posts = []
        for row in rows: 
            item = Post(
                row['id'], 
                row['title'], 
                row['content'], 
                row['views'], 
                row['user_id']
                )
            posts.append(item)
        return posts

    def find(self, user_id):
        rows = self.connection.execute(
            'SELECT * from posts WHERE id = %s',
            [user_id]
        )
        row = rows[0]
        return Post(
            row['id'], 
            row['title'], 
            row['content'], 
            row['views'], 
            row['user_id']
            )

    def create(self, post):
        self.connection.execute(
            'INSERT INTO posts (title, content, views, user_id) VALUES (%s, %s, %s, %s)', 
            [post.title, post.content, post.views, post.user_id]
        )
        return None 