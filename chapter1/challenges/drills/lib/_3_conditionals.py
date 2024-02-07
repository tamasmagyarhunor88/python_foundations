# == EXERCISES ==

# Purpose: implements a childhood game
# Rules:   if the number is divisible by 3, return 'fizz'
#          if the number is divisible by 5, return 'buzz'
#          if the number is divisible by 15, return 'fizzbuzz'
#          otherwise, return the number
# Clue: you can check divisibility using modulo (%)
# Example:
#   Call:    fizz_buzz(3)
#   Returns: "fizz"
#   Call:    fizz_buzz(5)
#   Returns: "buzz"
#   Call:    fizz_buzz(15)
#   Returns: "fizzbuzz"
#   Call:    fizz_buzz(8)
#   Returns: 8
def fizz_buzz(number):
    # your code goes here (delete the pass below)
    return "fizzbuzz" if number % 15 == 0 else "fizz" if number % 3 == 0 else "buzz" if number % 5 == 0 else number



# Purpose: responds to the user's greeting
# Rules:   if the greeting is 'good morning'
#          return 'good morning to you too'
#          if the greeting is 'hello'
#          return 'hi'
#          if the greeting is anything else
#          return the greeting that was received
# Example:
#   Call:    reply_to("good morning")
#   Returns: "good morning to you too"
#   Call:    reply_to("hello")
#   Returns: "hi"
#   Call:    reply_to("how are you?")
#   Returns: "how are you?"
def reply_to(greeting):
    # your code goes here (delete the pass below)
    return greeting + " to you too" if greeting == 'good morning' else "hi" if greeting == 'hello' else greeting

# Purpose: deducts 10 from a number if it is greater than or equal to 10,
#          otherwise returns the number
# Example:
#   Call:    deduct_10_if_possible(25)
#   Returns: 15
#   Call:    deduct_10_if_possible(10)
#   Returns: 0
#   Call:    deduct_10_if_possible(9)
#   Returns: 9
def deduct_10_if_possible(number):
    # your code goes here (delete the pass below)
    return number - 10 if number >= 10 else number


# Purpose: if the number is below 100, return 100, otherwise return the number
# Example:
#   Call:    top_up_to_100(25)
#   Returns: 100
#   Call:    top_up_to_100(100)
#   Returns: 100
#   Call:    top_up_to_100(125)
#   Returns: 125
def top_up_to_100(number):
    # your code goes here (delete the pass below)
    return 100 if number < 100 else number


# Congrats, you're done with this file. Move on to the next one.
