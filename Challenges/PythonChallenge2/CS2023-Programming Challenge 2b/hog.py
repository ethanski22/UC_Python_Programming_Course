"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    "*** REPLACE THIS LINE ***"
    score = 0

    for i in range(num_rolls):
        hold = dice()
        if(hold == 1):
            score = 1
            return score
        else:
            score += dice()

    return score
    # END Question 1

def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    "*** REPLACE THIS LINE ***"
    opponentScoreList = map(int, str(opponent_score))

    if (num_rolls == 0):
        points = max(opponentScoreList) + 1
    else:
        points = roll_dice(num_rolls, dice)

    return points
    # END Question 2

def select_dice(score, opponent_score, four_sided, six_sided):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    "*** REPLACE THIS LINE ***"
    if (score + opponent_score % 7 == 0):
        return four_sided
    else:
        return six_sided
    # END Question 3

def is_swap(score0, score1):
    """Return True if ending a turn with SCORE0 and SCORE1 will result in a
    swap.

    Swaps occur when the last two digits of the first score are the reverse
    of the last two digits of the second score.
    """
    # BEGIN Question 4
    "*** REPLACE THIS LINE ***"
    score0Lst = [int(digit) for digit in str(score0)]
    score1Lst = [int(digit) for digit in str(score1)]
    score0Lst.insert(0, 0)
    score1Lst.insert(0, 0)

    if (score0Lst[-2:] == score1Lst[-2:][::-1]):
        return True
    else:
        return False
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, four_sided, six_sided, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    "*** REPLACE THIS LINE ***"
    

    while(score0 < goal or score1 < goal):
        if (who == 0):
            numDice = strategy0(score0, score1) # returns number of dice to use
            sidedDice = select_dice(score0, score1, four_sided, six_sided)

            score0 += take_turn(numDice, score1, sidedDice)

            who = 1
            if (is_swap(score0, score1)):
                holder = score0
                score0 = score1
                score1 = holder
            if (score0 >= goal or score1 >= goal):
                break
        elif (who == 1):
            strategy1(score0, score1) # returns the number of dice to use
            sidedDice = select_dice(score0, score1, four_sided, six_sided)

            score1 += take_turn(numDice, score0, sidedDice)

            who = 0
            if (is_swap(score0, score1)):
                holder = score0
                score0 = score1
                score1 = holder

    # END Question 5
    return score0, score1


def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy


# four = make_test_dice(1)
# six = make_test_dice(3)
# lst = play(always_roll(5), always_roll(3), four, six, score0 = 98, score1 = 31)
# print(lst)
