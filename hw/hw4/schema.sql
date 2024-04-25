CREATE DATABASE mlk224_DB;
USE mlk224_DB;

CREATE TABLE artist(
    `artist_name` VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE 
);

CREATE TABLE album(
    `album_name` VARCHAR(50) NOT NULL,
    `release_date` DATETIME,
    `artist_name` VARCHAR(50),
    PRIMARY KEY (`album_name`, `artist_name`),
    FOREIGN KEY (`artist_name`) REFERENCES artist(`artist_name`)
);

CREATE TABLE song(
    `song_title` VARCHAR(50) NOT NULL,
    `artist_name` VARCHAR(50) NOT NULL,
    `album_name` VARCHAR(50),
    PRIMARY KEY (`song_title`, `artist_name`),
    FOREIGN KEY (`artist_name`) REFERENCES artist(`artist_name`),
    FOREIGN KEY (`album_name`) REFERENCES album(`album_name`)
);

CREATE TABLE user(
    `username` VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE
);

CREATE TABLE playlist(
    `playlist_title` VARCHAR(50) NOT NULL,
    `time_created` DATETIME NOT NULL,
    `username` VARCHAR(50),
    PRIMARY KEY (`playlist_title`, `time_created`),
    FOREIGN KEY (`username`) REFERENCES user(`username`)
);

CREATE TABLE playlist_song(
    `playlist_title` VARCHAR(50) NOT NULL,
    `song_title` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`playlist_title`, `song_title`),
    FOREIGN KEY (`playlist_title`) REFERENCES playlist(`playlist_title`),
    FOREIGN KEY (`song_title`) REFERENCES song(`song_title`)
);

CREATE TABLE rating(
    `username` VARCHAR(50) NOT NULL,
    `song_title` VARCHAR(50) NOT NULL,
    `album_name` VARCHAR(50) NOT NULL,
    `rating` INT CHECK (rating >= 1 AND rating <= 5), 
    PRIMARY KEY (`username`, `song_title`, `album_name`),
    FOREIGN KEY (`username`) REFERENCES user(`username`),
    FOREIGN KEY (`song_title`) REFERENCES song(`song_title`),
    FOREIGN KEY (`album_name`) REFERENCES album(`album_name`)
);

CREATE TABLE genre (
    `song_title` VARCHAR(50) NOT NULL,
    `genre` VARCHAR(10),
    PRIMARY KEY (`song_title`, `genre`),
    FOREIGN KEY (`song_title`) REFERENCES song(`song_title`)
);

-- Inserting dummy artist data
INSERT INTO artist (artist_name) VALUES 
('John Doe'),
('Jane Smith'),
('Michael Johnson'),
('Emily White'),
('Alex Brown'),
('Nikhila Sundar'),
('Maha Kanakala'),
('Adam Trabelsi'),
('Chase Atlantic'),
('Jhene Aiko');

-- Inserting dummy album data
INSERT INTO album (album_name, release_date, artist_name) VALUES 
('Greatest Hits', '2020-01-01', 'John Doe'),
('Love Songs', '2018-05-15', 'Jane Smith'),
('Rock Anthems', '2019-09-20', 'Michael Johnson'),
('Pop Hits', '2021-03-10', 'Emily White'),
('Classical Collection', '2022-07-05', 'Alex Brown'),
('Classical Collection 2', '2022-08-05', 'Nikhila Sundar'), 
('Classical Collection 3', '2024-08-05', 'Adam Trabelsi'),
('Love Songs 2', '2021-08-05', 'Maha Kanakala'),          
('Rock Anthems 2', '2020-09-20', 'Chase Atlantic'),      
('Greatest Hits 2', '2019-10-20', 'Michael Johnson'); 

-- Inserting dummy song data
INSERT INTO song (song_title, artist_name, album_name) VALUES 
('Song 1', 'John Doe', 'Greatest Hits'),
('Song 2', 'John Doe', 'Greatest Hits'),
('Song 3', 'Jane Smith', 'Love Songs'),
('Song 4', 'Michael Johnson', 'Rock Anthems'),
('Song 5', 'Emily White', 'Pop Hits'),
('Song 6', 'Alex Brown', 'Classical Collection'),
('Song 7', 'John Doe', 'Greatest Hits'),
('Song 8', 'Jane Smith', 'Love Songs'),
('Song 9', 'Michael Johnson', 'Rock Anthems'),
('Song 10', 'Emily White', 'Pop Hits');

-- Inserting dummy user data
INSERT INTO user (username) VALUES 
('user123'),
('musiclover'),
('rockstar'),
('jazzfan'),
('metalhead'),
('classicfan'),
('popstar'),
('hiphophead'),
('edmdj'),
('bluesmaster');

-- Inserting dummy playlist data
INSERT INTO playlist (playlist_title, time_created, username) VALUES 
('My Playlist', '2023-04-25 18:01:00', 'user123'),
('Favorites', '2023-04-25 18:01:00', 'musiclover'),
('Top Picks', '2023-04-25 18:01:00', 'rockstar'),
('Chill Vibes', '2023-04-25 18:01:00', 'jazzfan'),
('Workout Mix', '2023-04-25 18:01:00', 'metalhead'),
('Relaxation Station', '2023-04-25 18:01:00', 'classicfan'),
('Party Playlist', '2023-04-25 18:01:00', 'popstar'), 
('Rap Rotation', '2023-04-25 18:01:00', 'hiphophead'),
('Dance Floor', '2023-04-25 18:01:00', 'edmdj'),
('Blues Tunes', '2023-04-25 18:01:00', 'bluesmaster');

-- Inserting dummy playlist-song mappings
INSERT INTO playlist_song (playlist_title, song_title) VALUES 
('My Playlist', 'Song 1'),
('My Playlist', 'Song 2'),
('Favorites', 'Song 3'),
('Top Picks', 'Song 4'),
('Chill Vibes', 'Song 5'),
('Workout Mix', 'Song 6'),
('Relaxation Station', 'Song 7'),
('Party Playlist', 'Song 8'),
('Rap Rotation', 'Song 9'), 
('Dance Floor', 'Song 10');

-- Inserting dummy ratings
INSERT INTO rating (username, song_title, album_name, rating) VALUES 
('user123', 'Song 1', 'Greatest Hits', 4),
('musiclover', 'Song 2', 'Greatest Hits', 5),
('rockstar', 'Song 3', 'Love Songs', 3),
('jazzfan', 'Song 4', 'Rock Anthems', 4),
('metalhead', 'Song 5', 'Pop Hits', 5),
('classicfan', 'Song 6', 'Classical Collection', 5),
('popstar', 'Song 7', 'Greatest Hits', 4),
('hiphophead', 'Song 8', 'Greatest Hits 2', 4),
('edmdj', 'Song 9', 'Love Songs 2', 5),
('bluesmaster', 'Song 10', 'Greatest Hits', 5);

INSERT INTO genre (song_title, genre) VALUES
('Song 1', 'Pop'),
('Song 2', 'Rock'),
('Song 3', 'Love'),
('Song 4', 'Rock'),
('Song 5', 'Pop'),
('Song 6', 'Classical'),
('Song 7', 'Pop'),
('Song 8', 'Hip Hop'),
('Song 9', 'Love'),
('Song 10', 'Pop');