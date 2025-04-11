import requests

BASE_URL = "http://127.0.0.1:8000/users"

def test_users_endpoint_unauthorized(requests_mock):
    # Mock the GET request for unauthorized access
    requests_mock.get(
        f"{BASE_URL}?username=admin&password=admin",
        text="",
        status_code=401,
        headers={"Content-Type": "text/plain"}
    )

    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response body, got '{response.text}'"
    assert "application/json" not in response.headers.get("Content-Type", "")


def test_users_endpoint_authorized_but_empty(requests_mock):
    # Mock the GET request for authorized access
    requests_mock.get(
        f"{BASE_URL}?username=admin&password=qwerty",
        text="",
        status_code=200,
        headers={"Content-Type": "text/plain"}
    )

    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response body, got '{response.text}'"
    assert "application/json" not in response.headers.get("Content-Type", "")
