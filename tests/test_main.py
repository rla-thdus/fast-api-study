from fastapi.testclient import TestClient


from main import app

client = TestClient(app)


def test_user_register_should_success_with_correct_data():
    response = client.post("/register", json={"email": "ab", "password": "1234"})
    assert response.status_code == 200
    assert response.json() == {"message": "register success"}

def test_user_register_should_fail_with_duplicated_email():
    response = client.post("/register", json={"email": "ab", "password": "1234"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'email duplicated'}
