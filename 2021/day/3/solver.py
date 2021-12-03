#!/usr/bin/python3

from collections import Counter

def main():

    with open("input") as fh:
        rows = [line.strip() for line in fh.readlines()]
        cols = [''.join(m) for m in map(list,zip(*rows))]
        gamma = ''
        epsilon = ''
        for col in cols:
            counts = Counter(col)
            gamma_ch = max(counts, key=counts.get)
            gamma += gamma_ch
            epsilon += gamma_ch == '0' and '1' or '0'
        print(int(gamma,2) * int(epsilon,2))

    with open("input") as fh:
        rows = [line.strip() for line in fh.readlines()]
        bit_count = len(rows[0])
        o2_candidates = rows
        co2_candidates = rows
        o2_rating = None
        co2_rating = None
        for i in range(bit_count):
            if not o2_rating:
                o2_counts = Counter([''.join(x) for x in map(list,zip(*o2_candidates))][i])
                o2_ch = max(o2_counts, key=o2_counts.get)
                if (o2_ch == min(o2_counts, key=o2_counts.get)):
                    o2_ch = '1'
                o2_candidates = list(filter(lambda x: x[i]==o2_ch, o2_candidates))
                if len(o2_candidates) == 1:
                    o2_rating = o2_candidates[0]
            if not co2_rating:
                co2_counts = Counter([''.join(x) for x in map(list,zip(*co2_candidates))][i])
                co2_ch = min(co2_counts, key=co2_counts.get)
                if co2_ch == max(co2_counts, key=co2_counts.get):
                    co2_ch = '0'
                co2_candidates = list(filter(lambda x: x[i]==co2_ch, co2_candidates))
                if len(co2_candidates) == 1:
                    co2_rating = co2_candidates[0]
            if o2_rating and co2_rating:
                break
        print(int(o2_rating,2) * int(co2_rating,2))


if __name__ == "__main__":
    main()
