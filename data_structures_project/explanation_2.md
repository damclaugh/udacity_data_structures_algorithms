
# File Recursion

## Data Structures
The code uses a list to store the name files that end in ".c". Since the number of directories and subdirectories is unknown, I used recursion to go through each level to reach the files.

## Efficiency
The time complexity depends on the number of directories and files that need to be searched. The time increases linearly with the number of directories and files, so time complexity is O(n). Space complexity is O(n) where n is the number of files with the required extension. In addition, the function's recursive call creates a call stack that has its own space requirement that is also O(n), where n is the depth of the directory. [^1]

[^1]: See: https://www.interviewcake.com/concept/java/call-stack and https://stackoverflow.com/questions/61255507/time-and-space-complexity-of-a-file-recursion-algorithm

