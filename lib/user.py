class User:

    def __init__(self, id, username, email):
    # def __init__(self, id, username, email):
        # should i take the id out of this? 
        self.id = id
        self.username = username
        self.email = email

    def __eq__(self, other):
        # return self.__dict__ == other.__dict__
        if not isinstance(other, User):
            return False 
        return (
            self.username == other.username and
            self.email == other.email
        )

    def __repr__(self):
        return f"User({self.id}, {self.username}, {self.email})"
