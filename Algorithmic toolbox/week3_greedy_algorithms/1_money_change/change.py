# Uses python3
import sys

def get_change(m):
    #write your code here
    coin_list = [1, 5, 10]
    coin_count = 0
    coin_ind = 2
    while (m > 0):
        if m >= coin_list[coin_ind]:
            coin_count += 1
            m -= coin_list[coin_ind]
        else:
            coin_ind -= 1

    return coin_count


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
