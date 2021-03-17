

class RouteTrieNode:
    def __init__(self, handler=None):
        # initialize node
        self.children = {}
        self.handler = handler

    def insert(self, path_element, handler):
        # insert node
        self.children[path_element] = RouteTrieNode(handler)


class RouteTrie:
    def __init__(self, root_handler=None):
        # initialize trie with a root node and a handler
        self.root = RouteTrieNode(root_handler)

    def insert(self, path_elements, handler):
        # start at root
        node = self.root

        # check nodes for each path item; if not there, add it
        for path_element in path_elements:
            if path_element not in node.children:
                node.children[path_element] = RouteTrieNode(None)
            # move to next node
            node = node.children[path_element] 
        
        # add handler to deepest node of path (the leaf)
        node.handler = handler
        
    def find(self, path_elements):
        # start at root
        node = self.root

        # check nodes for each path item; retun None if item not there
        for path_element in path_elements:
            if path_element not in node.children:
                return None
            # move to next node
            node = node.children[path_element]
        
        # at the end of the path, return the handler
        return node.handler


# router class wraps the Trie and handle 
class Router:
    def __init__(self, handler):
        # initialize with RouteTrie
        self.route_trie = RouteTrie(handler)
        #self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        # add a handler for a path
        path_elements = self.split_path(path)
        self.route_trie.insert(path_elements, handler)

    def lookup(self, path):
        # lookup path by parts and return the associated handler
        path_elements = self.split_path(path)
        return self.route_trie.find(path_elements)

    def split_path(self, path):
        # split the path into parts
        if path == '/':
            return []
        return [path_element for path_element in path.split('/') if path_element]


# TEST CASE 1
router1 = Router("root handler")
router1.add_handler("/home/about", "about handler")  
print(router1.lookup("/")) 
# should print 'root handler'
print(router1.lookup("/home")) 
# should print None
print(router1.lookup("/home/about")) 
# should print 'about handler'
print(router1.lookup("/home/about/me")) 
# should print None

# TEST CASE 2
router2 = Router("root handler")
router2.add_handler("/", "about handler")
print(router2.lookup("/"))
# should print 'about handler'
print(router2.lookup("/home"))
# should print None

# TEST CASE 3
router3 = Router("")
router3.add_handler("/blog/2019-01-15/my-awesome-blog-post", "about handler")
print(router3.lookup("/blog"))
# should print None
print(router3.lookup("/blog/2019-01-15/my-awesome-blog-post"))
# should print 'about handler'