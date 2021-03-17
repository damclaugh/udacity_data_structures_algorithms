

def rearrange_digits(input_list):
    """
    Divide list into arrays of single elements

    """

    # if length of list == 1, it's sorted
    if len(input_list) <= 1:
        return input_list

    # divide list into into single arrays
    mid = len(input_list) // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = rearrange_digits(left)
    right = rearrange_digits(right)

    # merge two halves
    return merge(left, right)

def merge(left, right):
    """
    Combine elements of input_list into sorted list of descending order

    """

    merged = []
    left_index = 0
    right_index = 0

    # move through the lists until one is exhausted
    while left_index < len(left) and right_index < len(right):
        # if left's item is larger, append left's item
        # and increment the index
        if left[left_index] > right[right_index]:
           merged.append(left[left_index])
           left_index += 1
        # otherwise append right's item and increment
        else:
            merged.append(right[right_index])
            right_index += 1

    # append leftovers which are already sorted
    merged += left[left_index:]
    merged += right[right_index:]

    return merged

def max_numbers(sorted_list):
    """
    Combine digits of sorted list to create two biggest numbers

    """

    result = []
    num1 = 0
    num2 = 0

    for i in range(0, len(sorted_list), 2):
        num1 = num1*10 + sorted_list[i]
    result.append(num1)
    
    for i in range(1, len(sorted_list), 2):
        num2 = num2*10 + sorted_list[i]
    result.append(num2)

    return result
        

# TEST CASE 1
l1 = [8, 3, 1, 7, 0, 10, 2]
sorted_list = rearrange_digits(l1)
print(sorted_list)
# should print [10, 8, 7, 3, 2, 1, 0]
print(max_numbers(sorted_list))
# should print [10720, 831]

# TEST CASE 2
l2 = [4, 6, 2, 5, 9, 8]
sorted_list = rearrange_digits(l2)
print(sorted_list)
# should print [9, 8, 6, 5, 4, 2]
print(max_numbers(sorted_list))
# should print [964, 852]

# TEST CASE 3
l3 = [5]
sorted_list = rearrange_digits(l3)
print(sorted_list)
# should print [5]
print(max_numbers(sorted_list))
# should print [5, 0]