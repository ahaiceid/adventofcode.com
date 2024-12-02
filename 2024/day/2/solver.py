#!python3

def report_is_safe(report):
    if report != sorted(report) and report != sorted(report, reverse=True):
        return False
    v = report[0]
    for v1 in report[1:]:
        if abs(v1-v) not in [1,2,3]:
            return False
        v = v1
    return True

def part1(input_data):
    safe_count = 0
    for report in input_data:
        report = [int(n) for n in report.split()]
        if report_is_safe(report):
            safe_count += 1
    return safe_count

def report_is_safe_with_damping(report):
    rising = None
    failures = 0
    v = report[0]
    for v1 in report[1:]:
        if rising==None:
            rising = v1>v
        if rising:
            if v1-v not in [1,2,3]:
                failures += 1
                continue
        else:
            if v-v1 not in [1,2,3]:
                failures += 1
                continue
        v = v1
    return failures in [0,1]

def report_is_safe_with_damping2(report):
    report_variants = []
    for i in range(len(report)-1):
        report_variants += [report[:i] + report[i+1:]]
    report_variants += [report]
    for r in report_variants:
        if report_is_safe(r):
            return True
    return False

def part2(input_data):
    safe_count = 0
    for report in input_data:
        report = [int(n) for n in report.split()]
        if (report_is_safe_with_damping(report) or 
                report_is_safe(report[1:]) or 
                report_is_safe(report[:-1])):
            safe_count += 1
        elif report_is_safe_with_damping2(report):
            print(report)
            safe_count += 1
    return safe_count

if __name__=="__main__":
    with open("input") as input_data:
        print(part1(input_data))
    with open("input") as input_data:
        print(part2(input_data))
