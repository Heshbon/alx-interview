#!/usr/bin/python3
""" Python method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding"""
    num_bytes = 0

    for byte in data:
        if byte > 255:
            byte = byte & 0xFF
        # The start byte of the utf-8 character
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7) == 0:
                continue
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1
    # if trailing bytes are left in the data set, it's invalid
    return num_bytes == 0
