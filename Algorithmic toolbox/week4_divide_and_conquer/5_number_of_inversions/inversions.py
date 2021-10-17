# Uses python3
import sys




def merge(a, b, left, right, mid):
    inv_count = 0
    i = left
    j = mid + 1
    k = left
    while i <= mid and j <= right:
        if a[i] <= a[j]:
            b[k] = a[i]
            i += 1
            k += 1
        else:
            inv_count += mid - i + 1
            b[k] = a[j]
            j += 1
            k += 1

    while i <= mid:
        b[k] = a[i]
        i += 1
        k += 1
    while j <= right:
        b[k] = a[j]
        j += 1
        k += 1

    for ind in range(left, i + 1):
        a[ind] = b[ind]

    return inv_count




def get_number_of_inversions(a, b, left, right):


    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge(a, b, left, right, ave)
    #write your code here
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a) - 1))
