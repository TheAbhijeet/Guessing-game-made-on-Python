import random
number = random.randint(1, 10)
print("Hello, What's your name?")
player_name = input()
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')
while number_of_guesses < 5:
    guess = input()
    guess = int(guess)
    number_of_guesses = number_of_guesses + 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))
