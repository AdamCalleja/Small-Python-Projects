import random

def divisors_of_number(target_number): 
    for integer

def start_game(lower_bound, upper_bound): 
    target_number = random.randint(lower_bound, upper_bound, game_mode)
    target_found = False
    while target_found == False: 
        number_guess = input("Try to guess the number between ", lower_bound, " and ", upper_bound, ": ")
        if int(number_guess) == target_number: 
            target_found = True
        elif number_guess < target_number: 
            number_comparisson = "low"
        elif number_guess > target_number: 
            number_comparisson = "high"
        elif game_mode = "easy": 
            print("Incorrect")
            print("Your guess was too ", number_comparisson)
            