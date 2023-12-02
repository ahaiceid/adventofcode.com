#!/usr/bin/python3
from functools import reduce

def part1(input_data):
    accumulator = 0
    max_counts = {'red': 12, 'green': 13, 'blue': 14}
    for game in input_data:
        game_id, game_reveals = game.split(': ')
        game_id = int(game_id.split()[1])
        valid = True
        for reveal in game_reveals.split('; '):
            for colour_count in reveal.split(','):
                count, colour = colour_count.split()
                if int(count) > max_counts[colour]: valid = False
        if valid:
            accumulator += game_id
    return accumulator

def part2(input_data):
    accumulator = 0
    for game in input_data:
        counts = {'red': 0, 'green': 0, 'blue': 0}
        _, game_reveals = game.split(': ')
        for reveal in game_reveals.split('; '):
            for colour_count in reveal.split(','):
                count, colour = colour_count.split()
                counts[colour] = max(counts[colour], int(count))
        accumulator += reduce((lambda x,y: x*y), counts.values())
    return accumulator

if __name__ == "__main__":
    with open('input') as input_data:
        print(part1(input_data))
    with open('input') as input_data:
        print(part2(input_data))