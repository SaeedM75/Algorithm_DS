# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    fib_array = [0, 1] + (n -1) * [0]
    for i in range(2, len(fib_array)):
        fib_array[i] = fib_array[i - 1] + fib_array[i - 2]
    return fib_array[-1]
    # return calc_fib(n - 1) + calc_fib(n - 2)



n = int(input())
print(calc_fib(n))
