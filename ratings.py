"""Restaurant rating lister."""

import sys


def import_file(file_name):
    """Return file object"""

    restaurant_ratings = open(file_name)
   
    return restaurant_ratings

file_name = import_file(sys.argv[1])


def adding_to_restaurants_dict(file_name):
    """Adding restaurant names to dictionary"""

    reviews = {}

    for rating in file_name:
        rating = rating.rstrip()
        name, score = rating.split(":")
        reviews[name] = score

    return reviews

dictionary_reviews = adding_to_restaurants_dict(file_name)


def add_user_restaurant_score(reviews):
    """Returns dictionary with user input"""

    new_restaurant_name = raw_input("Enter a restaurant name: ")
    new_score = raw_input("Enter " + new_restaurant_name + "'s rating: ")

    reviews[new_restaurant_name] = new_score
    return reviews

user_restaurants = add_user_restaurant_score(dictionary_reviews)


def sorting_restaurants(reviews):
    """Prints sorted dictionary"""

    sorted_reviews = sorted(reviews.items())
    for restaurant_name, score in sorted_reviews:
        print "{} is rated at {}".format(restaurant_name, score)


sorting_restaurants(user_restaurants)
