import pytest

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello from Flask!'

def test_multiply(client):
    response = client.get('/multiply?a=4&b=5')
    assert response.status_code == 200
    assert response.json['result'] == 20
