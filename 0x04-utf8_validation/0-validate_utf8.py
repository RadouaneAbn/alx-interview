#!/usr/bin/python3
"""
UTF-8 Validator
"""


def validUTF8(data):
    """
    This function validates a dataset of integers representing bytes to check
        if they form valid UTF-8 encoded characters.

    Parameters:
    data (list): A list of integers where each integer represents a byte.

    Returns:
    bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    def count_ones(n):
        """
        This function counts the number of leading 1's in the binary
            representation of a byte.

        Parameters:
        n (int): An integer representing a byte.

        Returns:
        int: The number of leading 1's in the binary representation
            of the byte.
        """
        count = 0
        for i in range(7, -1, -1):
            if n & (1 << i):
                count += 1
            else:
                break
        return count

    count = 0
    for num in data:
        if count == 0:
            count = count_ones(num)
            if count == 0:
                continue
            if count == 1 or count > 4:
                return False
            count -= 1
        else:
            count -= 1
            if count_ones(num) != 1:
                return False
    return count == 0
