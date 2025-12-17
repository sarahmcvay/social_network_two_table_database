from lib.user_repository import UserRepository
from lib.user import User

"""
We get a list of all User objects reflecting the seed data
Showing that username and email is mapped correctly
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/social_network.sql") 
    repository = UserRepository(db_connection) 

    user = repository.all() 

    assert user == [
        User(1, 'sara123', 'sara@mail'),
        User(2, 'taz123', 'taz@mail'),
        User(3, 'sam123', 'sam@mail')
    ]

"""
Test we can find a single user object 
and that it reflects the seed data correctly.
"""
def test_get_single_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = repository.find(2)
    assert user == User(2, 'taz123', 'taz@mail')

"""
Test we can create a new user record in the database
and that new data is stored correctly
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)

    user = User(None, 'joe123', 'joe@mail')
    repository.create(user)

    result = repository.all()
    assert result == [
        User(1, 'sara123', 'sara@mail'),
        User(2, 'taz123', 'taz@mail'),
        User(3, 'sam123', 'sam@mail'),
        User(4, 'joe123', 'joe@mail'),
    ]

"""
When we call UserRepository#delete
We remove a record from the database.
"""
def test_delete_record(db_connection):
    db_connection.seed("seeds/social_network.sql")
    repository = UserRepository(db_connection)
    repository.delete(1) 

    result = repository.all()
    assert result == [
        User(2, 'taz123', 'taz@mail'),
        User(3, 'sam123', 'sam@mail'),
    ]
