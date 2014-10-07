""" Assignment 1, Exercise 2, INF1340, Fall, 2014. Perform a checksum on a UPC.

This module contains one function checksum. It can be passed a parameter
that is a 12-digit string. All other inputs will result in an error.

Example:
    $ python exercise2.py

"""

__author__ = 'Amy Kwan, Suraj Narayanan, Sue Min'
__email__ = "amykwan.cma@gmail.com, suraj.boss44@gmail.com, ses@drsusansim.org"

__copyright__ = "2014 AKSNSM"
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
    check_length = len(upc) - 12
    if check_length < 0:
        print ("Error - length short by " + str(abs(check_length)))
        raise ValueError ("Invalid length")
    elif check_length > 0:
        print ("Error - length over by " + str(abs(check_length)))
        raise ValueError ("Invalid length")
    # convert string to array
    # hint: use the list function

    upc_first11digits = []

    for i in range (0,11):
        # append only if character is a number
        if upc[i].isdigit():
            upc_first11digits.append(int(upc[i]))
        else:
            print(upc + " is not an integer")
            raise ValueError ("Invalid character")

    # generate checksum using the first 11 digits provided
    verify_upc = (sum(upc_first11digits[::2])*3 + sum(upc_first11digits[1::2])) % 10
    if verify_upc > 0:
        verified_upc = 10 - verify_upc
    else:
        verified_upc = verify_upc

    # check against the the twelfth digit
    # return True if they are equal, False otherwise
    if int(upc [-1]) == verified_upc:
        return True
    else:
        return False