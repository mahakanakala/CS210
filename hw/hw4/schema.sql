/*

Implement a Music relational (SQL) database, of the kind that might be used by Spotify or Amazon Music. The database has artists, albums, songs, users, playlists, and ratings.

Type up all the required work specified in the following sections in any word processor, then convert to a PDF file named music_db.pdf. (Handwritten work is NOT acceptable.) Submit this file to Canvas - only one submission per group, please.

You are allowed up to 3 submissions, only the last submission will be graded.

NOTE: You may populate the tables with data for your own testing, but we do not want you to turn in any of the data, or the results of any of your queries. We are only asking for the document with the required SQL statements for table creation and queries.

Database Schema (50 pts)
You are given the following description of the entities that need to be stored in the database. Your task is to design a database schema (set of tables) to store these entities.

Your schema must be minimally redundant in storing data. In other words, you should build a set of tables that minimize the repetition of data, by using foreign keys - credit will be in accordance with this.

Artist: An individual or a group/band, uniquely identified by their name. An artist might release albums, as well as songs that are not in albums (singles).
Song: A song has a title and is performed by an artist, either as a part of an album, or as a single that's not part of an album. Every song in an album has the release date of the album, but a single song has its own release date. A song title is unique to an artist (the same artist records a song exactly once), but the title may be shared by multiple artists (i.e. covers).
A song belongs to one or more genres. For example, a song could be in a single genre, such as R & B, or could be in multiple genres such as Pop and Rock. Genres are pre-defined, and every song must be in at least one genre. Also, songs in an album need not all be in the same genre.

Album: An album is a collection of songs released by an artist, on a certain date. For example, the album Achtung Baby was made by the artist (band) U2, released on November 19, 1991. An album name is not unique, but the combination of album name and artist name is unique.
User: A user is uniquely identified by their username. A user can optionally have one or more playlists, and optionally have ratings for songs, albums, or playlists. In other words, it's possible that a user has no playlists, and hasn't given any ratings.
Playlist: A user can make any number of playlists of songs. Note: A playlist may not include an entire album, only individual songs. Each song is either from some album, or a single that's not in any album.
Every playlist has a title, and a date+time when it was created. A playlist may be modified any number of times after creation by adding or removing songs, but the title and date+time will not change.

The title of a playlist is not unique since different users might create playlists with the same title. However, a user's playlists will have unique titles.

Rating: A user could rate an album, a song (even if it's in an album), or a playlist. A rating is limited to 1,2,3,4, or 5 (numeric), and is made on a specific date.
Note: The items listed above do NOT necessarily correspond 1-1 with tables, although some of them might. They simply detail all the data you will need to store whatever table structure you adopt. This also means you can create as many tables as you need to reduce redundancy.

Your database structure should have the most appropriate data type and size for each column in each table.

For size of data, think of a realistic online music service and imagine how many songs/artists/albums/playlists/users/ratings it might have to support. The idea is to use the least amount of storage space for each column that will be able to store the entire range of foreseeable values.

Make sure you define and specify all primary keys, foreign keys, unique valued columns or unique valued combination of columns, and null/non-null properties for columns.

In the document you will submit, type in the create table statement for each of the tables you create in the database. If you don't have the full create statement for a table, you will not get credit for it.
Note: When you test your design in MySQL, you might use alter table statements after the initial create. However, for the submission, you are required to rewrite the whole sequence as a single create table statement per table

*/

CREATE DATABASE DB;
USE DB;

CREATE TABLE artist(
    `artist_name` VARCHAR(50) PRIMARY KEY NOT NULL UNIQUE 
);

CREATE TABLE album(
    `album_name` VARCHAR(50) NOT NULL,
    `release_date` DATETIME,
    `artist_name` VARCHAR(50),
    PRIMARY KEY (`album_name`, `artist_name`),
    FOREIGN KEY (`artist_name`) REFERENCES artist(`name`)
);

CREATE TABLE song(
    `song_title` VARCHAR(50) NOT NULL,
    `artist_name` VARCHAR(50) NOT NULL,
    `album_title` VARCHAR(50),
    PRIMARY KEY (`song_title`, `artist_name`),
    FOREIGN KEY (`artist_name`) REFERENCES artist(`name`),
    FOREIGN KEY (`album_title`) REFERENCES album(`album_title`)
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
    `album_title` VARCHAR(50) NOT NULL,
    `rating` INT CHECK (rating >= 1 AND rating <= 5), 
    PRIMARY KEY (`username`, `song_title`, `album_title`),
    FOREIGN KEY (`username`) REFERENCES user(`username`),
    FOREIGN KEY (`song_title`) REFERENCES song(`song_title`),
    FOREIGN KEY (`album_title`) REFERENCES album(`album_title`)
);