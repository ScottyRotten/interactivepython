# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
import random

def name_to_number(name):
    if name == "rock":
        rock = 0
        return rock
    elif name == "Spock":
        Spock = 1
        return Spock
    elif name == "paper":
        paper = 2
        return paper
    elif name == "lizard":
        lizard = 3
        return lizard
    elif name == "scissors":
        scissors = 4
        return scissors
    else:
        return name


def number_to_name(number):
    if number == 0:
        rock = "rock"
        return rock
    elif number == 1:
        Spock = "Spock"
        return Spock
    elif number == 2:
        paper = "paper"
        return paper
    elif number == 3:
        lizard = "lizard"
        return lizard
    elif number == 4:
        scissors = "scissors"
        return scissors


def rpsls(player_choice):
    print "\n"
    print "Player chooses %s" % player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses %s" % comp_choice
    if (player_number - comp_number) % 5 == 1:
        print "Player wins!"
    if (player_number - comp_number) % 5 == 2:
        print "Player wins!"
    elif (player_number - comp_number) % 5 == 3:
        print "Computer wins!"
    elif (player_number - comp_number) % 5 == 4:
        print "Computer wins!"
    elif player_number == comp_number:
        print "Player and computer tie!"

# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


