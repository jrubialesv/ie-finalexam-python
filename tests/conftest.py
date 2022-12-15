import pytest
from iebank_api.models import Account
from iebank_api import db, app


@pytest.fixture
def testing_client(scope='module'):
    db.create_all()
    account = Account('Test Account', '€')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()

    # Modify the existing fixture so that it is executed for every test case 

@pytest.fixture
def testing_client(scope='function'):
    db.create_all()
    account = Account('Test Account', '€')
    db.session.add(account)
    db.session.commit()

    with app.test_client() as testing_client:
        yield testing_client

    db.drop_all()