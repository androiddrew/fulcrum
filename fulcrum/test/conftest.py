import os
import pytest

from fulcrum import create_app, db as _db

TESTDB_PATH = ''


@pytest.fixture(scope='session')
def app(request):
    """Session-wide test 'Flask' application"""
    app = create_app('test')

    # Establish an application context before running the tests
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    # Add note
    request.addfinalizer(teardown)
    return app

@pytest.fixture(scope='session')
def db(app, request):
    """Session-wide test database"""

    # If a test db file is found delete it. Assumption sqlite.
    if os.path.exists(TESTDB_PATH):
        os.unlink(TESTDB_PATH)

    def teardown():
        _db.drop_all()
        os.unlink(TESTDB_PATH)

    _db.app = app
    _db.create_all()

    request.addfinalizer(teardown)
    return _db

@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database sessoin for a test"""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
