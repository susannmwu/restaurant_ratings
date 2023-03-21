"""Restaurant rating lister."""


def get_restaurant_ratings(file):

    file = open("scores.txt")
    restaurant_dict = {}


    for line in file:
        line = line.split(":")
    # access each line in file by indexing
        restaurant_name = line[0]
        restaurant_score = line[1]

        restaurant_dict[restaurant_name] = restaurant_score

    return sorted(restaura#dictionary -> .items -> sorted

    for restaurant_name in restaurant_dict:

        print(f'{restaurant_name} is rated at {restaurant_score}')
        
get_restaurant_ratings("scores.txt")

# def get_new_ratings(parameter):

#     restaurant_name = input("What is the name of the restaurant?")
#     restaurant_score = input("What is the restaurant score? ")

