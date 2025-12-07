

def joltage(bank: str) -> str:
    max_u = max(bank[:-1])
    u = bank.index(max_u)
    max_v = max(bank[u+1:])
    v = bank[u+1:].index(max_v)
    joltage = max_u + max_v
    return joltage

def joltage_twelve(bank: str, rem=12) -> str:
    if rem == 1:
        return max(bank)
    max_u = max(bank[:1-rem])
    u = bank.index(max_u)
    return max_u + joltage_twelve(bank[u+1:], rem-1)

def total_joltage(banks, joltage_func) -> int:
    acc = 0
    count = 0
    for bank in banks:
        bank_joltage = joltage_func(bank.strip())
        acc += int(bank_joltage)
        count += 1
    return acc

if __name__ == "__main__":
    with open('input') as data:
        print(total_joltage(data, joltage))
    with open('input') as data:
        print(total_joltage(data, joltage_twelve))
