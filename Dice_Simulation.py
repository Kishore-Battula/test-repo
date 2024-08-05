""" Simulating  the dice game Craps."""
import random

def roll_dice():
    """ Roll two dice and return their face values as a tuple."""
    die1= random.randrange(1,7)
    die2= random.randrange(1,7)

    return (die1, die2) # pack die face values in to a tuple.

def display_dice(dice):
    """Display one roll of the two dice."""
    die1,die2 = dice
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

die_values = roll_dice()
display_dice(die_values)

#determine the gmae status and point, based on the first roll

sum_of_dice = sum(die_values)

if(sum_of_dice) in (7,11):
    game_status = 'WON'
elif sum_of_dice in (2,3,12):
    game_status =  'LOST'
else:
    game_status = 'CONTINUE'
    my_point = sum_of_dice
    print('Point is ',my_point)

#continue rolling until the player wins or looses.
while game_status == 'CONTINUE':
    die_values= roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)

    if sum_of_dice == my_point:
        game_status = 'WON'
    elif sum_of_dice == 7:
        game_status= 'LOST'

#display win or loose message
if game_status == 'WON':
    print('Player wins')
else:
    print('Player looses')

