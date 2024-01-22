import requests_with_caching
import json
"""for Tastedive
"""
def get_movies_from_tastedive(movie_name):
    parameters = {"q": movie_name, "type": "movies", "limit":5}
    tastedive_response = requests_with_caching.get("https://tastedive.com/api/similar", params = parameters)
    py_data = json.loads(tastedive_response.text)

    return py_data

def extract_movie_titles(movie_dict):
    movie_list = list()
    movie_list = [movies["Name"] for movies in movie_dict["Similar"]["Results"]]
    return movie_list

def get_related_titles(movie_title_list):
    related_titles = list()
    for movie in movie_title_list:
        tastedive_movies = get_movies_from_tastedive(movie)
        extract_movie = extract_movie_titles(tastedive_movies)
        for movie in extract_movie:
            if movie not in related_titles:
                related_titles.append(movie)

    return related_titles

"""for omdbapi
"""
def get_movie_data(movie_name):
    parameters = {"t": movie_name, "r": "json"}
    omdb_response = requests_with_caching.get("http://www.omdbapi.com/", params = parameters)
    py_data = json.loads(omdb_response.text)

    return py_data

def get_movie_rating(omdb_dict):
    for ratings_dict in omdb_dict["Ratings"]:
        if "Rotten Tomatoes" in ratings_dict.values():
            movie_rating = str(ratings_dict["Value"]).replace("%","")
            movie_rating = int(movie_rating)
            break
        else:
            movie_rating = 0
            #break

    return movie_rating

#def sort_tuple(tup):
    #return tup[0]

def get_sorted_recommendations(movie_titles):

    related_movies_list = get_related_titles(movie_titles)

    related_movies_rating_tup = list()

    for movies in related_movies_list:
        rating = get_movie_rating(get_movie_data(movies))
        related_movies_rating_tup.append(rating)

    sorted_movies = sorted(zip( related_movies_rating_tup, related_movies_list),key=lambda tup: -tup[0], reverse = False)

    related_movies_rating= list()
    for movie_tuples in sorted_movies:
        related_movies_rating.append(movie_tuples[1])

    return related_movies_rating

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])
