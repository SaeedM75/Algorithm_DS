def binary_search(keys, query):
    # write your code here

    low, high = 0, len(keys) - 1
    while low <= high:
        mid = int((low + high) / 2)
        if keys[mid] == query:
            if mid > 0 and keys[mid - 1] == query:
                high = mid - 1
            else:
                return mid
        if keys[mid] > query:
            high = mid - 1
        if keys[mid] < query:
            low  = mid + 1
    return -1



if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries
    input_keys.sort()
    for q in input_queries:
        # print(input_keys)
        print(binary_search(input_keys, q), end=' ')
