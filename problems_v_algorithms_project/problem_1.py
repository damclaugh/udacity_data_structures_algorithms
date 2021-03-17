
def sqrt(number):
    """
    Calculate the floored square root of a number

    """
    if number == 0 or number == 1:
        return number
    
    start = 1
    end = number

    while start <= end:
        mid = (start + end) // 2

        if mid * mid == number:
            return mid

        elif mid * mid <= number:
            start = mid + 1
            root = mid
        else:
            end = mid - 1

    return root

# TEST CASE 1
print(sqrt(9))
# should print 3

# TEST CASE 2
print(sqrt(0))
# should print 0

# TEST CASE 3
print(sqrt(27))
# should print 5

# TEST CASE 4
print(sqrt(99))
# should print 9
