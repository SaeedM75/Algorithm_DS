# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    '''
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % 10
    '''

    if (n <= 1):
        return n
    fib_array = [0, 1] + (n -1) * [0]
    for i in range(2, len(fib_array)):
        fib_array[i] = (fib_array[i - 1] + fib_array[i - 2]) % 10
    return fib_array[-1]


# n = int(input())
# print(get_fibonacci_last_digit_naive(n))

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
