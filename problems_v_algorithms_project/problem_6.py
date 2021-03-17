

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    """

    min_val = ints[0]
    max_val = ints[0]

    for i in range(1, len(ints)):
        if ints[i] < min_val:
            min_val = ints[i]
        elif ints[i] > max_val:
            max_val = ints[i]

    tup = (min_val, max_val)
    return tup


# TEST CASE 1
l1 = [9, 10, 1, 5, 7, 6, 2, 19, 12]
print(get_min_max(l1))
# should print (1, 19)

# TEST CASE2 2
l2 = [10, 10, 10]
print(get_min_max(l2))
# should print (10, 10)

# TEST CASE 3
l3 = [-5, 0, 4, 7, -1]
print(get_min_max(l3))
# should print (-5, 7)