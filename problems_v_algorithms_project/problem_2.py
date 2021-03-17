
def rotated_array_search(input_list, number):
    """
    Find index of number in rotated array

    """

    low = 0 
    high = len(input_list) - 1
    first = input_list[0]

    while low <= high:
        mid = (low + high) // 2
        mid_value = input_list[mid]
       
        if mid_value == number:
           return mid
        
        elif mid_value >= first and number >= first:
            if mid_value < number:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if mid_value >= first:
                low = mid + 1
            else:
                high = mid - 1
    
    return -1



# TEST CASE 1
l1 =[6, 7, 8, 9, 10, 1, 2, 3, 4]
print(rotated_array_search(l1, 6))
# should print 0

# TEST CASE 2
print(rotated_array_search(l1, 1))
# should print 5

# TEST CASE 3
print(rotated_array_search(l1, 15))
# should print -1

