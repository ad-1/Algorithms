# HackerRank - 30 Days of Code (Day 10)

""" Binary Numbers """


def max_consecutive(n):
    current_consecutive = 0
    max_consecutive = 0
    while n > 0:
        remainder = n % 2
        if remainder == 1:
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
        else:
            current_consecutive = 0
        n = n // 2
    print(max_consecutive)

def decimal_to_binary(num):
    if num > 1:
        decimal_to_binary(num // 2)
    print(num % 2, end='')


def count_max_successive_ones(binary_num):
    max_ones, count = 0, 0
    for bit in binary_num:
        if bit == '1':
            count += 1
            if count > max_ones:
                max_ones = count
        else:
            count = 0
    return max_ones


if __name__ == '__main__':
    num = int(input())
    max_consecutive(num)
    # binary_num = bin(num)
    # print(count_max_successive_ones(binary_num))
