# Move all zeroes to end of array

"""
Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
"""


def push_zeros_to_end(arr, n):
    count = 0  # Count of non-zero elements
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < n:
        arr[count] = 0
        count += 1


arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9]
n = len(arr)
push_zeros_to_end(arr, n)
print("Array after pushing all zeros to end of array:")
print(arr)
