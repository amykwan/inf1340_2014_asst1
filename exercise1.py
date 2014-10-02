""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    Grade_to_GPA (90)
    4.0
    Grade_to_GPA (80)
    3.7
    Grade_to_GPA (FZ)
    0.0
"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line

def mark_to_letter (percentage):
    """
   Return letter grade associated with the given integer mark

    :param:
        percentage (integer): Grade to be converted
            Accepted values are 0-100.

    :return:
        strong: The equivalent letter grade
            Possible values are A+, A, A-, B+, B, B-, FZ

    """
    if percentage >= 90:
        temp_letter = "A+"
    elif percentage >= 85:
        temp_letter = "A"
    elif percentage >= 80:
        temp_letter = "A-"
    elif percentage >= 77:
        temp_letter = "B+"
    elif percentage >= 73:
        temp_letter = "B"
    elif percentage >= 70:
        temp_letter = "B-"
    elif percentage >= 0:
        temp_letter = "FZ"
    return(temp_letter)

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
        print ("letter") # remove this line once the code is implemented
        # check that the grade is one of the accepted values
        # assign grade to letter_grade
        if grade == "A+" or grade == "A" or grade == "A-" or grade == "B+" or grade == "B" or grade == "B-" or grade == "FZ":
            letter_grade = grade
    elif type(grade) is int:
        print("mark") # remove this line once the code is implemented
        # check that grade is in the accepted range
        if grade >= 0 and grade <= 100:
            # convert the numeric grade to a letter grade
            # assign the value to letter_grade
            # hint: letter_grade = mark_to_letter(grade)
            letter_grade = mark_to_letter(grade)
        else:
            raise ValueError("Grade out of range")
    else:
        # raise a TypeError exception
        #print ("error")
        raise TypeError("Invalid type passed as parameter")

    # write a long if-statement to convert letter_grade
    # assign the value to gpa
    if letter_grade == "A+":
        gpa = 4.0
    elif letter_grade == "A":
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

print(grade_to_gpa(77))

