## Social Network - two table database design

### Requirement / User Stories

As a social network user:
- So my info is registered, I'd like a user account with my email address.
- So my info is registered, I'd like a user account with my username.
- So I can write on my timeline, I'd like to create posts associated with my user account.
- So I can write on my timeline, I'd like each posts to have a title and content.
- So I know how popular my posts are, I'd like each posts to have a number of views.

Step 1: Extract Nouns --> account, email, username, timeline, posts, title, content, views

## Tables
Step 2: Set out tables and identify cardinality of the relationship
### users (parent)

| Column  | Type | Notes |
|---------|------|-------|
| id      | SERIAL | Primary key |
| username | TEXT | User’s username |
| email   | TEXT | User’s email address |

### posts (child)

| Column   | Type | Notes |
|---------|------|-------|
| id      | SERIAL | Primary key |
| title   | TEXT | Title for post |
| content | TEXT | Content added to post |
| views   | INT | Number of views |
| user_id | INT | Foreign key → users.id |


### SQL
```sql
    file: social_network.sql
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        username text,
        email text);

    CREATE TABLE posts (
        id SERIAL PRIMARY KEY,
        title text,
        content text,
        views int,
        user_id datatype,
        constraint fk_user foreign key(user_id) references users(id)
            on delete cascade);

    psql social_network < path/social_network.sql
```
### Tests
Tests to demonstrate the database design and repositories
meet the user stories described above.

UserRepository

- Can retrieve all users  
  (shows username and email are mapped correctly)

- Can find a single user by id  
  (shows the data matches the seeded user)

- Can create a new user  
  (shows new user data is stored correctly)

- Can delete a user  
  (shows the database reflects updated information)

PostRepository
- Can retrieve all posts from the database  
  (shows title, content, views, and user_id are mapped correctly)

- Can find a single post by id  
  (shows a post has a title, content, and an associated user)

- Can create a new post associated with a user  
  (shows title, content, and views are stored correctly)

