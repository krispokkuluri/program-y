import unittest
import unittest.mock
from programy.storage.entities.sets import SetsReadOnlyStore
from programy.storage.entities.sets import SetsReadWriteStore


class SetsStoreTests(unittest.TestCase):

    def test_split_into_fields(self):
        pass

    def test_add_set_values(self):
        pass


class SetsReadOnlyStoreTests(unittest.TestCase):

    def test_load(self):
        store = SetsReadOnlyStore()
        with self.assertRaises(NotImplementedError):
            collector = unittest.mock.Mock()
            store.load(collector)

    def test_load_all(self):
        store = SetsReadOnlyStore()
        with self.assertRaises(NotImplementedError):
            collector = unittest.mock.Mock()
            store.load(collector)


class SetsReadWriteStoreTests(unittest.TestCase):

    def test_process_line(self):
        pass

    def test_load(self):
        store = SetsReadWriteStore()
        with self.assertRaises(NotImplementedError):
            collector = unittest.mock.Mock()
            store.load(collector)

    def test_load_all(self):
        store = SetsReadWriteStore()
        with self.assertRaises(NotImplementedError):
            collector = unittest.mock.Mock()
            store.load(collector)

    def test_add_to_map(self):
        store = SetsReadWriteStore()
        with self.assertRaises(NotImplementedError):
            name = unittest.mock.Mock()
            value = unittest.mock.Mock()
            store.add_to_set(name, value)

    def test_remove_from_set(self):
        store = SetsReadWriteStore()
        with self.assertRaises(NotImplementedError):
            name = unittest.mock.Mock()
            key = unittest.mock.Mock()
            store.remove_from_set(name, key)

