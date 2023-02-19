# -*- coding: utf-8 -*-
"""
Author: KESKES Nazim
Version: 1.0.0
Date created: October 28th, 2022
"""

# This function returns the binary value of an integer
def int2bin(m):
    """Returns a list of bits representing the binary decomposition of an integer"""
    tmp = []
    j = m
    # Convert n to binary form using a list
    while j >= 1:
        tmp.append(j % 2)
        j = j // 2
    # Reverse the list
    tmp.reverse()
    return tmp

# This recursive function returns the binary value of an integer
def int2bin_rec(m, tmp):
    """Returns a list of bits representing the binary decomposition of an integer using a recursive implementation"""
    # Convert n to binary form using a list
    if m >= 1:
        # Insert the bit into the list and divide m by 2
        tmp.append(m % 2)
        return int2bin_rec(m // 2, tmp)
    else:
        # Reverse the list
        tmp.reverse()
        return tmp

# Function that performs the inverse operation of the int2bin function
def bin2int(tmp):
    """Function that returns an integer from a list of bits representing its decomposition in base 2"""
    num = 0
    # Iterate through the list
    for i in range(len(tmp)):
        # Add bit i * 2 to the power of i to the result
        num += (tmp[-i-1]) * (2**i)
    # Return the resulting integer
    return num

# Second version of the function that converts a list of bits to an integer
def bin2int_version2(tmp):
    """Function that returns an integer from a list of bits representing its decomposition in base 2. This version uses reversed(tmp)."""
    p = 1
    num = 0
    tmp = list(reversed(tmp))
    # Iterate through the reversed list
    for i in range(len(tmp)):
        # Add bit i * p, which represents the power (multiplied by 2 each time)
        num += tmp[i] * p
        p = p * 2
    # Return the resulting integer
    return num

# Function that returns an integer from a list of bits using the Horner's method
def bin2int_horner(tmp):
    """Function that returns an integer from a list of bits representing its decomposition in base 2 using Horner's method."""
    u = 0
    for i in tmp:
        # Apply the recurrence relation U(k) = b * U(k−1) + a(p−k)
        u = 2 * u + i
    # Return the resulting integer
    return u

# The function that performs the transformation operation from a ca2 representation to an integer
def comp2int(tmp):
    """ Function returns an integer from a list of bits representing the decomposition of its two's complement in base 2.
    """
    # If the integer is positive, return the binary to integer conversion of all bits except the sign bit.
    if tmp[0] == 0:
        return bin2int(tmp[1:])
    else:
        # If the integer is in the form '1000...000', return -2^(n-1) using the binary to integer conversion function.
        if all(i == 0 for i in tmp[1:]):
            return - bin2int(tmp)
        else:
            j = len(tmp) - 1
            # Search for the position where the 0s and 1s start to be inverted.
            while j > 0 and tmp[j] == 0:
                j -= 1
            # Invert the 0s and 1s in the remaining bits.
            for i in range(len(tmp[:j])):
                tmp[i] = 1 - tmp[i]
            return - bin2int(tmp[1:])

# Function that calculates the length of the longest binary gap

def espacemax(num):
    """
    Function espacemax that takes a natural number as argument and returns the length of the longest binary gap present in n if one exists, and 0 otherwise.
    """

    # Convert an integer to a list of bits in its base-2 decomposition
    tmp = int2bin(num)

    # Initialize the maximum length and a counter
    max = 0
    j = 0

    # Loop through the list of bits
    for i in range(len(tmp)):
        # If we find a 1, we have found a binary gap
        if tmp[i] == 1:
            # Check if the length of this binary gap is greater than the current maximum or 0 if there is no previous maximum
            if max < j:
                # Update the new maximum
                max = j
            # Reset the counter for the length of the current binary gap
            j = 0
        else:
            # If we find a 0, increase the length of the current binary gap
            j += 1

    # Return the maximum binary gap length
    return max

# Version 1 of adding 2 integers represented by a list of bits of their base 2 decomposition
def addition(tmp1, tmp2):
    """ 
    This function returns the addition of 2 integers represented by a list of bits of their base 2 decomposition.
    The result will also be represented as a list of bits of the decomposition in base 2.
    """
    # if tmp1 and tmp2 have different lengths
    if len(tmp1) != len(tmp2):
        return None
    else:
        # return the base 10 value of tmp1
        x = bin2int(tmp1)
        # return the base 10 value of tmp2
        y = bin2int(tmp2)
        # construct the list of the base 2 decomposition of the result using the int2bin function
        tmp_res = int2bin((x + y))
        # if the length of the result exceeds the length of one of the two input integers, return None
        if len(tmp_res) != len(tmp1):
            return None
        # return the resulting list
        else:
            return tmp_res

# Version 2 of adding 2 integers represented by a list of bits of their base 2 decomposition
def addition_version_primaire(tmp1, tmp2):
    """ 
    Version 2 (the primary school addition algorithm):
    This function returns the addition of 2 integers represented by a list of bits of their base 2 decomposition.
    The result will also be represented as a list of bits of the decomposition in base 2.
    """
    # if tmp1 and tmp2 have different lengths
    if len(tmp1) != len(tmp2):
        return None
    else:
        e = 0
        tmp_res = []
        # traverse both lists
        for i in range(len(tmp1)):
            # add the remainder e + tmp1[i] + tmp2[i], the result will be the modulo
            # but for the remainder e, if the previous sum exceeds 1, we get a remainder e equal to 1, 
            # so it's the integer division of the previous sum
            tmp_res.insert(0, (e + tmp1[-i-1] + tmp2[-i-1]) % 2)
            e = (e + tmp1[-i - 1] + tmp2[-i - 1]) // 2
        if e != 0:
            tmp_res.insert(0, e)
        # if the length of the result exceeds the length of one of the two input integers, return None
        if len(tmp_res) != len(tmp1):
            return None
        # return the resulting list
        else:
            return tmp_res




def main() -> None:
    """Executes the sequences of the scientific computing activity."""
    # Test the int2bin function
    print(f"iterative version: {int2bin(2985)}")

    # Test the recursive int2bin_rec function
    tmp = []
    print(f"recursive version: {int2bin_rec(2985,tmp)}")

    # Test the bin2int function
    print(f"version 1 : {bin2int([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1])}")

    # Test the bin2int function with the second version
    print(f"version 2 : {bin2int_version2([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1])}")

    # Test the bin2int function with Horner's method
    print(f"version horner : {bin2int_horner([1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1])}")

    # Test the comp2int function.
    print(comp2int([1,0,0,1,0,0,1,0]))
    print(comp2int([0,1,1,0,1,1,0,1]))

    # Test the espacemax function
    print(espacemax(529))
    print(espacemax(32))

    # Test for the addition function when the resulting list is of the same size as the input lists.
    print("Test 1: When the resulting list has the same size as the input lists.")
    print(f"Version 1: {addition([0,1,1,0,1,1,1,0],[0,1,1,1,1,0,0,1])}")
    print(f"Version 2: {addition_version_primaire([0, 1, 1, 0, 1, 1, 1, 0], [0, 1, 1, 1, 1, 0, 0, 1])}")

    # Test for the addition function when the resulting list is of a different size than the input lists.
    print("\nTest 2: When the resulting list has a different size than the input lists.")
    print(f"Version 1: {addition([1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0, 1])}")
    print(f"Version 2: {addition_version_primaire([1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 0, 0, 1])}")

if __name__ == "__main__":
    main()



