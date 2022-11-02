"""_summary_"""
import uuid

import pytest
from schema import Schema
from starlette.testclient import TestClient

from blog.main import app
from blog.jwk_token import create_access_token

client = TestClient(app)

token_schema = Schema({"access_token": str, "token_type": "bearer"})
user_schema = Schema(
    {"name": str, "email": str, "blogs": [{"title": str, "body": str}]}
)

ACCESS_TOKEN = create_access_token(
    data={"user": "rahulreghunath11@gmail.com", "scopes": ["blogs"]}
)

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


@pytest.mark.parametrize(
    "body, status_code, result, check_type",
    (
        (
            {},
            422,
            {
                "detail": [
                    {
                        "loc": ["body", "username"],
                        "msg": "field required",
                        "type": "value_error.missing",
                    },
                    {
                        "loc": ["body", "password"],
                        "msg": "field required",
                        "type": "value_error.missing",
                    },
                ]
            },
            "VALUE",
        ),
        (
            {"username": "wrong username", "password": "password"},
            401,
            {"detail": "Invalid Credentials"},
            "VALUE",
        ),
        (
            {"username": "rahulreghunath11@gmail.com", "password": "password"},
            200,
            token_schema,
            "SCHEMA",
        ),
    ),
)
def test_login_user(body, status_code, result, check_type):
    """test user routes."""

    response = client.post("/login", body)
    assert response.status_code == status_code

    if check_type == "SCHEMA":
        assert result.validate(response.json())
    else:
        assert response.json() == result


EMAIL = str(uuid.uuid1()) + "@cloudium.io"


@pytest.mark.parametrize(
    "body, status_code, result",
    [
        (
            {"name": "name", "email": EMAIL, "password": "password"},
            201,
            {"details": "User Added"},
        ),
        (
            {"name": "name", "email": EMAIL, "password": "password"},
            422,
            {
                "detail": [
                    {
                        "loc": ["body", "email"],
                        "msg": "Email already exist",
                        "type": "value_error",
                    }
                ]
            },
        ),
    ],
)
def test_create_user(body, status_code, result):
    """_summary_

    Args:
        body (_type_): _description_
        status_code (_type_): _description_
        result (_type_): _description_
    """
    response = client.post("/users", json=body)
    assert response.status_code == status_code
    assert response.json() == result


@pytest.mark.parametrize(
    "id, status_code, schema, check_type, result",
    [
        (1, 200, user_schema, "SCHEMA", {}),
        (0, 404, user_schema, "VALUE", {"detail": "Blog not found"}),
    ],
)
def test_get_user(user_id, status_code, schema, check_type, result):
    """_summary_

    Args:
        id (_type_): _description_
        status_code (_type_): _description_
        schema (_type_): _description_
        authentication (_type_): _description_
        type (_type_): _description_
        result (_type_): _description_
    """
    response = client.get(f"/users/{user_id}", headers=headers)
    print(response.json())
    assert response.status_code == status_code
    if check_type == "SCHEMA":
        assert schema.validate(response.json())
    else:
        assert response.json() == result
