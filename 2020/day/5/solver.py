#!/usr/bin/python3
import itertools

BINARY_TRANSLATION = str.maketrans('FBLR','0101')

def decode_seat(code):
    return int(code.translate(BINARY_TRANSLATION),2)

if __name__ == "__main__":
    maximum_seat = 0
    occupied = [False]*pow(2,10)
    last_two = [0,0]
    with open('input') as fh:
        for i, code in enumerate(fh):
            seat_number = decode_seat(code)
            occupied[seat_number] = True
            maximum_seat = max(seat_number,maximum_seat)
    print('last seat: {}'.format(maximum_seat))
    print('first suitable seat: {}'.format(occupied.index(False,occupied.index(True))))