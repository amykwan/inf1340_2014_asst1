""" Assignment 1, Exercise 3, INF1340, Fall, 2014. Rock Paper Scissors game.

This module contains one function decide_rps. It can be passed a parameter
that is a string. All other inputs will result in an error.

Example:
    $ python exercise3.py

"""

__author__ = 'Amy Kwan, Suraj Narayanan, Sue Min'
__email__ = "amykwan.cma@gmail.com, suraj.boss44@gmail.com, ses@drsusansim.org"

__copyright__ = "2014 AKSNSM"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def decide_rps(player1, player2):

    """
    Returns the winner of the rock, paper, scissors game where:
        rock beats scissors
        paper beats rock
        scissors beats paper

    :param:
        player1 (string): player1 inputs/plays rock, paper, or scissors
        player1 (string): player2 inputs/plays rock, paper, or scissors

    :return:
        integer: value is 0, 1, or 2
            0 if tie
            1 if player1 wins
            2 if player2 wins

    :raises:
        TypeError if parameter is not a string
        ValueError if parameter is an invalid input
    """

# if type(player1) is not str (style keep function and (parameter) together with no space

    # define valid inputs
    valid_inputs = ["Rock", "Paper", "Scissors"]

    # check type of input
    # raise TypeError if not string
    if type(player1) is not str or type(player2) is not str:
        print ("error")
        raise TypeError ("Invalid type passed as parameter")
    # check type of input
    # raise ValueError if not a valid input
    if player1 not in valid_inputs or player2 not in valid_inputs:
        print ("error")
        raise ValueError ("Invalid value passes as parameter")

    # define player1 and player2 input combinations (tuple is the dictionary key) and their corresponding results
    rps_dict = {("Rock","Rock"):0, ("Paper","Paper"):0, ("Scissors","Scissors"):0,("Rock","Scissors"):1,
                ("Paper","Rock"):1, ("Scissors","Paper"):1, ("Rock","Paper"):2, ("Paper","Scissors"):2,
                ("Scissors","Rock"):2}

    # create the lookup value
    players_inputs = (player1, player2)

    # return the results of the game
    return rps_dict [players_inputs]
