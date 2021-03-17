

class TrieNode:
    def __init__(self):
        # initialize node
        self.children = {}
        self.is_end = False
    
    def insert(self, char):
        # add child node
        self.children[char] = TrieNode()

    def suffixes(self, suffix=''):
        # collects suffix for complete words below this point
        suffixes = []
        for char, node in self.children.items():
            if node.is_end:
                suffixes.append(suffix + char)
            if node.children:
                suffixes += node.suffixes(suffix + char)
        return suffixes

class Trie:
    def __init__(self):
        # initialize trie
        self.root = TrieNode() 

    def insert(self, word):
        # add word to trie
        node = self.root

        for char in word:
            # if char not there, add it
            if char not in node.children:
                node.insert(char)
            # move to the next node
            node = node.children[char]
        
        node.is_end = True

    def find_prefix(self, prefix):
        # find the trie node that represents the prefix
        node = self.root
        for char in prefix:
            # if char in node, move to next node
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node



MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym", 
    "fun", "function", "factory", 
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

# TEST CASE 1
print(MyTrie.find_prefix("an").suffixes())
# should print ['t', 'thology', 'tagonist', 'tonym']

# TEST CASE 2
print(MyTrie.find_prefix('f').suffixes())
# should print ['un', 'unction', 'actory']

# TEST CASE 3
print(MyTrie.find_prefix("").suffixes())
# should print ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function',
# 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']

# TEST CASE 4
print(MyTrie.find_prefix("X"))
# should print None

# TEST CASE 5
print(MyTrie.find_prefix("tripod").suffixes())
# should print []