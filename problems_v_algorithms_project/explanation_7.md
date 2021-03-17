
# HTTP Router

## Explanation
The code uses a trie to create a URL path. A trie is a tree-like structure that is built around a dictionary. Each node in this case holds one part of the http path that is separated by a '/'. Looking up the paths returns a handler message or None if there is no handler.

## Efficiency
The time complexity of the insert method in the RouteTrie class is O(n), where n is the number of elements in the path. The path 'home/about/me' has three elements, for example. Insertion requires looping over each element to check whether an element already exists. Similarly, the find method is also O(n) time complexity. The add_handler and lookup methods are also O(n) because they rely on the insert and find methods respectively. The time complexity of the split_path method is O(n) as well because it loops over the path elements to add them as individual elements to a list. Because the split_path method adds the elements to a list, the overall space complexity is O(n)
