"""

Consider an array of integers, we define the absolute difference between
two elements i and j where i is not equal to j.

Given an array of integers, find and print the minimum absolute difference
between any two elements in the array.

"""


def minimum_absolute_difference(arr):
    arr.sort()
    min_dif = abs(arr[0] - arr[1])
    for i in range(1, len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) < min_dif:
            min_dif = abs(arr[i] - arr[i + 1])
            if min_dif == 0:
                break
    return min_dif


if __name__ == '__main__':
    _arr = [3, -7, 0]
    minimum_absolute_difference(_arr)
