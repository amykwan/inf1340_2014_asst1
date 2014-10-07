""" Module to test exercise2.py """

__author__ = 'Amy Kwan, Suraj Narayanan'
__email__ = "amykwan.cma@gmail.com, suraj.boss44@gmail.com"

__copyright__ = "2014 AKSN"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
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

def test_input():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        decide_rps(1, 2)
    with pytest.raises(TypeError):
        decide_rps(1, "Paper")

    # other tests
    with pytest.raises(ValueError):
        decide_rps("Spark", "Lizard")
    with pytest.raises(ValueError):
        decide_rps("Pen", "Fish")