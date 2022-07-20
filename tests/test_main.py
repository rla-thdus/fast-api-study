from fastapi.testclient import TestClient


from main import app

client = TestClient(app)


def test_user_register_should_success_with_correct_data():
    response = client.post("/register", json={"email": "test2", "password": "1234"})
    assert response.status_code == 200
    assert response.json() == {'email': 'test2', 'id': 4, 'is_active': True, 'password': '1234'}


def test_user_register_should_fail_with_duplicated_email():
    response = client.post("/register", json={"email": "ab", "password": "1234"})
    assert response.status_code == 400
    assert response.json() == {'detail': 'email duplicated'}


def test_get_all_users_info_should_success():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [{'email': 'ab', 'id': 1, 'is_active': True, 'password': '1234'},
 {'email': 'abcd', 'id': 3, 'is_active': True, 'password': '1234'}]
