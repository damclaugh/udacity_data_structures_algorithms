
# Search in a Rotated Sorted Array

## Explanation
The code uses a binary search algorithm to find the index of the target number in a given array.

## Efficiency
Binary search has a time complexity of O(log n) where n is the size of the array. The algorithm must perfom more iterations for larger arrays. The number of iterations increase by one when the size of the array doubles, which equates to an efficiency of log n. Space complexity is O(1) the algorithm keeps track of the same number of variables no matter the size of the array.