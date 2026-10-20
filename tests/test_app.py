import json
from app import app


def test_home_page():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"CloudDeploy" in response.data
    assert b"Deployment & Monitoring Dashboard" in response.data


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200

    data = json.loads(response.data)

    assert data["status"] == "healthy"
    assert data["application"] == "CloudDeploy"
    assert "version" in data
    assert "timestamp" in data


def test_system_information():
    client = app.test_client()
    response = client.get("/api/info")

    assert response.status_code == 200

    data = json.loads(response.data)

    assert data["application"] == "CloudDeploy"
    assert data["environment"] == "Development"
    assert "python_version" in data
    assert "platform" in data
    assert data["uptime_seconds"] >= 0


def test_unknown_route():
    client = app.test_client()
    response = client.get("/does-not-exist")

    assert response.status_code == 404