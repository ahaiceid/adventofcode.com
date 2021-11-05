#!/usr/bin/python3
from sys import maxsize as MAXSIZE

if __name__ == "__main__":
    with open("input") as fh:
        timestamp = int(fh.readline().strip())
        buses = [
            int(bus) for bus in fh.readline().strip().split(',')
            if bus != 'x']
        earliest_bus, minimum_wait = 0, MAXSIZE
        for bus in buses:
            wait = (((timestamp // bus) + 1) * bus) - timestamp
            if wait < minimum_wait:
                minimum_wait = wait
                earliest_bus = bus
        print(minimum_wait * earliest_bus)

    # part 2 is computationally... expensive
    # solving Chinese Remainder Theorem is a pain so I used wolfram alpha:
    # (t + 48) mod 787 = 0,(t + 17) mod 439 = 0,(t + 58) mod 41 = 0,(t + 11) mod 37 = 0,(t + 19) mod 29 = 0,(t + 40) mod 23 = 0,(t + 67) mod 19 = 0,(t + 0) mod 17 = 0,(t + 30) mod 13 = 0
    '''with open("input") as fh:
        fh.readline()
        buses = [
            (i,int(bus))
            for i, bus in enumerate(fh.readline().strip().split(','))
            if bus != 'x']
        buses = sorted(buses, key=lambda x: x[1], reverse=True)
        #i = 1
        i = 100000000000000 // buses[0][1]
        timestamp_found = False
        while(not timestamp_found):
            timestamp = i * buses[0][1] - buses[0][0]
            #print(timestamp, end='\r')
            timestamp_found = True
            for bus in buses[1:]:
                if (timestamp+bus[0])%bus[1] != 0:
                    timestamp_found = False
                    break
            i += 1
        print(timestamp)
    '''