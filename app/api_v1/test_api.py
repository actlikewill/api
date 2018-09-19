
import pytest
from app import create_app

@pytest.fixture
def client(request):
    test_client = create_app('default').test_client()

    def teardown():
        pass # databases and resourses have to be freed at the end. But so far we don't have anything

    request.addfinalizer(teardown)
    return test_client

def test_get_orders(client):
    response = client.get('/api/v1/orders')
    assert response.status_code == 200

def test_orders_post(client):
    response = client.post('api/v1/orders?item=Burger&quantity=2')
    assert response.status_code == 201
    assert b'Burger' in response.data



def test_no_quantity(client):
    response = client.post('api/v1/orders?item=Burger')
    assert b'sorry' in response.data

def test_no_item(client):
    response = client.post('api/v1/orders?quantity=1')
    assert b'sorry' in response.data

def test_no_item(client):
    response = client.post('api/v1/orders?quantity=3')
    assert b'sorry' in response.data

