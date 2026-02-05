-- USERS
insert into users values (1, 'Alice Johnson', 'alice@email.com', 'USA', '2024-01-10');
insert into users values (2, 'Bob Smith', 'bob@email.com', 'Canada', '2024-03-15');
insert into users values (3, 'Carlos Diaz', 'carlos@email.com', 'USA', '2024-06-20');
insert into users values (4, 'Diana Lee', 'diana@email.com', 'UK', '2024-02-05');
insert into users values (5, 'Ethan Brown', 'ethan@email.com', 'USA', '2024-07-01');

-- SUBSCRIPTION TYPES
insert into subscription_type values (1, 'Basic', 8.99, 1, 'SD');
insert into subscription_type values (2, 'Premium', 15.99, 4, '4K');
insert into subscription_type values (3, 'Family', 12.99, 3, 'HD');

-- SUBSCRIPTIONS
insert into subscription values (1, 1, 2, '2024-01-10', null);
insert into subscription values (2, 2, 1, '2024-03-15', null);
insert into subscription values (3, 3, 2, '2024-06-20', null);
insert into subscription values (4, 4, 3, '2024-02-05', null);
insert into subscription values (5, 5, 1, '2024-07-01', '2024-12-31');

-- MOVIES
insert into movie values (1, 'Galaxy War', 2022, 130, 'PG-13');
insert into movie values (2, 'Love in Paris', 2021, 110, 'PG');
insert into movie values (3, 'Haunted Manor', 2023, 95, 'R');
insert into movie values (4, 'The Last Hero', 2020, 140, 'PG-13');
insert into movie values (5, 'Laugh Out Loud', 2019, 100, 'PG');

-- GENRES
insert into genre values (1, 'Action');
insert into genre values (2, 'Romance');
insert into genre values (3, 'Horror');
insert into genre values (4, 'Comedy');

-- MOVIE-GENRES
insert into content_genres values (1, 1);
insert into content_genres values (2, 2);
insert into content_genres values (3, 3);
insert into content_genres values (4, 1);
insert into content_genres values (5, 4);
insert into content_genres values (5, 2); -- rom-com

-- WATCH HISTORY
insert into watch_history values (1, 1, 1, '2025-01-10 20:00:00', 130, true);
insert into watch_history values (2, 1, 5, '2025-01-11 22:00:00', 100, true);
insert into watch_history values (3, 2, 2, '2025-01-09 19:00:00', 60, false);
insert into watch_history values (4, 2, 2, '2025-01-09 20:30:00', 110, true);
insert into watch_history values (5, 3, 1, '2025-01-12 21:00:00', 130, true);
insert into watch_history values (6, 3, 4, '2025-01-13 23:30:00', 140, true);
insert into watch_history values (7, 4, 3, '2025-01-08 00:30:00', 95, true);
insert into watch_history values (8, 5, 5, '2025-01-15 18:00:00', 40, false);

-- RATINGS
insert into ratings values (1, 1, 1, 5);
insert into ratings values (2, 1, 5, 4);
insert into ratings values (3, 2, 2, 3);
insert into ratings values (4, 3, 1, 4);
insert into ratings values (5, 3, 4, 5);
insert into ratings values (6, 4, 3, 4);
insert into ratings values (7, 5, 5, 2);
