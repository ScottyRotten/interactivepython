# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code here

secret_number = 0
counter = 0

# helper function to start and restart the game
def new_game():
    range100()

# define event handlers for control panel
def range100():
    global secret_number
    global counter
    secret_number = random.randint(0, 100)
    counter = 7

def range1000():
    global secret_number 
    global counter
    secret_number = random.randint(0, 1000)
    counter = 10
    return counter

    
def input_guess(guess):
    global counter
    global secret_number
    while counter > 0:
        guess = int(guess)
        print "Guess was", guess
        if guess == secret_number:
            print "Correct"
            break
        elif guess <= secret_number:
            print "Higher"
            counter -= 1
            break
        elif guess >= secret_number:
            print "Lower"
            counter -= 1
            break
        else:
            print "Error! Put in a number"
    else:
        print "You lose!"

    
# create frame

frame = simplegui.create_frame('Guess the Number', 300, 200) 
# register event handlers for control elements and start frame
input = frame.add_input('Enter Guess', input_guess, 50)
button100 = frame.add_button('Range 0-100', range100, 100)
button1000 = frame.add_button('Range 0-1000', range1000, 100) 

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric

