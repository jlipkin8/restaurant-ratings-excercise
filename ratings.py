"""Restaurant rating lister."""

import sys

restaurant_ratings = sys.argv[1]
restaurant_ratings = open(restaurant_ratings)

reviews = {}

for rating in restaurant_ratings:
    rating = rating.rstrip()
    name, score = rating.split(":")
    reviews[name] = score

new_restaurant_name = raw_input("Enter a restaurant name: ")
new_score = raw_input("Enter " + new_restaurant_name + "'s rating: ")

reviews[new_restaurant_name] = new_score

sorted_reviews = sorted(reviews.items())
for restaurant_name, score in sorted_reviews:
    print "{} is rated at {}".format(restaurant_name, score)

restaurant_ratings.close()
