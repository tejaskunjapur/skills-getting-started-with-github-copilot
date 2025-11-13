import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    # Add more assertions based on your root endpoint's response

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert isinstance(data, dict)


def test_signup_for_activity():
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    data = response.json()
    assert f"Signed up {email} for {activity}" in data["message"]
