# Subset Sum Problem - Backtracking Algorithm

"""
    Given a set of integers and an integer s,
    is there a non-empty subset whose sum is s?
"""

from timeit import default_timer as timer


def filter_set(arr, s):
    """
        filter set to remove any values less
        than zero and greater than target
    """

    filtered_arr = [i for i in arr if 0 < i < s]
    return filtered_arr


def trivial_case(arr, s):
    """
        check the trivial case that the set has an
        element which is equal to the target value
    """

    if any(i == s for i in arr):
        return True
    return False


def is_target_value(s, curr_sum):
    """
        check if current sum is target value
    """

    if curr_sum == s:
        return True
    return False


def is_set_positive(arr):
    """
        check if set contains all positive integers
    """
    if all(i >= 0 for i in arr):
        return True
    return False


def is_less_than_target_value(s, curr_sum):
    """
        validate that the current sum
        is less than target value
    """

    if curr_sum < s:
        return True
    return True


def solve_subset_sum(arr, s, curr_sum, subset, pos):
    """
        recursive function to solve subset sum problem
    """

    if curr_sum == s:
        return True

    for i in range(pos, len(arr)):
        subset.append(arr[i])
        curr_sum = sum(subset)
        if is_less_than_target_value(s, curr_sum):
            pos += 1
            if solve_subset_sum(arr, s, curr_sum, subset, pos):
                return True

        subset.pop(-1)
        curr_sum = sum(subset)


def subset_sum(arr, s):
    """
        driver method to solve subset sum problem.
        sets initial conditions of recursive method
    """

    if trivial_case(arr, s):
        print('Trivial solution - set contains {}'.format(s))
        return

    if is_set_positive(arr):
        arr = filter_set(arr, s)

    curr_sum, subset, pos = 0, [], 0
    if solve_subset_sum(arr, s, 0, subset, 0):
        print(subset)
    else:
        print('No solution exists')


# Driver program to test above function
if __name__ == '__main__':
    # array, sum_ = [3, 9, 34, 4, 12, 5, 2], 9
    # array, sum_ = [15, 22, 14, 26, 32, 9, 16, 8], 53
    # array, sum_ = [7, 3, 2, 5, 8], 14
    array, sum_ = [267, 493, 869, 961, 1000, 1153, 1246, 1598, 1766, 1922], 5842

    start = timer()
    subset_sum(array, sum_)
    end = timer()
    print('\ncompleted in {} seconds'.format(end - start))
