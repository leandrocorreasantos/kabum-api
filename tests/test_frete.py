from http.client import (
    OK, BAD_REQUEST
)
from api.app import application
from api.config import TestingConfig


application.config.from_object(TestingConfig)
app = application.test_client()


def test_post_without_data_should_return_bad_request():
    response = app.post("/v1/frete", json={})
    assert response.status_code == BAD_REQUEST.value


def test_post_complete_data_should_return_ok():
    data = {
        "dimensao": {
            "largura": 30,
            "altura": 30
        },
        "peso": 500
    }
    response = app.post("/v1/frete", json=data)
    assert response.status_code == OK.value


def test_post_data_without_peso_should_return_bad_request():
    data = {
        "dimensao": {
            "largura": 30,
            "altura": 30
        }
    }
    response = app.post("/v1/frete", json=data)
    assert response.status_code == BAD_REQUEST.value
