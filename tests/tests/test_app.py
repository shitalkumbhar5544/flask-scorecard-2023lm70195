import app

def test_index():
    client = app.app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, dict)
    assert "Hello" in data["message"]
