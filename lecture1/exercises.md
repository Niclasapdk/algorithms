# Algorithms 1 - exercises

## Exercise 1 - insertion sort

a. Consider the application of insertion sort on an integer array with n ($n \ge 4$) elements.
Create at least 8 instances of this array (including the sorted and reverse sorted instances)
and calculate the running time for each instance. Make a bar chart of the estimated
running times indicating the best and worst cases.

```python
>>> for i in range(6): [random.randint(0,9) for i in range(4)]
...
[1, 9, 4, 8]
[9, 2, 4, 1]
[1, 5, 7, 8]
[1, 5, 6, 5]
[9, 3, 8, 7]
[7, 8, 4, 0]
>>> def runtime(ar, comparisons):
...     n = len(ar)
...     return n + 3*(n-1) + comparisons + 2 * (comparisons - (n-1))
>>> r = [runtime(ar, c) for (ar, c) in zip(a, comparisons)]
>>> for i in r:
...     print(i)
...
16
22
25
16
19
19
25
25
```

| Input          | Comparisons | Running time |
|----------------|-------------|--------------|
| `[1, 2, 3, 4]` | 3           | 16           |
| `[1, 5, 7, 8]` | 3           | 16           |
| `[1, 5, 6, 5]` | 4           | 19           |
| `[9, 3, 8, 7]` | 4           | 19           |
| `[1, 9, 4, 8]` | 5           | 22           |
| `[4, 3, 2, 1]` | 6           | 25           |
| `[7, 8, 4, 0]` | 6           | 25           |
| `[9, 2, 4, 1]` | 6           | 25           |

b. Prove insertionsort pseudocode correctness

```pseudocode
function insertionSort(arr):
    for i from 1 to length(arr):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key
```

Loop Invariant for the Outer Loop (for i from 1 to length(arr)):
At the start of each iteration of the outer loop, the subarray arr[0..i-1] is sorted in non-decreasing order.

Loop Invariant for the Inner Loop (while j >= 0 and arr[j] > key):
At the start of each iteration of the inner loop, key holds the value that was originally at arr[i]. The elements arr[j+1], arr[j+2], ..., arr[i-1] are greater than key, and the elements arr[0], arr[1], ..., arr[j] are less than or equal to key.

Now, let's prove these loop invariants:

Initialization:

    At the beginning of the algorithm, i is 1, and the subarray arr[0..i-1] contains only one element, which is trivially sorted.
    The inner loop is not executed because j is initialized as i - 1, which is 0 in this case, and the condition j >= 0 is not met.

Maintenance:

    Assume that the loop invariants hold at the start of an iteration of the outer loop (for i from 1 to length(arr)).
    In the inner loop, we move elements greater than key to the right (shifting them up one position) until we find the correct position for key. This preserves the sorted order of arr[0..i-1].
    After the inner loop completes, arr[j+1] is set to key, which places key in the correct position in the sorted subarray.

Termination:

    When the outer loop completes (i.e., i becomes length(arr)), the subarray arr[0..i-1] is sorted in non-decreasing order, as per the loop invariant.
    The entire array arr is now sorted because the outer loop has iterated through all elements.

c. Implement the insertion sort algorithm and ensure to time its execution

ii. Plot the averaged running time estimate as a function of the size of the input
array, n. You are to generate arrays of random integers of the appropriate size for
the tests.

```python
import time
import matplotlib.pyplot as plt

def insertionsort(ar):
    for i in range(1, len(ar)):
        key = ar[i]
        j = i - 1
        while j >= 0 and ar[j] > key:
            ar[j+1] = ar[j]
            j -= 1
        ar[j+1] = key
    return ar

def time_execution(ar):
    t0 = time.time()
    insertionsort(ar)
    t1 = time.time()
    return t1-t0

SIZE_MAX = 20000
inputs = [[[random.randint(0, 30) for _ in range(i)] for _ in range(5)] for i in range(SIZE_MAX)]
ns = [i for i in range(SIZE_MAX)]
exec_times = [[time_execution(inputs[size][idx]) for idx in range(5)] for size in range(SIZE_MAX)]
plt.plot(ns, exec_times)
plt.show()
```
