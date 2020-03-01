# # A recursive function to find nth catalan number
# def catalan(n):
#     # Base Case
#     if n <=1 :
#         return 1
#
#     # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
#     res = 0
#     for i in range(n):
#         res += catalan(i) * catalan(n-i-1)
#
#     return res
#
# # Driver Program to test above function
# for i in range(500):
#     print(catalan(i))
# # This code is contributed by Nikhil Kumar Singh (nickzuck_007)


from timeit import default_timer as timer

# A dynamic programming based function to find nth
# Catalan number
def catalan(n):
    if (n == 0 or n == 1):
        return 1

    # Table to store results of subproblems
    catalan = [0 for i in range(n + 1)]

    # Initialize first two values in table
    catalan[0] = 1
    catalan[1] = 1

    # Fill entries in catalan[] using recursive formula
    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

        # Return last entry
    return catalan[n]


# Driver code
start = timer()
cats = []
for i in range(500):
    cats.append(catalan(i))
end = timer()
print(cats[-1])
print('\n', end - start, 'seconds')
# This code is contributed by Aditi Sharma

