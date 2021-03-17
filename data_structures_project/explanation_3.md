
# Huffman Coding

## Data Structures
The code relies on several different data structures. A dictionary stores all the characters and their frequencies. The dictionary is then used to build a tree that consists of nodes for each character and the character's frequency. The build_tree function uses a Python heap structure, which is a priority queue. I chose the heap structure because its pop method provides easy access to letters with the smallest frequencies, which are needed to build the tree. I then used recursion to traverse the tree to collect the codes for each letter, which are stored in a dictionary. The program then loops over the original string and for each letter, gets the corresonding code from the dictionary. For decoding, the program walks "down" the branches of the tree based on whether the digit is a 0 or 1 until it reaches a leaf, at which point it gets that letter.

## Efficiency
The time complexity for the code is 0(nlog n) because of the use of the Python heap structure used to build the tree. The heap pop and push methods have time complexity of O(log n), and there are n characters.[^1] Since those methods are the most time-consuming elements of the code, the overall time complexity is O(nlog n). Space complexity is O(n) where n in the number of characters in the string to be decoded. The call stack created by the recursion function in the traverse_tree method also has space complexity of O(n) because the stack increases linearly with the depth of the tree.[^2]


[^1]: See: https://stackoverflow.com/questions/38806202/whats-the-time-complexity-of-functions-in-heapq-library#:~:text=heapq%20is%20a%20binary%20heap,O(n%20log%20n).

[^2]: See: https://www.interviewcake.com/concept/java/call-stack