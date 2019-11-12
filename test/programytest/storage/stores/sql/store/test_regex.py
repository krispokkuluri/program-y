import unittest

import programytest.storage.engines as Engines
from programy.storage.stores.sql.config import SQLStorageConfiguration
from programy.storage.stores.sql.engine import SQLStorageEngine
from programy.storage.stores.sql.store.properties import SQLRegexStore
from programytest.storage.asserts.store.assert_regex import RegexStoreAsserts


class SQLRegexStoreTests(RegexStoreAsserts):

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_initialise(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLRegexStore(engine)
        self.assertEqual(store.storage_engine, engine)

    @unittest.skipIf(Engines.sql is False, Engines.sql_disabled)
    def test_load_regex(self):
        config = SQLStorageConfiguration()
        engine = SQLStorageEngine(config)
        engine.initialise()
        store = SQLRegexStore(engine)

        self.assert_upload_from_file(store)
