
import pytest
from app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def test_index(client):
    response = client.get('/', content_type='html/text')
    assert b'Hello World' in response.data

def test_users_post(client):
    response = client.post('/orders?item=Burger&quantity=2')
    assert response.status_code == 201