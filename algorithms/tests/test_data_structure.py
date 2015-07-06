import unittest
from ..data_structure import stack,queue,union_find,union_find_by_rank,union_find_with_path_compression, hashtable

class TestStack(unittest.TestCase):
    """
    Test Stack Implementation
    """
    def test_stack(self):
        self.sta = stack.stack()
        self.sta.add(5)
        self.sta.add(8)
        self.sta.add(10)
        self.sta.add(2)

        self.assertEqual(self.sta.remove(),2)
        self.assertEqual(self.sta.is_empty(),False)
        self.assertEqual(self.sta.size(),3)

class TestQueue(unittest.TestCase):
    """
    Test Queue Implementation
    """
    def test_queue(self):
        self.que = queue.queue()
        self.que.add(1)
        self.que.add(2)
        self.que.add(8)
        self.que.add(5)
        self.que.add(6)

        self.assertEqual(self.que.remove(),1)
        self.assertEqual(self.que.size(),4)
        self.assertEqual(self.que.remove(),2)
        self.assertEqual(self.que.remove(),8)
        self.assertEqual(self.que.remove(),5)
        self.assertEqual(self.que.remove(),6)
        self.assertEqual(self.que.is_empty(),True)

class TestUnionFind(unittest.TestCase):
    """
    Test Union Find Implementation
    """
    def test_union_find(self):
        self.uf = union_find.UnionFind(4)
        self.uf.make_set(4)
        self.uf.union(1, 0)
        self.uf.union(3, 4)

        self.assertEqual(self.uf.find(1), 0)
        self.assertEqual(self.uf.find(3), 4)
        self.assertEqual(self.uf.is_connected(0, 1), True)
        self.assertEqual(self.uf.is_connected(3, 4), True)

class TestUnionFindByRank(unittest.TestCase):
    """
    Test Union Find Implementation
    """
    def test_union_find_by_rank(self):
        self.uf = union_find_by_rank.UnionFindByRank(6)
        self.uf.make_set(6)
        self.uf.union(1, 0)
        self.uf.union(3, 4)
        self.uf.union(2, 4)
        self.uf.union(5, 2)
        self.uf.union(6, 5)

        self.assertEqual(self.uf.find(1), 1)
        self.assertEqual(self.uf.find(3), 3)
        # test tree is created by rank
        self.uf.union(5, 0)
        self.assertEqual(self.uf.find(2), 3)
        self.assertEqual(self.uf.find(5), 3)
        self.assertEqual(self.uf.find(6), 3)
        self.assertEqual(self.uf.find(0), 3)

        self.assertEqual(self.uf.is_connected(0, 1), True)
        self.assertEqual(self.uf.is_connected(3, 4), True)
        self.assertEqual(self.uf.is_connected(5, 3), True)

class TestUnionFindWithPathCompression(unittest.TestCase):
    """
    Test Union Find Implementation
    """
    def test_union_find_with_path_compression(self):
        self.uf = union_find_with_path_compression.UnionFindWithPathCompression(5)
        self.uf.make_set(5)
        self.uf.union(0, 1)
        self.uf.union(2, 3)
        self.uf.union(1, 3)
        self.uf.union(4, 5)
        self.assertEqual(self.uf.find(1), 0)
        self.assertEqual(self.uf.find(3), 0)
        self.assertEqual(self.uf.parent(3), 2)
        self.assertEqual(self.uf.parent(5), 4)
        self.assertEqual(self.uf.is_connected(3, 5), False)
        self.assertEqual(self.uf.is_connected(4, 5), True)
        self.assertEqual(self.uf.is_connected(2, 3), True)
        # test tree is created by path compression
        self.uf.union(5, 3)
        self.assertEqual(self.uf.parent(3), 0)

        self.assertEqual(self.uf.is_connected(3, 5), True)

class TestHashTable(unittest.TestCase):
    """
    Test Hash Table Implementation
    """
    def setUp(self):
        self.ht = hashtable.HashTable()
        self.ht[1] = 'naughty'
        self.ht[2] = 'nice'
        self.ht['monte hall'] = -2
        self.ht[-3] = (1,2)

    def test_put_get_remove(self):
        self.assertEqual(self.ht[1], 'naughty')
        self.ht[1] = 'very naughty'
        self.assertEqual(self.ht[1], 'very naughty')
        self.assertEqual(self.ht[2], 'nice')
        self.assertEqual(self.ht['monte hall'], -2)
        self.assertEqual(self.ht[-3], (1,2))
        self.assertEqual(self.ht.n, 4)
        self.assertEqual(self.ht.table_size, 31)
        self.ht.remove('monte hall')
        self.assertEqual(self.ht['monte hall'], None)
        self.assertEqual(self.ht.n, 3)
        with self.assertRaises(TypeError):
            self.ht[{}] = 1
            self.ht[set(1,2,3)] = 'haha'
        self.ht.remove(1)
        with self.assertRaises(KeyError):
            self.ht.remove(1)

    def test_clear(self):
        self.ht.clear()
        self.assertEqual(self.ht.n,0)

    def test_resize(self):
        self.ht.clear()
        for i in range(1, 6):
            self.ht[1] = 'nice'
            self.ht.remove(1)
            if i == 5:
                self.assertEqual(self.ht.table_size, 1)
            else:
                self.assertEqual(self.ht.table_size, 31 // 2**i)
        for i in range(11):
            self.ht[i] = str(i)
            if i == 10:
                self.assertEqual(self.ht.table_size, 2)
            else:
                self.assertEqual(self.ht.table_size, 1)

    def test_is_empty(self):
        self.ht.clear()
        self.ht[1] = 'naughty'
        self.assertFalse(self.ht.is_empty())
        self.ht.remove(1)
        self.assertTrue(self.ht.is_empty())

    def test_contains(self):
        self.assertTrue(self.ht.contains('monte hall'))
        self.ht.remove('monte hall')
        self.assertFalse(self.ht.contains('monte hall'))
        with self.assertRaises(TypeError):
            self.ht.remove({})

    def test_keys(self):
        self.assertEqual(set(self.ht.keys()), {1,2,-3,'monte hall'})
        self.ht.remove('monte hall')
        self.assertEqual(set(self.ht.keys()), {1,2,-3})
