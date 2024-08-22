#!/usr/bin/python3
""" Check """


def validUTF8(data):
    """ determines if a given data set represents a valid UTF-8 encoding """
    n_bytes = 0

    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if n_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
