create table users (
    user_id integer primary key,
    name varchar(20) not null,
    email varchar(50) not null,
    country varchar(15),
    signup_date date not null
);

create table subscription_type (
    subscription_type_id integer primary key,
    name varchar(20) not null,
    monthly_price decimal(5,2) not null,
    max_streams integer not null,
    video_quality varchar(3),
    constraint quality_constraint 
        check (video_quality in ('SD', 'HD', '4K'))
);

create table subscription (
    subscription_id integer primary key,
    user_id integer not null,
    subscription_type_id integer not null,
    start_date date not null,
    end_date date,
    foreign key (user_id) references users(user_id),
    foreign key (subscription_type_id) references subscription_type(subscription_type_id)
);

create table movie (
    movie_id integer primary key,
    title varchar(30) not null,
    release_year smallint not null,
    duration_min smallint,
    age_rating varchar(5),
    constraint rating_constraint 
        check (age_rating in ('G','PG','PG-13','R'))
);

create table genre (
    genre_id integer primary key,
    name varchar(15) not null
);

create table content_genres (
    movie_id integer not null,
    genre_id integer not null,
    primary key (movie_id, genre_id),
    foreign key (movie_id) references movie(movie_id),
    foreign key (genre_id) references genre(genre_id)
);

create table watch_history (
    watch_id integer primary key,
    user_id integer not null,
    movie_id integer not null,
    watch_date datetime not null,
    minutes_watched integer not null,
    completed boolean not null,
    foreign key (user_id) references users(user_id),
    foreign key (movie_id) references movie(movie_id)
);

create table ratings (
    rating_id integer primary key,
    user_id integer not null,
    movie_id integer not null,
    rating tinyint not null check (rating between 1 and 5),
    foreign key (user_id) references users(user_id),
    foreign key (movie_id) references movie(movie_id)
);
