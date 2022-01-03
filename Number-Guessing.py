# Below i am importing the libraries that I will use in this program. 
import random
import math

# The following function will randomly choose an integer between a given range and ask the user to select their desired difficulty. ]
def game_setup():
    lower_bound = int(input("Please enter the lower bound of the number range: "))
    upper_bound = int(input("Please enter the upper bound of the number range: "))
    target_number = random.randint(lower_bound, upper_bound)
    game_mode = input("Please select a game mode (easy, normal, hard): ").lower
    return lower_bound, upper_bound, target_number, game_mode

# The function below finds and returns all of the factors of a given 'target_number'.
def divisors_of_number(target_number): 
    factors_of_target = []
    root_target_number = math.sqrt(target_number)
    divisor_upper_limit = math.floor(root_target_number + 1) 
    for potential_divisor in range(0, divisor_upper_limit):
        if target_number % potential_divisor == 0: 
            known_divisor = target_number / potential_divisor
            factors_of_target.append(potential_divisor)
            factors_of_target.append(known_divisor)
    if len(factors_of_target) == 2: 
        target_prime = True
    else:
        target_prime = False
    return factors_of_target, target_prime

# The function below creates a dictionary containing all of the hints that can be given to the player. 
def define_hints():
    lower_bound, upper_bound, target_number, game_mode = game_setup()
    hint_dict = {

    }
    factors_of_target, target_prime = divisors_of_number(target_number) 
    if target_prime == True: 
        hint_dict["1"] = "The number is prime."
    else: 
        hint_dict["1"] = "The number is not prime."
    index = 1
    for factor in factors_of_target: 
        hint = str(factor) + " is a factor of the target number"
        hint_dict[str(index)] = hint
        hint += 1

# The function below will generate a random hint for the user.
def get_hint():
    print

# The function below will ask the user to guess the target number and give the user feedback which depends on the game mode they have chosen. 
# The following game modes will be possible: 'easy', 'normal', 'hard'.
# In the 'easy' game mode the game will automatically give a hint if the guess is incorrect. 
# In the 'normal' game mode the game will ask the user if they want a hint. 
# In the 'hard' game mode the user won't get any hints. 
def guess_target(lower_bound, upper_bound, game_mode, target_number): 
    target_found = False
    number_guess = input("Try to guess the number between ", lower_bound, " and ", upper_bound, ": ")
    if int(number_guess) == target_number: 
        target_found = True
    elif number_guess < target_number: 
        number_comparisson = "low"
    elif number_guess > target_number: 
        number_comparisson = "high"
    if game_mode == "easy": 
        print("Incorrect")
        print("Your guess was too ", number_comparisson)     

def main(): 
    lower_bound, upper_bound, target_number, game_mode = game_setup()
    
