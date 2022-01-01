import random
import math

def divisors_of_number(target_number): 
    factors_of_target = []
    root_target_number = math.sqrt(target_number)
    divisor_upper_limit = math.floor(root_target_number + 1) 
    for potential_divisor in range(0, divisor_upper_limit):
        if target_number % potential_divisor == 0: 
            factors_of_target.append(potential_divisor)
    return factors_of_target

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
            