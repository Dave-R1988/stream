from src.service import app
from fastapi.testclient import TestClient


client = TestClient(app)


def test_cpu_percent():
    response = client.get("/cpu_percent")
    assert response.status_code == 200
    assert len(response.json()) > 0
    for (idx, item) in enumerate(response.json()):
        assert "cpu" in item
        assert "percent" in item
        assert isinstance(item["cpu"], str)
        assert isinstance(item["percent"], float)
        assert item["percent"] >= 0.0
        assert item["percent"] <= 100.0
        assert idx == int(item["cpu"].replace("CPU", ""))
