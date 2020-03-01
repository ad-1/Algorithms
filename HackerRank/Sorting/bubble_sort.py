"""
HackerRank Sorting

Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {

    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }

}

Given an array of integers, sort the array in ascending order using the Bubble Sort algorithm above.

Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where numSwaps is the number of swaps that took place
irst Element: firstElement, where firstElement is the first element in the sorted array.
Last Element: lastElement, where lastElement is the last element in the sorted array.

Hint: To complete this challenge, you must add a variable that keeps a running tally of all swaps that occur during execution.

"""


def count_swaps(a):
    num_swaps = 0
    for j in range(0, len(a)):
        for i in range(0, len(a) - 1):
            # swap adjacent elements if they are in decreasing order
            if a[i] > a[i + 1]:
                v1 = a[i]
                v2 = a[i + 1]
                a[i] = v2
                a[i + 1] = v1
                num_swaps += 1
    print('Array is sorted in {} swaps.'.format(num_swaps))
    print('First Element: {}'.format(a[0]))
    print('Last Element: {}'.format(a[-1]))
    return


if __name__ == '__main__':
    arr = [6, 4, 1]
    count_swaps(arr)
