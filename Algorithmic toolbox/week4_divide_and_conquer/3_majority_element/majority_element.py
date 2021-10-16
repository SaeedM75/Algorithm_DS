# Uses python3
import sys


def count_freq(a, left, right, majority):
    count = 0
    for i in a[left: right + 1]:
        if i == majority:
            count += 1
    return count


def get_majority_element(a, left, right):
    if left == right:
        return a[left]

    mid = int((right - left) / 2) + left
    left_majority = get_majority_element(a, left, mid)
    right_majority = get_majority_element(a, mid + 1, right)
    if left_majority == right_majority:
        return left_majority

    if left + 1 == right:
        return a[left]

    left_majority_freq =  count_freq(a, left, right, left_majority)
    right_majority_freq = count_freq(a, left, right, right_majority)

    if left_majority_freq >= right_majority_freq:
        return left_majority
    else:
        return right_majority

    #write your code here


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    major_element = get_majority_element(a, 0, n - 1)
    major_element_count =  count_freq(a, 0, n-1, major_element)

    if major_element_count >= int(len(a)/2) + 1:
        print(1)
    else:
        print(0)


    # if get_majority_element(a, 0, n - 1) != -1:
    #     print(1)
    # else:
    #     print(0)
