
# Autocomplete With Tries

## Explanation
The code uses a trie to create an auto-complete function for strings. A trie is a tree-like structure that is built around a dictionary.

## Efficiency
The time complexity is O(n*w). Inserting a word and finding prefixes and suffixes depends on the number of characters in the word or string (n) and the number of words in the trie (w). Space complexity is O(n), where n is the number of nodes.