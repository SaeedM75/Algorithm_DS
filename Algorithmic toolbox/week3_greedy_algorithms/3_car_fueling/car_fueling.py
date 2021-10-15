# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    r = 0
    i = 0
    d = 0
    while i < len(stops) :
        if (stops[i] - d) < tank:
            if i + 1 < len(stops):
                if (stops[i + 1] - d) < tank:
                    i += 1
                else:
                    d = stops[i]
                    i += 1
                    r += 1
            else:
                d = stops[i]
                i += 1
                r += 1
        else:
            return -1

    return r

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
