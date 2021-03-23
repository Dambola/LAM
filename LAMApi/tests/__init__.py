import os
import tempfile

import pytest

from lamapi import app, db
from lamapi.db_init import db_init

@pytest.fixture
def client():
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db_init(db)
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])