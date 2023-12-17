#!python3

def part1(input_data):
    points = 0
    for line in input_data:
        winning, numbers = line.split(': ')[1].split(' | ')
        winning_set = set((int(x) for x in winning.split()))
        number_set = set((int(x) for x in numbers.split()))
        matches = winning_set.intersection(number_set)
        if matches:
            points += pow(2, len(matches)-1)
    return points

def part2(input_data):
    cards = set()
    card_multiples = dict()
    for line in input_data:
        card = int(line.split(': ')[0].split()[1])
        winning, numbers = line.split(': ')[1].split(' | ')
        winning_set = set((int(x) for x in winning.split()))
        number_set = set((int(x) for x in numbers.split()))
        matches = len(winning_set.intersection(number_set))
        cards.add(card)
        if card not in card_multiples:
            card_multiples[card] = 1
        for i in range(1,matches+1):
            try:
                card_multiples[card+i] = card_multiples[card+i] + card_multiples[card]
            except KeyError:
                card_multiples[card+i] = 1 + card_multiples[card]
    return sum((v for k,v in card_multiples.items() if k in cards))

if __name__ == "__main__":
    with open('input') as input:
        print(part1(input))
    with open('input') as input:
        print(part2(input))