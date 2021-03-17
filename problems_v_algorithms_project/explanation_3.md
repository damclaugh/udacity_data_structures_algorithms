
# Rearrange Array Elements

## Explanation
The code uses a merge sort algorithm to recursively halve the array and then merge the halves to create a new sorted array. It then loops through the array to concatenate digits to form the two biggest numbers, storing them in a list.

## Efficiency
The time efficiency of a merge sort alogorithm is O(nlog n) where n is the number of elements in the array. The process of dividing the array takes place in O(log n) time and the merging process requires O(n) time. The time complexity of the max_numbers function is O(n) because it loops through the entire array. Therefore, the overall time complexity is O(nlog n). Space complexity is O(n), where n is the number of array elements that are stored in a new array as they are sorted. 