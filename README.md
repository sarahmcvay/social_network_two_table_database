TWO TABLES DESIGN RECIPE

USER STORIES:
As a social network user,
--So I can have my information registered,
--I'd like to have a user account with my email address.

As a social network user,
--So I can have my information registered,
--I'd like to have a user account with my username.

As a social network user,
--So I can write on my timeline,
--I'd like to create posts associated with my user account.

As a social network user,
--So I can write on my timeline,
--I'd like each of my posts to have a title and a content.

As a social network user,
--So I can know who reads my posts,
--I'd like each of my posts to have a number of views.

USER NOUNS: user account, email, username, timeline, posts, title, content, views

INFERED TABLE:
| Record            | Properties            |
|--------------     |-----------------      |
| user account      | email, username       |
| posts             | title, content, views | 

FIRST TABLE NAME:(always plural)
users
TABLE COLUMNS: (column name and data type)
    id: SERIAL
    username: text
    email: text

SECOND TABLE NAME:(always plural)
posts
TABLE COLUMNS: (column name and data type)
    id: SERIAL
    title: text
    content: text
    views: int

TABLES RELATIONSHIP
Identify cardinality of the relationship: one-to-one, one-to-many or many-to-many
option a - users can have many posts, so posts belongs to users 
option b - posts can have many users... incorrect. 

As such the foreign key is on posts, the child table. 

```sql
WRITE SQL
    file: social_network.sql
----parent table, create table without foreign key first
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username text,
        email text
    );

    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title text,
        content text,
        views int,
        user_id datatype,
        constraint fk_user foreign key(user_id)
            references users(id)
            on delete cascade
    );

INPUT file.SQL CODE
INPUT SEED INFO

RUN SQL
    psql social_network < path/social_network.sql
```
```python
EXAMPLE TESTS-link to user stories

"""PostRepository 
Test that all posts can be read from the database 
Showing that title content views and user_id is mapped correctly
"""
"""PostRepository
Test we can find a single post 
and that it has a title and contents and a user association
"""
"""PostRepository
Test that posts can be created and associated with a user
Shows title, content and views are stored
"""
"""UserRepository
Test we can get a list of all User objects reflecting the seed data
Showing that username and email is mapped correctly
"""
"""UserRepository
Test we can find a single user object 
and that it reflects the seed data correctly.
"""
"""UserRepository
Test we can create a new user record in the database
and that new data is stored correctly
"""
"""UserRepository
Test we can remove a user record from the database.
And the database reflects updated information. 
"""
