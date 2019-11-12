import os
import os.path

from programy.rdf.collection import RDFCollection
from programy.storage.stores.file.config import FileStorageConfiguration
from programy.storage.stores.file.config import FileStoreConfiguration
from programy.storage.stores.file.engine import FileStorageEngine
from programy.storage.stores.file.store.rdfs import FileRDFStore
from programytest.storage.asserts.store.assert_rdfs import RDFStoreAsserts


class FileRDFStoreTests(RDFStoreAsserts):

    def test_initialise(self):
        config = FileStorageConfiguration()
        engine = FileStorageEngine(config)
        engine.initialise()
        store = FileRDFStore(engine)
        self.assertEqual(store.storage_engine, engine)

    def test_load_from_test_dir_no_subdir(self):
        config = FileStorageConfiguration()
        config._rdf_storage = FileStoreConfiguration(dirs=[os.path.dirname(__file__) + os.sep + "data" + os.sep + "rdfs" + os.sep + "text"], extension="rdf", subdirs=False, fileformat="text", encoding="utf-8", delete_on_start=False)
        engine = FileStorageEngine(config)
        engine.initialise()
        store = FileRDFStore(engine)

        map_collection = RDFCollection()
        store.load_all(map_collection)

        self.assertTrue(map_collection.contains('ACTIVITY'))

    def test_load_from_test_dir_with_subdir(self):
        config = FileStorageConfiguration()
        config._rdf_storage = FileStoreConfiguration(dirs=[os.path.dirname(__file__) + os.sep + "data" + os.sep + "rdfs" + os.sep + "text"], extension="rdf", subdirs=True, fileformat="text", encoding="utf-8", delete_on_start=False)
        engine = FileStorageEngine(config)
        engine.initialise()
        store = FileRDFStore(engine)

        map_collection = RDFCollection()
        store.load_all(map_collection)

        self.assertTrue(map_collection.contains('ACTIVITY'))
        self.assertTrue(map_collection.contains('ANIMAL'))
