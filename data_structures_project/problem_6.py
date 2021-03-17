

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    unions = LinkedList()
    set1 = set()
    set2 = set()

    # add unique items from list1 to set1
    curr1 = llist_1.head
    while curr1:
        set1.add(curr1.value)
        curr1 = curr1.next

    # add unique items from list2 to set2
    curr2 = llist_2.head
    while curr2:
        set2.add(curr2.value)
        curr2 = curr2.next

    # get all items from both sets
    comb_set = (set1 | set2)

    # return None if combined set is empty
    if len(comb_set) == 0:
        return None

    # add items to LinkedList
    for item in comb_set:
        unions.append(item)

    return unions

def intersection(llist_1, llist_2):
    intersections = LinkedList()
    set1 = set()
    set2 = set()

    # add unique items from list1 to set1
    curr1 = llist_1.head
    while curr1:
        set1.add(curr1.value)
        curr1 = curr1.next

    # add unique items from list2 to set2
    curr2 = llist_2.head
    while curr2:
        set2.add(curr2.value)
        curr2 = curr2.next

    # get overlapping items from both sets
    comb_set = (set1 & set2)

    # return None if combined set is empty
    if len(comb_set) == 0:
        return None
    
    # add items to LinkedList
    for item in comb_set:
        intersections.append(item)

    return intersections


# TEST CASE 1
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1,2,3,4]
element_2 = [3,4,5]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# 1 -> 2 -> 3 -> 4 -> 5 ->
print(intersection(linked_list_1,linked_list_2))
# 3 -> 4 -> 

# TEST CASE 2
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->
print(intersection(linked_list_1,linked_list_2))
#4 -> 21 -> 6 ->

# TEST CASE 3
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print(union(linked_list_1,linked_list_2))
# None
print(intersection(linked_list_2,linked_list_2))
# None

