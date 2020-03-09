# HackerRank - 30 Days of Code (Day 11)


def hourglass_sum(arr):
    n = len(arr)
    max_sum = n * -9  # determined from constraints - min sum
    for i in range(0, n - 2):
        for j in range(0, n - 2):
            hourglass_sum = get_hourglass_sum(arr, i, j)
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
    return max_sum


def get_hourglass_sum(arr, i, j):
    s = arr[i][j] + \
        arr[i][j + 1] + \
        arr[i][j + 2] + \
        arr[i + 1][j + 1] + \
        arr[i + 2][j] + \
        arr[i + 2][j + 1] + \
        arr[i + 2][j + 2]
    return s


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    max_sum = hourglass_sum(arr)
    print(max_sum)
