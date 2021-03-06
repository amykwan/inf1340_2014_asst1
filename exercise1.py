""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion.

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__author__ = 'Amy Kwan, Suraj Narayanan, Sue Min'
__email__ = "amykwan.cma@gmail.com, suraj.boss44@gmail.com, ses@drsusansim.org"

__copyright__ = "2014 AKSNSM"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    if type(grade) is str:
        # print ("letter") # remove this line once the code is implemented
        # check that the grade is one of the accepted values
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" \
                or grade == "B" or grade == "B-" or grade == "FZ":
            # assign grade to letter_grade
            letter_grade = grade
        else:
            print ("error")
            raise ValueError ("Invalid value passed as parameter")

    elif type(grade) is int:
        # print("mark") # remove this line once the code is implemented
        # check that grade is in the accepted range
        if grade >= 0 and grade <= 100:
            # convert the numeric grade to a letter grade
                # assign the value to letter_grade
                # hint: letter_grade = mark_to_letter(grade)
            if grade >= 90:
                letter_grade = "A+"
            elif grade >= 85:
                letter_grade = "A"
            elif grade >= 80:
                letter_grade = "A-"
            elif grade >= 77:
                letter_grade = "B+"
            elif grade >= 73:
                letter_grade = "B"
            elif grade >= 70:
                letter_grade = "B-"
            elif grade >= 0:
                letter_grade = "FZ"
        else:
            print ("error")
            raise ValueError ("Grade out of range")

    else:
        # raise a TypeError exception
        print ("error")
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+" or letter_grade == "A":
        gpa = 4.0
    elif letter_grade == "A-":
        gpa = 3.7
    elif letter_grade == "B+":
        gpa = 3.3
    elif letter_grade == "B":
        gpa = 3.0
    elif letter_grade == "B-":
        gpa = 2.7
    elif letter_grade == "FZ":
        gpa = 0.0
    return gpa