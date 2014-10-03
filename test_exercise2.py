#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string
    if type(upc) is not str:
        print ("error")
        raise TypeError ("Invalid type passed as parameter")
        # check length of string
    if len(upc) != 12:
        # raise ValueError if not 12
        print("error")
        raise ValueError ("Invalid length of string")

    # convert string to array
    # hint: use the list function

    upc_digits = []
    #upc_digits = upc[0]
    #upc_digits.append(upc[1]) #type this out 11 times if don't know loop
    #cannot be used b/c can only add two lists together (two values that have same type, here we have list + str + str, etc) upc_digits = upc_digits + upc[1] + upc[2]+ upc[3]+ upc[4]+ upc[5]+ upc[6]+ upc[7]+ upc[8]+ upc[9]+ upc[10]

    for i in range (0,11):
        upc_digits.append(int(upc[i]))

    # generate checksum using the first 11 digits provided
    verify_upc = (sum(upc_digits[::2])*3 + sum(upc_digits[1::2])) % 10
    if verify_upc > 0:
        verified_upc = 10 - verify_upc
    else:
        verified_upc = verify_upc

    # check against the the twelfth digit
    if int(upc [-1]) == verified_upc:
        return True
    # return True if they are equal, False otherwise
    else:
        return False

