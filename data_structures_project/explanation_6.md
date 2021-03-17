
# Union and Intersection

## Data Structures
The code creates linked lists that are then used to compare the two groups of elements. Two sets are built from the lists and combined to form either a union or an intersection. A new linked list is then created from the combination.


## Efficiency
The time complexity of building the initial sets is O(n).[^1] For combining the two sets, complexity is O(2n). Finally, building the new linked list is O(n).[^2] So the overall time complexity is O(n). Space complexity is O(n), where n is the total size of the two linked lists.

[^1]: See: https://wiki.python.org/moin/TimeComplexity

[^2]: See: https://www.bigocheatsheet.com/
