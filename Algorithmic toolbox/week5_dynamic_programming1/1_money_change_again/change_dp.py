# Uses python3
import sys

def get_change(m):
    min_num_coins = [0] * m
    coins = [1, 3, 4]
    for i in range(0, m ):
        min_num_coins[i] = m + 1
        for coin in coins:
            if m >= coin:
                num_coin = min_num_coins[i - coin] + 1
                if num_coin < min_num_coins[i]:
                    min_num_coins[i] = num_coin


    #write your code here


    return min_num_coins[m - 1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
