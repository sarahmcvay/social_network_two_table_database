-- file social_network.sql

DROP TABLE IF EXISTS users CASCADE;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
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
    user_id int,
    constraint fk_user foreign key(user_id)
    references users(id)
    on delete cascade
);

-- seed information
INSERT INTO users (username, email) VALUES ('sara123', 'sara@mail');
INSERT INTO users (username, email) VALUES ('taz123', 'taz@mail');
INSERT INTO users (username, email) VALUES ('sam123', 'sam@mail');

INSERT INTO posts (title, content, views, user_id) VALUES ('today', 'great day', 100, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('monday', 'fun trip', 200, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('tuesday', 'bad trip', 50, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('recipe1', 'chocolate cake', 70, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('recipe2', 'salad', 10, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('recipe3', 'fish pie', 60, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('travel1', 'London', 90, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('travel2', 'San Fran', 180, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('travel3', 'Tokyo', 300, 3);
