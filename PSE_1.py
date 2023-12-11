# Imagine working on software that deals with restaurant reviews.
# Create a function named get_highest_rated. This function is responsible
# for finding the highest-rated restaurant.
#
# This function should take in a list of dictionaries named restaurants.
# Each dictionary represents the data associated with a restaurant,
# including its rating. The function should return the restaurant with the
# highest rating.

def get_highest_rated(restaurants):
    if not restaurants:
        return None
    highest_rated_restaurant = restaurants[0]

    for restaurant in restaurants[1:]:
        if restaurant["rating"] > highest_rated_restaurant["rating"]:
            highest_rated_restaurant = restaurant

    return highest_rated_restaurant

# Time Complexity
# The time complexity of this function is O(n), where n is the number of
# restaurants in the restaurants list. This is because the function iterates
# through each restaurant exactly once (starting from the second restaurant,
# as the first one is initially assumed to be the highest rated).

# Space Complexity
# The space complexity of this function is O(1). It uses a fixed amount of
# additional space regardless of the input size: the highest_rated_restaurant
# variable. This variable simply holds a reference to an item in the
# restaurants list, so no extra space proportional to the size of the input
# list is used.

def get_highest_rated(restaurants):
    if not restaurants:
        return None
    
    return max(restaurants, key=lambda x: x["rating"])


# This version does the same thing: it returns the restaurant with the highest
# rating. The max function takes care of the iteration and comparison for you.
# The lambda function lambda x: x["rating"] tells max to compare the
# restaurants based on their "rating" key. The time and space complexities
# remain O(n) and O(1), respectively, but the code is more succinct and easier
# to read.

