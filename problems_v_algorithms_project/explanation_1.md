
# Floor Square Root of Number

## Explanation 
The code uses a binary search algorithm to check the square of digits less than the input number to find that number's floor square root.

## Efficiency
Binary search has a time complexity of O(log n) where n is the input number. The algorithm must perfom more iterations for larger input numbers. The number of iterations increase by one when the size of the array (or in this case the range from one to the input number) doubles, which equates to an efficiency of log n. Space complexity is O(1). No matter what which number is used as the input, the algorithm keeps track of the same number of variables.

