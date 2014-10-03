#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps ("Paper", "Rock") == 1
    assert decide_rps ("Paper", "Paper") == 0
    assert decide_rps ("Paper", "Scissors") == 2
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Scissors") == 0

    # other tests
    #assert decide_rps("Paper", "Pen") == "Invalid Input"
    #assert decide_rps(1, "Paper") == "Invalid Input"

def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        decide_rps(1, 2)
        decide_rps(1, "Paper")

    with pytest.raises(ValueError):
        decide_rps("Spark", "Lizard")
        decide_rps("Pen", "Fish")

    # other tests

# add functions for any other tests