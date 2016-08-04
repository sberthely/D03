#!/usr/bin/env python
# HW03_ex06
# (1) Please comment your code.
# (2) Please be thoughtful when naming your variables.
# (3) Please remove development code before submitting.
###############################################################################
# Exercise 6.2
# See 6.1: "write a compare function takes two values, x and y, and returns 1
# if x > y, 0 if x == y, and -1 if x < y."
# When you submit only include your final function: compare

def compare(x, y):
    if x > y:           #if x is greater than y
        return 1
    elif x == y:        #if x equals y
        return 0
    else:               #otherwise
        return -1




###############################################################################
# Exercise 6.2
# See 6.2: "use incremental development to write a function called hypotenuse
# that returns the length of the hypotenuse of a right triangle given the
# lengths of the other two legs as arguments."
# When you submit only include your final function: hypotenuse
# Do develop incrementally. Do not share in your final push your incremental
# work.

import math
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)


###############################################################################
# Exercise 6.4
# See 6.4: "write a function is_between(x, y, z) that returns True if x ≤ y ≤ z
# or False otherwise"
# When you submit only include your final function: is_between

def is_between(x, y, z):
    return x <= y <= z



###############################################################################
# Exercise 3.2
# See "Exercise 3, part 2": "Write a function called is_palindrome that takes a
# string argument and returns True if it is a palindrome and False otherwise.
# Remember that you can use the built-in function len to check the length of a
# string."
# When you submit only include your final function: is_palindrome

def is_palindrome(s):    
    s = str.lower(s)
    
    if len(s) == 0:
        return 'Must enter a string'
    if len(s) == 1:
        return False
    if len(s) == 2:
        if s[0] == s[-1]:
            return True
        else:
            return False

    if s[0] == s[-1]:
        new_s = s[1:len(s)-1]
        if len(new_s) ==1:
            return True
        else:
            is_palindrome(new_s)
    else:
        return False

    return True


###############################################################################
# Exercise 4
# See "Exercise 4": "A number, a, is a power of b if it is divisible by b and
# a/b is a power of b. Write a function called is_power that takes parameters a
# and b and returns True if a is a power of b. Note: you will have to think
# about the base case."
# Note: Please use the provided definition and only plan for positive integers
# (whole numbers not including zero)
# When you submit only include your final function: is_power

def is_power(a, b):
    if b > a:
        return False
    elif a % b != 0:
        return False
    else:
        new_a = a / b
        if new_a == b:
            return True
        return(is_power(new_a, b))


###############################################################################
def main():
    """Your functions will be called within this function."""
    ###########################################################################
    # Use this space temporarily to call functions in development:
    print("Hello World!")
    
    # x = int(input("Value of x\n"))
    # y = int(input("Value of y\n"))
    # print("Returned value: " + str(compare(x, y)))

    # a = int(input("Value of a\n"))
    # b = int(input("Value of b\n"))
    # print("Hypotenuse: " + str(hypotenuse(a, b)))

    # x = int(input("Value of x\n"))
    # y = int(input("Value of y\n"))
    # z = int(input("Value of z\n"))
    # print(is_between(x, y, z))

    # s = input("Write a palindrome\n")
    # print(is_palindrome(s))

    # a = int(input("Value of a\n"))
    # b = int(input("Value of b\n"))
    # print(is_power(a, b))


    ###########################################################################
    # # Uncomment the below to test and before commiting:
    # # Exercise 1
    print(compare(1, 1))
    print(compare(1, 2))
    print(compare(2, 1))
    # # Exercise 2
    print(hypotenuse(1, 1))
    print(hypotenuse(3, 4))
    print(hypotenuse(1.2, 12))
    # # Exercise 3
    print(is_between(1, 2, 3))
    print(is_between(2, 1, 3))
    print(is_between(3, 1, 2))
    print(is_between(1, 1, 2))
    # # Exercise 6
    print(is_palindrome("Python"))
    print(is_palindrome("evitative"))
    print(is_palindrome("sememes"))
    print(is_palindrome("oooooooooooo"))
    # # Exercise 7
    print(is_power(28, 3))
    print(is_power(27, 3))
    print(is_power(248832, 12))
    print(is_power(248844, 12))


if __name__ == "__main__":
    main()
