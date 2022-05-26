from datetime import datetime


def binary_search(n, arr):
    low = 0
    high = len(arr) - 1
    counter = 0

    while low <= high:
        counter += 1
        mid = int((low + high) / 2)
        guess = arr[mid]

        if guess == n:
            return mid, counter
        if guess > n:
            high = mid - 1
        else:
            low = mid + 1

    return None


arr = list(range(1, 100000001))
n = int(input())

start_time = datetime.now()

print(binary_search(n, arr))

print(datetime.now() - start_time, ' ms')

