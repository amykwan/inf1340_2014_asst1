""" Module to test exercise2.py """

__author__ = 'Amy Kwan, Suraj Narayanan, Sue Min'
__email__ = "amykwan.cma@gmail.com, suraj.boss44@gmail.com, ses@drsusansim.org"

__copyright__ = "2014 AKSNSM"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import pytest
from exercise2 import checksum

def test_checksum():
    """
    Inputs that are the correct format and length
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("123456789999") is True
    assert checksum("717951000841") is False
    assert checksum("123412341234") is False

    # other tests
def test_input_type():
    """
    Inputs that are the incorrect format and length
    """
    with pytest.raises(TypeError):
        checksum(1.0)
    with pytest.raises(TypeError):
        checksum(786936224306)

def test_input_value():
    with pytest.raises(ValueError):
        checksum("1")
    with pytest.raises(ValueError):
        checksum("1234567890")
    with pytest.raises(ValueError):
        checksum("123456789012345")

# add functions for any other tests
def test_non_numeric_input():
    with pytest.raises(ValueError):
        checksum("asdfasdfasdf")
    with pytest.raises(ValueError):
        checksum("12345abcde12")