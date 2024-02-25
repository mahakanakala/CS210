# FILL IN ALL THE FUNCTIONS IN THIS TEMPLATE
# MAKE SURE YOU TEST YOUR FUNCTIONS WITH MULTIPLE TEST CASES
# ASIDE FROM THE SAMPLE FILES PROVIDED TO YOU, TEST ON YOUR OWN FILES

# WHEN DONE, SUBMIT THIS FILE TO CANVAS

from collections import defaultdict
from collections import Counter

# YOU MAY NOT CODE ANY OTHER IMPORTS

# ------ TASK 1: READING DATA  --------

# 1.1
def read_ratings_data(f):
    # parameter f: movie ratings file name f (e.g. "movieRatingSample.txt")
    # return: dictionary that maps movie to ratings
    # f = open("./data/movieRatingSample.txt", "r")
    # WRITE YOUR CODE BELOW
    movie_ratings_dict = {}
    with open(f, 'r') as file:
        for line in file:
            parts = line.strip().split("|")
            movie = parts[0]
            rating = parts[1]
            if movie not in movie_ratings_dict:
                movie_ratings_dict[movie] = []
            movie_ratings_dict[movie].append(float(rating))
    return movie_ratings_dict
    

# 1.2
def read_movie_genre(f):
    # parameter f: movies genre file name f (e.g. "genreMovieSample.txt")
    # return: dictionary that maps movie to genre
    # Output: { "Toy Story (1995)" : "Adventure", "Golden Eye (1995)" : "Action" }
    # WRITE YOUR CODE BELOW
    movie_genre_dict = {}
    with open(f, 'r') as file:
        for line in f:
            parts = line.strip().split("|")
            genre = parts[0]
            movie = parts[2]
            if movie not in movie_genre_dict:
                movie_genre_dict[movie] = genre
    return movie_genre_dict


# ------ TASK 2: PROCESSING DATA --------

# 2.1
def create_genre_dict(d):
    # parameter d: dictionary that maps movie to genre
    # return: dictionary that maps genre to movies
    # WRITE YOUR CODE BELOW
    genre_movie_dict = defaultdict(list)
    for movie, genre in d.items():
        genre_movie_dict[genre].append(movie)
    return genre_movie_dict

    
# 2.2
def calculate_average_rating(d):
    # parameter d: dictionary that maps movie to ratings
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    movie_avg_rating_dict = {}
    for movie, ratings in d.items():
        average = sum(ratings)/len(ratings)
        movie_avg_rating_dict[movie] = average
    return movie_avg_rating_dict
    
# ------ TASK 3: RECOMMENDATION --------

# 3.1
def get_popular_movies(d, n=10):
    # parameter d: dictionary that maps movie to average rating
    # parameter n: integer (for top n), default value 10
    # return: dictionary that maps movie to average rating, 
    #         in ranked order from highest to lowest average rating
    # WRITE YOUR CODE BELOW
    top_n_movies_dict = {m: r for m, r in sorted(d.items(), key=lambda item: item[1], reverse=True)}
    return top_n_movies_dict
    
# 3.2
def filter_movies(d, thres_rating=3):
    # parameter d: dictionary that maps movie to average rating
    # parameter thres_rating: threshold rating, default value 3
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    filter_movies_dict = {m: r for m, r in sorted(d.items()) if r >= thres_rating}
    return filter_movies_dict
    
# 3.3
def get_popular_in_genre(genre, genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    movies = genre_to_movies.get(genre, [])
    movies.sort(key=lambda x: movie_to_average_rating.get(x, 0), reverse=True)
    popular_movies_in_genre = {movie: movie_to_average_rating.get(movie, 0) for movie in movies[:n]}
    return popular_movies_in_genre
    
# 3.4
def get_genre_rating(genre, genre_to_movies, movie_to_average_rating):
    # parameter genre: genre name (e.g. "Comedy")
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # return: average rating of movies in genre
    # WRITE YOUR CODE BELOW
    movies = genre_to_movies.get(genre, [])
    ratings = [movie_to_average_rating.get(movie, 0) for movie in movies]
    genre_ratings = sum(ratings) / len(ratings) if ratings else 0
    return genre_ratings
    
# 3.5
def genre_popularity(genre_to_movies, movie_to_average_rating, n=5):
    # parameter genre_to_movies: dictionary that maps genre to movies
    # parameter movie_to_average_rating: dictionary  that maps movie to average rating
    # parameter n: integer (for top n), default value 5
    # return: dictionary that maps genre to average rating
    # WRITE YOUR CODE BELOW
    avg_ratings = {genre: get_genre_rating(genre, genre_to_movies, movie_to_average_rating) for genre in genre_to_movies}
    n_genre_popularity_dict = dict(sorted(avg_ratings.items(), key=lambda item: item[1], reverse=True)[:n])
    return n_genre_popularity_dict

# ------ TASK 4: USER FOCUSED  --------

# 4.1
def read_user_ratings(f):
    # parameter f: movie ratings file name (e.g. "movieRatingSample.txt")
    # return: dictionary that maps user to list of (movie,rating)
    # WRITE YOUR CODE BELOW
    user_ratings_dict = defaultdict(list)
    with open(f, 'r') as file:
        for line in file:
            movie, rating, user_id = line.strip().split('|')
            user_ratings_dict[user_id].append((movie, float(rating)))
            # print(type(user_id))
    return user_ratings_dict
    
# 4.2
def get_user_genre(user_id, user_to_movies, movie_to_genre):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # return: top genre that user likes
    # WRITE YOUR CODE BELOW
    ratings = user_to_movies.get(user_id, [])
    genre_ratings = defaultdict(list)
    for movie, rating in ratings:
        genre = movie_to_genre.get(movie)
        genre_ratings[genre].append(rating)
    average_genre_ratings = {genre: sum(ratings) / len(ratings) for genre, ratings in genre_ratings.items()}
    user_top_genre = max(average_genre_ratings, key=average_genre_ratings.get)
    return user_top_genre
    
# 4.3    
def recommend_movies(user_id, user_to_movies, movie_to_genre, movie_to_average_rating):
    # parameter user_id: user id
    # parameter user_to_movies: dictionary that maps user to movies and ratings
    # parameter movie_to_genre: dictionary that maps movie to genre
    # parameter movie_to_average_rating: dictionary that maps movie to average rating
    # return: dictionary that maps movie to average rating
    # WRITE YOUR CODE BELOW
    user_genre = get_user_genre(user_id, user_to_movies, movie_to_genre)
    movies_in_genre = [movie for movie, genre in movie_to_genre.items() if genre == user_genre]
    movies_in_genre.sort(key=lambda x: movie_to_average_rating.get(x, 0), reverse=True)
    unrated_movies = [movie for movie in movies_in_genre if movie not in dict(user_to_movies.get(user_id, []))]
    recommended_movies_dict = {movie: movie_to_average_rating.get(movie, 0) for movie in unrated_movies[:3]}
    return recommended_movies_dict

# -------- main function for your testing -----
def main():
    # write all your test code here
    # this function will be ignored by us when grading
    read_ratings_data("movieRatingSample.txt")
    movie_to_genre = read_movie_genre("genreMovieSample.txt")
    genre_to_movies = create_genre_dict(movie_to_genre)
    pass
    
# DO NOT write ANY CODE (including variable names) outside of any of the above functions
# In other words, ALL code your write (including variable names) MUST be inside one of
# the above functions
    
# program will start at the following main() function call
# when you execute hw1.py
main()

    