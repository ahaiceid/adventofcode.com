
part1_scores = {
    "A X": 4,   # 1 + 3
    "A Y": 8,   # 2 + 6
    "A Z": 3,   # 3 + 0
    "B X": 1,   # 1 + 0
    "B Y": 5,   # 2 + 3
    "B Z": 9,   # 3 + 6
    "C X": 7,   # 1 + 6
    "C Y": 2,   # 2 + 0
    "C Z": 6,   # 3 + 3
}

part2_scores = {
    "A X": 3,   # 3 + 0
    "A Y": 4,   # 1 + 3
    "A Z": 8,   # 2 + 6
    "B X": 1,   # 1 + 0
    "B Y": 5,   # 2 + 3
    "B Z": 9,   # 3 + 6
    "C X": 2,   # 2 + 0
    "C Y": 6,   # 3 + 3
    "C Z": 7,   # 1 + 6
}


def score_games(input_data, scoring_strategy):
    return sum([scoring_strategy[game.strip()] for game in input_data])

def part1(input_data):
    return score_games(input_data, part1_scores)

def part2(input_data):
    return score_games(input_data, part2_scores)

if __name__ == "__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))