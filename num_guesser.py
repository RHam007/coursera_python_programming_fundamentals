# Small number guessing game using "random" to generate a 'secret_number' as well as the "guess" number
# - Is possible for the same number to be guessed multiple times

# Importing the random library
import random

# Setting a random number from 1 to 10
secret_number = random.randrange(1,10)

# Validation test - comment out for hidden numbers
print(secret_number)

# Initial guess value
guess = 0

# Looping until the random guess number matches the secret_number
while guess != secret_number:
    guess = random.randrange(1,10)
    print ("Guessing:", guess)

# Ending loop when the two values match
if guess == secret_number:
    print ("Correct! The secret number was:",secret_number,"Are you psychic?!")