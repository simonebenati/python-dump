#This is a guess the number game.

import random

print("Hello sir, what is your name?")
name = input()

while name.isalpha() == False:
    print("A name cannot contain any number! Please type it again:")
    name = input()

print("Nice to meet you " + name + ", Now try to guess the number I've been thinking about")

number = random.randint(1,10)

tentatives = 0

while tentatives < 6:
    guess = input()

    if guess == str(number):
        print("Congratulations, you guessed it right, my number was: " + str(number))
        exit()
    elif tentatives == 5 and guess != str(number):
        print("Sorry, you tried too many times, better luck next time!")
        exit()
    else:
        if int(guess) > number:
            print("Not the right number, it's too high, Try again!")
        elif int(guess) < number:
            print("Not the right number, it's too low, Try again!")
        tentatives = tentatives + 1


