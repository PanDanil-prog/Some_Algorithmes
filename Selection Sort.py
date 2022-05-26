from datetime import datetime
import random


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


my_list = [random.randint(1, 1000) for _ in range(10000)]

start_time = datetime.now()
selection_sort(my_list)
print(datetime.now() - start_time)




