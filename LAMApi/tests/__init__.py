from lamapi import createApplication, db
from lamapi.db_init import db_init

import pytest

app = createApplication('lamapi.config.LAMTestConfiguration')
with app.app_context():
    db.drop_all()
    db.create_all()
    db_init(db)

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

        