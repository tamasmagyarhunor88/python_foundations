from urllib.request import urlopen
import json
# == INSTRUCTIONS ==
#
# Below, you'll find lots of incomplete functions.
#
# Your job: Implement each function so that it does its job effectively.
#
# * Use the material, Python Docs and Google as much as you want

# == EXERCISES ==

# Purpose: Use Python libraries to request the provided URL, convert the
#          response data to JSON, and return the data.
# Example:
#   Call:    load_data_from_url("https://example.org/my.json")
#   Returns: A JSON object
def load_data_from_url(url):
    request = urlopen(url)
    response = request.read().decode('UTF-8')
    json_data = json.loads(response)
    return json_data

# Purpose: Use Python libraries to open the specified file, convert the
#          data to JSON, and return the data.
# Example:
#   Call:    load_data_from_file("my_test_data.json")
#   Returns: A JSON object
def load_data_from_file(filename):
    file = open(f"{filename}")
    json_data = json.load(file)
    return json_data

# Purpose: Load the sample JSON from file, and returns a list of films 
#           directed by the named person.
# Example:
#   Call:    get_films_by_director("my_test_data.json", "Olivia Wilde")
#   Returns: ["Booksmart, "Don't Worry Darling"]
def get_films_by_director(filename, director):
    json_data = load_data_from_file(filename)
    # json_str = json.dumps(json_data, indent=4)
    # print(json_str)
    filtered_list = list(filter(lambda item: item['director'] == director, json_data))
    movies = []
    for dictionary in filtered_list:
        movies.append(dictionary['name'])
    return movies

    # return list(set(item['name'] for item in json_data if item.get('director') == director))




# Purpose: Load the sample JSON from file, and returns a list of films 
#           starring the named person.
# Example:
#   Call:    get_films_by_actor("my_test_data.json", "Dwayne Johnson")
#   Returns: ["Jumanji", "Jungle Cruise"]
def get_films_by_actor(filename, desired_actor):
    json_data = load_data_from_file(filename)
    filtered_list = [item for item in json_data if desired_actor in item.get('stars', [])]
    movies = []
    for dictionary in filtered_list:
        movies.append(dictionary['name'])
    return movies

# Purpose: Load the sample JSON from file, and returns a list of films 
#           with a rating which is AT LEAST the value specified.
# Example:
#   Call:    get_films_with_minimum_rating("test.json", 9.3)
#   Returns: ["The Shawshank Redemption"]
def get_films_with_minimum_rating(filename, rating):
    json_data = load_data_from_file(filename)
    filtered_list =  list(filter(lambda item: item['imdb_rating'] >= rating, json_data))
    movies = []
    for dictionary in filtered_list:
        movies.append(dictionary['name'])
    return movies

# Purpose: Load the sample JSON from file, and returns a list of films 
#           which were released during the specified years.
# Example:
#   Call:    get_films_within_year_range("my_test_data.json", 1994, 1996)
#   Returns: ["The Lion King", "Independence Day"]
def get_films_within_year_range(filename, start_year, end_year):
    json_data = load_data_from_file(filename)
    filtered_list =  list(filter(lambda item: item['year'] >= start_year and item['year'] <= end_year, json_data))
    movies = []
    for dictionary in filtered_list:
        movies.append(dictionary['name'])
    return movies

# Purpose: Load the sample JSON from file, and returns a list of films 
#           in order of the year that they were released.
# Example:
#   Call:    order_films_chronologically("test.json")
#   Returns: ["12 Angry Men", "The Godfather", "The Godfather: Part II", ... ]
def order_films_chronologically(filename):
    json_data = load_data_from_file(filename)
    sorted_list = sorted(json_data, key = lambda item: item['year'])
    movies = []
    for dictionary in sorted_list:
        movies.append(dictionary['name'])
    return movies

# Purpose: Load the sample JSON from file, and returns a list of films 
#           starting with the most recent.
# Example:
#   Call:    order_films_most_recent_first("test.json")
#   Returns: ["The Dark Knight", "The Shawshank Redemption", "The Godfather: Part II", ... ]
def order_films_most_recent_first(filename):
    json_data = load_data_from_file(filename)
    sorted_list = sorted(json_data, key = lambda item: item['year'], reverse=True)
    movies = []
    for dictionary in sorted_list:
        movies.append(dictionary['name'])
    return movies

# Purpose: Load the sample JSON from file, and returns a deduplicated list 
#           of all the actors whose name begins with that letter,
#           in alphabetical order.
# Example:
#   Call:    all_actors_starting_with_letter("test.json", "a")
#   Returns: ["Aaron Eckhart, "Al Pacino"]
def all_actors_starting_with_letter(filename, letter):
    json_data = load_data_from_file(filename)
    filtered_list = [item for item in json_data if any(actor.startswith(letter.upper()) for actor in item.get('stars', []))]
    actors_set = set()
    for dictionary in filtered_list:
        for star in dictionary.get('stars', []):
            if star[0].lower() == letter.lower():
                actors_set.add(star)
    return list(actors_set)