def avg_rating(reviews):
    movie_rating={}
    for review in reviews:
        movie=review["movie"]
        rating=review["rating"]

        if movie not in movie_rating:
            movie_rating[movie]=[]
        
        movie_rating[movie].append(rating)

    
    for movie, rating in movie_rating.items():
        movie_rating[movie] = sum(rating)/len(rating)
    
    return movie_rating

def high_rated(a):
    for movie,rating in a.items():
        
        if rating == max(a.values()):
            top_movie=movie
    return top_movie

def must_watch(a):
    must_watchh=[]
    for movie,rating in a.items():
        if rating>=8.5:
            must_watchh.append(movie)
    return must_watchh

def user_favs(reviews):
    user_favourite={}
    for review in reviews:
        user=review["user"]
        rating=review["rating"]
        movie=review["movie"]
        if user not in user_favourite:
            user_favourite[user]=(movie,rating)
        else:
            if rating > user_favourite[user][1]:
                user_favourite[user]=(movie,rating)
    a={}
    for movie,items in user_favourite.items():
        a[movie]=items[0]
    return a
    
def main():
    reviews= [
  {"movie": "Inception",  "user": "alice", "rating": 9},
  {"movie": "Dune",       "user": "bob",   "rating": 8},
  {"movie": "Inception",  "user": "bob",   "rating": 7},
  {"movie": "Interstellar","user":"alice",  "rating": 10},
  {"movie": "Dune",       "user": "charlie","rating": 9},
  {"movie": "Interstellar","user":"charlie","rating": 8},
  ]
    movie_rating = avg_rating(reviews=reviews)
    top_movie = high_rated(movie_rating)
    must_watchh = must_watch(movie_rating)
    user_fav = user_favs(reviews)

    print("avg_rating:",movie_rating)
    
    print("top_movie:",top_movie)

    print("must_watch",must_watchh)

    print("user_favs",user_fav)


if __name__=="__main__":
    main()