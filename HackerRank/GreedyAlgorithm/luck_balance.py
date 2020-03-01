"""

Lena is preparing for an important coding competition that is preceded by a number of
sequential preliminary contests. Initially, her luck balance is 0.

She believes in "saving luck", and wants to check her theory.
Each contest is described by two integers L(i) and T(i)

L(i) is the amount of luck associated with a contest.
If Lena wins the contest, her luck balance will decrease by L(i) or if she loses it,
her luck balance will increase by L(i)

T(i) denotes the contest's importance rating.
It's equal to 1 if the contest is important, and it's equal to 0 if it's unimportant.

If Lena loses no more than k important contests, what is the maximum amount of
luck she can have after competing in all the preliminary contests?
This value may be negative.

k: the number of important contests Lena can lose
a 2D array of integers where each contents[i] contains two integers that
represent the luck balance and importance of the i contest.

Print a single integer denoting the maximum amount of luck Lena can have after all the contests.

"""


def luck_balance(k, contests):
    luck = 0
    lost = 0
    contests.sort(key=lambda a: a[0], reverse=True)
    for val in contests:
        if val[1] == 0:
            luck += val[0]
        elif val[1] == 1 and lost < k:
            luck += val[0]
            lost += 1
        else:
            luck -= val[0]
    return luck


if __name__ == '__main__':
    _k = 3
    _arr = [(5, 1), (2, 1), (1, 1), (8, 1), (10, 0), (5, 0)]
    luck_balance(_k, _arr)  # 29
