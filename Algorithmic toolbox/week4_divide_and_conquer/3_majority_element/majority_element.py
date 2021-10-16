# Uses python3
import sys

def get_majority_element(a, left, right):

    if len(a) == 1:
        return 1
    mid = int(len(a ) / 2)

    if a[left] == a[mid ]:
        return 1
    else:
        return -1

    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    #


    #write your code here


    # return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    a.sort()
    if get_majority_element(a, 0, n - 1) != -1:
        print(1)
    else:
        print(0)
