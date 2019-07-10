

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    return (hash % max) & 0xFFFFFFFF


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    new_val = LinkedPair(key, value)
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        hash_table.storage[index] = new_val
        return new_val
    curr = hash_table.storage[index]
    while curr.next:
        curr = curr.next
    curr.next = new_val
    return new_val


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
# 1 -> 2 -> 3 -> 4 -> 5
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        raise IndexError("Invalid key")
    curr = hash_table.storage[index]
    prev = None
    while curr:
        if curr.key == key:
            prev.next = curr.next
            curr.next = None
        prev = curr
        curr = curr.next


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        raise IndexError("Invalid key")
    curr = hash_table.storage[index]
    while curr:
        if curr.key == key:
            return curr.value
        curr = curr.next


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    x = len(hash_table.storage)
    capacity = x * 2
    z = HashTable(capacity)
    for i in range(0, len(hash_table.storage) - 1):
        z.storage[i] = hash_table.storage[i]
    return z


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
