"""
    hashtable.py

    An implementation of hash table data structure.
    In this implementation, seperate chaining is used to deal with collision.
    Dynamic Resizing is implemented in put() and remove() operation to:
        1. Keep load factor l (number of elements/table size) under control
            (2 <l < 10);
        2. Prevent chain gets potentially too long.
    This Implementation can only process key that is hashable in Python,
    if not, TypeError is raised.

    Hash Table Overview:
    ------------------------
    A hash table data structure implements two functions:
        put(key,value) - put a key-value pair in the hash table
        get(key) - return value associated with key
        remove(key) - remove the key-value pair associated with key
        is_empty() - return 1 if empty, else 0
        contains(key) - return 1 if hash table contains this key, else 0
        keys() - return list of keys
        clear() - clear the hash table

    Time Complexity  :  O(1)
    Space Complexity : O(n)

    Psuedo Code: http://algs4.cs.princeton.edu/34hash/
"""


class HashTable:

    def __init__(self, table_size=31):
        self.n = 0  # number of key-value pairs
        self.table_size = table_size
        self.slots = [[] for i in range(self.table_size)]

    def hashcode(self, key):
        try:
            # masks off the sign bit to make sure to return a non-negative int
            return (hash(key) & 0x7fffffff) % self.table_size
        except TypeError:
            raise

    def put(self, key, value):
        if self.n >= 10 * self.table_size:
            # doulbe table size if number of elements >= 10* table size
            self.resize(2 * self.table_size)
        h = self.hashcode(key)
        chain = self.slots[h]
        key_in_chain = False
        for i in range(len(chain)):
            if chain[i][0] == key:
                key_in_chain = True
                chain[i] = (key, value)
        if not key_in_chain:
            self.slots[h].append((key, value))
            self.n += 1

    def get(self, key):
        h = self.hashcode(key)
        chain = self.slots[h]
        for i in range(len(chain)):
            if key == chain[i][0]:
                return chain[i][1]
        return None

    def remove(self, key):
        if not self.contains(key):
            raise KeyError
        else:
            h = self.hashcode(key)
            chain = self.slots[h]
            for i in range(len(chain)):
                if key == chain[i][0]:
                    self.n -= 1
                    del chain[i]
            # half the table_size if number of elements <= 2* table size
            if self.n <= 2 * self.table_size:
                self.resize(self.table_size // 2)

    def resize(self, table_size):
        # make sure table size >= 1
        if table_size == 0:
            table_size = 1
        temp = HashTable(table_size)
        for slot in self.slots:
            for item in slot:
                temp.put(*item)
        self.n = temp.n
        self.table_size = temp.table_size
        self.slots = temp.slots

    def is_empty(self):
        return self.n == 0

    def contains(self, key):
        return self.get(key) is not None

    def keys(self):
        return [item[0] for slot in self.slots for item in slot]

    def clear(self):
        temp = HashTable()
        self.n = temp.n
        self.table_size = temp.table_size
        self.slots = temp.slots

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)
