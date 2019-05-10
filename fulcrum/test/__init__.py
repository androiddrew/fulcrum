import os
import unittest
from fulcrum import create_app, db
from fulcrum.config import basedir


class TestBase(unittest.TestCase):
    """Base class for testing the fulcrum API"""

    def setUp(self):
        app = create_app("test")
        self.app = app
        self.db = db
        with self.app.app_context():
            db.create_all()
        self.client = self.app.test_client(use_cookies=False)

    def tearDown(self):
        with self.app.app_context():
            self.db.session.remove()
            self.db.drop_all()

        if "sqlite" in self.app.config.get("SQLALCHEMY_DATABASE_URI", ""):
            if os.path.exists(os.path.join(basedir, "test.db")):
                os.unlink(os.path.join(basedir, "test.db"))
