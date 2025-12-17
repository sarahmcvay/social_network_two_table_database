class Post:

    def __init__(self, id, title, content, views, user_id):
        self.id = id
        self.title = title
        self.content = content 
        self.views = views
        self.user_id = user_id
    
    def __eq__(self, other):
        if not isinstance(other, Post):
            return False 
        return (
            self.title == other.title and
            self.content == other.content and
            self.views == other.views and
            self.user_id == other.user_id
        )
