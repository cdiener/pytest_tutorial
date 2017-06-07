"""Unit tests for networker."""

import pytest
import json
from networker.app import app
from networker.app import validate


@pytest.fixture
def test_app():
    """Set up an app instance for testing."""
    return app.test_client()


@pytest.mark.parametrize("name", ["miserables", "e_coli.json"])
def test_validate_good(name):
    assert validate(name)


@pytest.mark.parametrize("name", ["miserables123", "README.md"])
def test_bad_file(name):
    assert not validate(name)


def test_bad_json(tmpdir):
    json_file = tmpdir.join("bad.json")
    json_file.write('{"text": "hello", "name": "what?"}')
    assert not validate(str(json_file))


def test_get_json(test_app):
    resp = test_app.get("/json/love_actually")
    content = json.loads(resp.data.decode())
    assert "nodes" in content
    assert "links" in content
    resp = test_app.get("/json/whatever")
    assert resp.mimetype == "text/html"
    assert "sorry" in resp.data.decode()


def test_get_validation(test_app):
    resp = test_app.get("/validate/miserables")
    assert resp.mimetype == "text/plain"
    assert "Yup" in resp.data.decode()
    resp = test_app.get("/validate/miserables123")
    assert "Nope" in resp.data.decode()


def test_force_graph(test_app):
    resp = test_app.get("/miserables")
    assert resp.mimetype == "text/html"
    assert "svg" in resp.data.decode()
    resp = test_app.get("/whatever")
    assert resp.mimetype == "text/html"
    assert "sorry" in resp.data.decode()
