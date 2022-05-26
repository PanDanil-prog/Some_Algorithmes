import random
from datetime import datetime


def qsort(arr):
    if len(arr) < 2:
        return arr
    else:
        sup_el = arr[0]

        less = [i for i in arr[1:] if i <= sup_el]
        greater = [i for i in arr[1:] if i > sup_el]

        return qsort(less) + [sup_el] + qsort(greater)


array = [random.randint(1, 1000) for _ in range(100000)]
start_time = datetime.now()
qsort(array)
print(datetime.now() - start_time, ' ms for MY qsort()')

array = [random.randint(1, 1000) for _ in range(100000)]
start_time = datetime.now()
array.sort()
print(datetime.now() - start_time, ' ms for .sort()')

array = [random.randint(1, 1000) for _ in range(100000)]
start_time = datetime.now()
arr = sorted(array)
print(datetime.now() - start_time, ' ms for sorted()')
