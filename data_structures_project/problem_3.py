
import heapq
import sys

class HuffmanNode():
    def __init__(self, freq, char=None, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    # compares letter frequencies to order nodes correctly
    def __lt__(self, other):
        return self.freq < other.freq

    # checks for end of tree
    def is_leaf(self):
        return (self.left == None and self.right == None)
    
    def __repr__(self):
        return "HuffmanNode(char=%s, freq=%s)" % (self.char, self.freq)


# get frequency count of letters in string
def char_freq(string):
    char_freq = {}
    for char in string:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    return char_freq


def build_tree(char_freq):
    # create nodes from frequency counts and add them to nodes list
    nodes = []
    for char in char_freq:
        nodes.append(HuffmanNode(char_freq[char], char))
    # transform nodes list to priority queue
    heapq.heapify(nodes)
    # get nodes with two smallest frequencies; combine them; repeat until all nodes combined
    while (len(nodes) > 1): 
        child1 = heapq.heappop(nodes)
        child2 = heapq.heappop(nodes)
        parent = HuffmanNode(child1.freq + child2.freq, left=child1, right=child2)
        heapq.heappush(nodes, parent)
    return None if nodes == [] else heapq.heappop(nodes)


def traverse_tree(node, code=''):
    # dictionary to hold code for each letter
    codes = {}
    if node is None:
        return
    # # walk down tree and add 0 to code for left branch, 1 for right branch
    # # add code once lead is reached
    if node.is_leaf():
        codes[node.char] = code
        return codes
    codes.update(traverse_tree(node.left, code + '0'))
    codes.update(traverse_tree(node.right, code + '1'))
    return codes


def coded_str(codes_dict, string):
    # loop over string and get each letter's code
    coded_str = ""
    for char in string:
        coded_str += codes_dict[char]
    return coded_str


def huffman_encoding(string):
    # check for empty string
    if not string:
        return "", None
    
    frequencies = char_freq(string)
    root = build_tree(frequencies)
    codes = traverse_tree(root)
    code = coded_str(codes, string)

    # if string is one letter or same letter repeated
    if len(frequencies) == 1:
        code = "0"*len(string)
    
    return code, root


def huffman_decoding(coded_str, tree):
    # when there's only one character or the same character repeated
    if len(char_freq(coded_str)) == 1:
        return len(coded_str)*str(tree.char)
    
    decoded_str = ""

    if coded_str == "":
        return decoded_str

    # traverse tree one branch at a time until leaf
    # go left for 0; right for 1
    curr_node = tree
    for char in coded_str:
        if (char == "0"):
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
        if (curr_node.is_leaf()):
            decoded_str += curr_node.char
            curr_node = tree # start again from top of tree
    return decoded_str



# TEST CASE 1    
a_great_sentence = "The bird is the word"
print("The content of the data is: {}\n".format(a_great_sentence))
# The content of the data is: The bird is the word
print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
# The size of the data is: 69    
    
encoded_data, tree = huffman_encoding(a_great_sentence)
print("The content of the encoded data is: {}\n".format(encoded_data))
# The content of the encoded data is: 1110111111101010001100110000101100101101101011111101010000111001100001
print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
# The size of the encoded data is: 36

decoded_data = huffman_decoding(encoded_data, tree)
print("The content of the decoded data is: {}\n".format(decoded_data))
# The content of the decoded data is: The bird is the word
print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# The size of the decoded data is: 69

# TEST CASE 2
empty_sentence = ""
print("The content of the data is: {}\n".format(empty_sentence))
# The content of the data is:
encoded_data, tree = huffman_encoding(empty_sentence)
print("The content of the encoded data is: {}\n".format(encoded_data))
# The content of the encoded data is:
decoded_data = huffman_decoding(encoded_data, tree)
print("The content of the decoded data is: {}\n".format(decoded_data))
# The content of the decoded data is: 

# TEST CASE 3
one_letter = "AAAAAA"
print("The content of the data is: {}\n".format(one_letter))
# The content of the data is: AAAAAA
print("The size of the data is: {}\n".format(sys.getsizeof(one_letter)))
# The size of the data is: 55

encoded_data, tree = huffman_encoding(one_letter)
print("The content of the encoded data is: {}\n".format(encoded_data))
# The content of the encoded data is: 000000
print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
The size of the encoded data is: 24

decoded_data = huffman_decoding(encoded_data, tree)
print("The content of the decoded data is: {}\n".format(decoded_data))
# The content of the decoded data is: AAAAAA 
print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
# The size of the decoded data is: 55