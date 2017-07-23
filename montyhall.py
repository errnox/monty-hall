import sys
from random import randrange

from visualizer import visualize


# Algorithm
#
# 1. Set car_door
# 2. Set choice
# 3. Set alternative_door
#   3.1. Exclude choice
#   3.2. Exclude car_door
# (4. Reset choice)
# 4./5. Compare choice and car_door


CHOICE_RANGE = [1, 2, 3]
PROMPT_SYMBOL = '>'
YES_NO_ANSWERS = ['y', 'n']

class WrongStringException(Exception):
    def __init__(self, value):
        self.parameter = value

    def __str__(self):
        return 'Wrong string: ' + repr(self.parameter)

def place_car(car, doors):
    car_door = randrange(CHOICE_RANGE[0], CHOICE_RANGE[-1] + 1)
    doors[car_door] = car
    return car_door

def ask_for_door(interactive):
    choice = 0
    choice_string = '0'
    if interactive:
        while choice_string not in [str(i) for i in CHOICE_RANGE]:
            choice_string = raw_input('Your choice:\n%s ' % PROMPT_SYMBOL).strip()
        choice = int(choice_string)
        sys.stdout.write("You chose door %s." % choice)
    else:
        choice = int(randrange(1, 4))
    return choice

def offer_door_switching(doors, goat, switch, choice, interactive):
    alternative_door = 0
    do_switch = ''
    for door in doors.items():
        if  door[0] != choice and door[1] == goat:
            alternative_door = door[0]
    if interactive:
        while do_switch not in YES_NO_ANSWERS:
            do_switch = raw_input(" Do you want to switch to door %s? [y/n]\n%s " %
                                  (alternative_door, PROMPT_SYMBOL)).strip()
    else:
        if switch:
            if switch == 'yes':
                do_switch = 'y'
            elif switch == 'no':
                do_switch = 'n'
            else:
                raise WrongStringException(switch)
        else:
            do_switch = YES_NO_ANSWERS[randrange(0, 2)]
    return alternative_door

def check_for_victory(car_door, choice, interactive):
    user_wins = False
    if choice == car_door:
        user_wins = True
    if interactive:
        if user_wins:
            print('You win!')
        else:
            print('You loose.')
    return user_wins

def monty_hall(switch=None, interactive=True):
    # Setup
    goat = 0
    car = 1
    doors = {1: goat, 2: goat, 3: goat}

    # Place car behind a door
    car_door = place_car(car, doors)

    # Ask player for a door
    choice = ask_for_door(interactive)
    
    # Offer door switching to user
    alternative_door = offer_door_switching(doors, goat, switch,choice,
                                            interactive)
        # Check for victory and return statutus
    return check_for_victory(car_door, choice, interactive)
    

if __name__ == '__main__':
    # Tests
    def test_iteration(iterations, summary=True, total=True):
        n_runs = iterations
        wins = 0
        losses = 0
        for i in range(n_runs):
            if monty_hall(interactive=False, switch='yes'):
                wins += 1
            else:
                losses += 1

        if summary:
            print("%s iterations" % n_runs)
            print("Wins  : %s" % wins)
            print("Losses: %s" % losses)

        if total:
            if wins > losses:
                print 'WIN'
            elif losses > wins:
                print 'LOSS'
            else:
                print '===='

        return (wins, losses)


    def test_visualization():
        wins_and_losses = []
        for i in range(100):
            wins_and_losses.append(test_iteration(iterations=3000,
                                                  summary=False, total=False))
        wins_data = [(idx, num[0]) for idx,num in enumerate(wins_and_losses)]
        losses_data = [(idx, num[1]) for idx,num in enumerate(wins_and_losses)]

        visualize(wins_data, losses_data)

    # test_iteration(3000, summary=True, total=True)
    test_visualization()



    # --------------------------------------------------------------------


    # DEBUG
    # test_iteration(iterations=3000, summary=True, total=True)


    # Test: Params
    # print [monty_hall(switch='yes', interactive=False) for i in range(10)]


    # DEBUG
    # [monty_hall(switch='yes', interactive=True) for i in range(50)]
