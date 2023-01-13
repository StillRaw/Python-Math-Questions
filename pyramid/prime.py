import math

"""Write a code that verify the number wheter it is prime or not.

                       
                        PRIME NUMBER QUERY
_________________________________________________________________________________
Description: Verifiyng prime number by using the number theory.

                                                          created by Onur Gülşin®
_________________________________________________________________________________"""


def prime_number(number=int):
    """Test whether it is divisible only up to the square root of that number"""
    if number > 2:
        floor_number= math.floor(number**0.5)
        print(floor_number)
        for i in range(2,floor_number):
            if (number % i == 0):
                return False
        else:
            return True
    else:
        return False

print(prime_number(223))