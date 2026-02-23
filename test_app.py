import pytest
from app import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_endpoint(client):
    """Test the home endpoint returns correct JSON."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Welcome to CI/CD Flask App!"
    assert data["status"] == "running"
    assert "version" in data


def test_health_endpoint(client):
    """Test the health check endpoint."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "healthy"
    assert "environment" in data


def test_info_endpoint(client):
    """Test the info endpoint returns correct structure."""
    response = client.get("/api/info")
    assert response.status_code == 200
    data = response.get_json()
    assert "app" in data
    assert "author" in data
    assert "description" in data


def test_404_endpoint(client):
    """Test that non-existent endpoints return 404."""
    response = client.get("/nonexistent")
    assert response.status_code == 404
