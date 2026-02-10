def count_digits(n):
    if n == 0:
        return 1
    n = abs(n)
    count = 0
    while n>0:
        count = count+1
        n = n // 10
    return count

# OR

import math

def count_digits_log(n):
    if n == 0:
        return 1
    return int(math.log10(n)) + 1
 

# The count of digits can be calculated using log10 N + 1.
# log10 N operation gives the logarithmic base 10 of which returns the power to which 10 must be raised to, to be equal to N.
# We add 1 to the result which accounts for the possibility that N itself is a power of 10.
# Financially cast the result to an integer to ensure that it is rounded down to the nearest whole number.


# Complexity Analysis-
# Time Complexity: O(1), as simple arithmetic operations in constant time are computed on integers.
# Space Complexity : O(1), as only a constant amount of additional memory for the count variable regardless of size of the input number.