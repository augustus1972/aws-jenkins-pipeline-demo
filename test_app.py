from application import application

def test_health():
    r = application.test_client().get("/health")
    assert r.status_code == 200
    assert r.json["status"] == "ok"
