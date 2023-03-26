# ------------- WAVE 1 --------------------
import json

def create_movie(title, genre, rating):
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
        }
    return None

def add_to_watched(user_data, movie):
     user_data["watched"].append(movie)

     return user_data

def add_to_watchlist(user_data, movie):
    if "watchlist" in user_data.keys():
        user_data["watchlist"].append(movie)
    else:
        user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data, title):
    if user_data["watchlist"]:
        for movie in user_data["watchlist"]:
            if title == movie["title"]:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)
    else:
        user_data["watched"].append(movie)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total = 0.0

    if user_data["watched"]:
        for movie in user_data["watched"]:
            total += movie["rating"]

        return total / len(user_data["watched"])
    
    return 0.0

def get_most_watched_genre(user_data):
    genre_dict = {}
    most_watched_count = 0
    most_watched = None

    for movie in user_data["watched"]:
        genre = movie["genre"]

        if genre in genre_dict:
            genre_dict[genre] += 1 
        else: 
            genre_dict[genre] = 1

    for genre in genre_dict:
        if genre_dict[genre] > most_watched_count:
            most_watched_count = genre_dict[genre]
            most_watched = genre

    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friend_movies_title(user_data):
    friends_movies = []
    
    for friend in user_data["friends"]:
        for watched_movie in friend["watched"]:
            if watched_movie not in friends_movies:
                friends_movies.append(watched_movie)

    return friends_movies

def get_unique_watched(user_data):
   unique = []
   friend_titles = get_friend_movies_title(user_data)

   print(json.dumps(user_data, indent=4))

   for movie in user_data["watched"]:
       if movie not in friend_titles:
           unique.append(movie) 


   print(unique)

   return unique

def get_friends_unique_watched(user_data):
    unique = []
    friends_movies = get_friend_movies_title(user_data)

    for movie in friends_movies:
        if movie not in user_data["watched"]:
            if movie not in unique:
                unique.append(movie)
    
    return unique
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
       recs = []
       friends_movies = get_friend_movies_title(user_data)

       print(json.dumps(user_data, indent=4))

       for movie in friends_movies:
           if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
               if movie not in recs:
                   recs.append(movie)
       return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    recs = []
    friends_movies = get_friend_movies_title(user_data)

    for movie in friends_movies:
           if movie not in user_data["watched"] and movie["genre"] == fav_genre:
               if movie not in recs and movie["genre"] == fav_genre:
                   recs.append(movie)
    return recs
    

def get_rec_from_favorites(user_data):
    friends_movies = get_friend_movies_title(user_data)
    recs = []
    
    for movie in user_data["favorites"]:
        if movie not in friends_movies:
            recs.append(movie)

    return recs