import pytest
from main import app


def test_post_api():
    response = app.test_client().get('/api/posts')
    assert type(response.json) == list
    assert response.status_code == 200


def test_post_api_by_id():
    response = app.test_client().get('/api/posts/2')
    assert type(response.json) == dict
