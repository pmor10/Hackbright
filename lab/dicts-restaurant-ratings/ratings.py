"""Restaurant rating lister."""


# put your code here
#make a function
def ratings_dictionary(filename):
    """

    """

    # get the file
    data = open(filename)

    # create an empty dict.
    restaurant_ratings = {}
    
    # loop through the file lines
    for line in data:
        # each line as a string of resturant name split from rating 
        line = line.rstrip().split(":")
        # add the resturant name as the key and rating as the value to the dict.
        restaurant_ratings[line[0]] = int(line[1])

    return restaurant_ratings

#create a new function that alphabetizes the keys into a list
def sorted_ratings(filename):
    """
    docstring
    """
    restaurant_ratings = ratings_dictionary(filename)

    # iterates through the list to call the value
    for restaurant, rating in sorted(restaurant_ratings.items()):
        print(f'{restaurant} is rated at {rating}.')

#create our print statement 
sorted_ratings('scores.txt')

