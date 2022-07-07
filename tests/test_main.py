from fastapi.testclient import TestClient


from main import app

client = TestClient(app)


def test_user_register_should_success_with_correct_data():
    response = client.post("/register", json={"email": "ab", "pwd": "1234"})
    assert response.status_code == 200
    assert response.json() == {"message": "register success"}
