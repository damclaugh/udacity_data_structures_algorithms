
def sort_012(a):
    """
    Given an array consisting of only 0, 1, and 2, sort the array in a single traversal

    """
    low = 0
    mid = 0
    high = len(a) - 1

    while mid <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[high] = a[high], a[mid]
            high -= 1
    return a


# TEST CASE 1
l1 = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
print(sort_012(l1))
# should print [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]

# TEST CASE 2
l2 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print(sort_012(l2))
# should print [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

# TEST CASE 3
l3 = [0]
print(sort_012(l3))
# should print [0]
