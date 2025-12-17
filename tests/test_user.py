from lib.user import *

"""
User constructs with an id, username and email
"""
def test_user_constructs():
    user = User(1, "TestName", "test@mail")
    assert user.id == 1
    assert user.username == "TestName"
    assert user.email == "test@mail"

"""
We can format users to strings nicely
"""
def test_users_format_nicely():
    user = User(1, "TestName", "test@mail")
    assert str(user) == "User(1, TestName, test@mail)"

"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "TestName", "test@mail")
    user2 = User(1, "TestName", "test@mail")
    assert user1 == user2

