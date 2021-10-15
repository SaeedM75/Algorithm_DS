# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    w = 0
    vtw = []
    for i in range(len(values)):
        vtw.append(values[i]/weights[i])

    values = vtw
    indexes = list(range(len(values)))
    indexes.sort(key=lambda i:values[i], reverse= True)
    values.sort(reverse= True)
    index = 0
    while w < capacity:
        add_w = min(weights[indexes[index]], capacity - w)
        value += add_w * values[index]
        index += 1
        w += add_w

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
