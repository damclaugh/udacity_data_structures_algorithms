
from collections import OrderedDict

class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        if key not in self.cache:
            return -1
        else:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value

    def set(self, key, value):
        if self.capacity <= 0:
            error = 'Capacity at 0. Unable to add element.'
            return error
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        try:
            self.cache.pop(key)
        except KeyError:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
        self.cache[key] = value



# TEST CASE 1
cache = LRU_Cache(5)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(4, 4)

print(cache.get(1))
# 1
print(cache.get(2))
# 2
print(cache.get(9)) 
# -1    

# TEST CASE 2
cache = LRU_Cache(2)
cache.set(1, 1)
cache.set(2, 2)
cache.set(3, 3)
cache.set(5, 5) 
cache.set(6, 6)
print(cache.get(3))     
# -1

# TEST
cache = LRU_Cache(0)
print(cache.set(1, 1))
# Capacity at 0. Unable to add element.
print(cache.get(1))
# -1