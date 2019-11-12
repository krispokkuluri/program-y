import unittest

import programytest.storage.engines as Engines
from programy.storage.stores.nosql.mongo.config import MongoStorageConfiguration
from programy.storage.stores.nosql.mongo.engine import MongoStorageEngine
from programy.storage.stores.nosql.mongo.store.lookups import MongoDenormalStore
from programytest.storage.asserts.store.assert_denormals import DenormalStoreAsserts


class MongoDenormalStoreTests(DenormalStoreAsserts):

    @unittest.skipIf(Engines.mongo is False, Engines.mongo_disabled)
    def test_initialise(self):
        config = MongoStorageConfiguration()
        engine = MongoStorageEngine(config)
        engine.initialise()
        store = MongoDenormalStore(engine)
        self.assertEqual(store.storage_engine, engine)

    @unittest.skipIf(Engines.mongo is False, Engines.mongo_disabled)
    def test_upload_from_file(self):
        config = MongoStorageConfiguration()
        engine = MongoStorageEngine(config)
        engine.initialise()
        store = MongoDenormalStore(engine)

        self.assert_upload_from_file(store)

