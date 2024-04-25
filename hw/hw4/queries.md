Queries (50 points)
Every query must be written in a single SQL statement, meaning that if you were to write it in a MySQL client session on a terminal, there would be a single terminating semicolon. So, for example, you can have nested or multiple SQLs for a query, provided you can write it all up with a single terminating semicolon in a MySQL client session. No Python code!

For any of the queries:

If the result might require breaking ties, then unless otherwise specified in the query, let the MySQL engine deal with it (you need not do anything explicit)
If the result has fewer than the required number of entities, report all of them.
For all queries that ask for 'top n' or 'most', the result must appear from highest ranked to lowest ranked.
Type the SQL queries in the document you will submit, and make sure to write the query number against each query. (If you want to play it extra safe, copy the query statement from this list, then write your answer SQL query.)

Write queries for the following.

---

Which 3 genres are most represented in terms of number of songs in that genre?
The result must have two columns, named genre and number_of_songs.

Find names of artists who have songs that are in albums as well as outside of albums (singles).
The result must have one column, named artist_name

What were the top 10 most highly rated albums (highest average user rating) in the period 1990-1999? Break ties using alphabetical order of album names. (Period refers to the rating date, NOT the date of release).
The result must have two columns, named album_name and average_user_rating.

Which were the top 3 most rated genres (this is the number of ratings of songs in genres, not the actual rating scores) in the years 1991-1995? (Years refers to the rating date, NOT the date of release).
The result must have two columns, named genre_name and number_of_song_ratings.

Which users have a playlist that has an average song rating of 4.0 or more? (This is the average of the average song rating for each song in the playlist.) A user may appear multiple times in the result if more than one of their playlists make the cut.
The result must 3 columns named username, playlist_title, average_song_rating

Who are the top 5 most engaged users in terms of number of ratings that they have given to songs or albums? (In other words, they have given the most number of ratings to songs or albums combined.)
The result must have 2 columns, named username and number_of_ratings.

Find the top 10 most prolific artists (most number of songs) in the years 1990-2010? Count each song in an album individually.
The result must have 2 columns, named artist_name and number_of_songs.

Find the top 10 songs that are in most number of playlists. Break ties in alphabetical order of song titles.
The result must have a 2 columns, named song_title and number_of_playlists.

Find the top 20 most rated singles (songs that are not part of an album). Most rated meaning number of ratings, not actual rating scores. The result must have 3 columns, named song_title, artist_name, number_of_ratings.
Find all artists who discontinued making music after 1993.
The result should be a single column named artist_title


