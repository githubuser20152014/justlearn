# Guessing Game
# Exercise 9 
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, print this out.


import random

guess_count = 0
play_again = ""
correct_guess = 0

while (play_again != "exit"):

  ask_user = int(input('Guess a number between 1 and 9: '))

  num_generate = random.randint(1,9)

  if ask_user == num_generate:
    print('Your guess was correct \n')
    guess_count += 1
    correct_guess += 1
  else:
    print('Wrong guess, I had {} in mind \n'.format(num_generate))
    guess_count += 1

  play_again = input('Hit enter to try again or type "exit" to quit')


print('Total guesses: {}, correct guesses: {}'.format(guess_count, correct_guess))
