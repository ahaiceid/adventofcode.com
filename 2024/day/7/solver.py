from cmath import log10
import itertools
import operator
from tqdm import tqdm

def get_test_value(equation):
    return int(equation.split(':')[0])

def get_numbers(equation):
    return [int(n) for n in equation.strip().split(': ')[1].split(' ')]

def validate_equation(equation, operations):
    test_value = get_test_value(equation)
    numbers = get_numbers(equation)
    operation_combinations = itertools.product(operations,repeat=len(numbers)-1)
    for operation_combination in operation_combinations:
        class ResultTooBig(Exception):
            pass
        acc = numbers[0]
        try:
            for i,op in enumerate(operation_combination,1):
                acc = op(acc,numbers[i])
                if test_value < acc:
                    raise ResultTooBig("")
        except ResultTooBig:
            continue
        if acc == test_value:
            return True
    return False

def part1(input_data, iterations=850):
    total_calibration_result = 0
    for equation in tqdm(input_data, total=iterations):
        if validate_equation(equation, [operator.__mul__, operator.__add__]):
            total_calibration_result += get_test_value(equation)
    return total_calibration_result

def part2(input_data, iterations=850):
    total_calibration_result = 0
    for equation in tqdm(input_data, total=iterations):
        if validate_equation(equation, [operator.__mul__, operator.__add__, combine_numbers]):
            total_calibration_result += get_test_value(equation)
    return total_calibration_result

def combine_numbers(a: int, b: int):
    return int(str(a)+str(b))

if __name__=="__main__":
    with open('input') as fh:
        print(part1(fh))
    with open('input') as fh:
        print(part2(fh))