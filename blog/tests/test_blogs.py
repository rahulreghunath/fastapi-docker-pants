"""_summary_"""
import pytest
from schema import Schema
from starlette.testclient import TestClient

from blog.main import app
from blog.jwk_token import create_access_token

client = TestClient(app)

blog = {"title": str, "body": str, "creator": {"name": str, "email": str}}
blogs_schema = Schema([blog])
blog_schema = Schema(blog)

ACCESS_TOKEN = create_access_token(
    data={"user": "rahulreghunath11@gmail.com", "scopes": ["blogs"]}
)

headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}


@pytest.mark.parametrize(
    "status_code, result, check_type, url, authentication",
    (
        (401, {"detail": "Not authenticated"}, "VALUE", "/blogs", {}),
        (401, {"detail": "Not authenticated"}, "VALUE", "/blogs/1", {}),
        (200, blogs_schema, "SCHEMA", "/blogs", headers),
        (200, blog_schema, "SCHEMA", "/blogs/1", headers),
    ),
)
def test_get_blog(status_code, result, check_type, url, authentication):
    """test blogs routes."""
    # pylint: disable=duplicate-code
    response = client.get(url, headers=authentication)

    assert response.status_code == status_code

    if check_type == "SCHEMA":
        assert result.validate(response.json())
    else:
        assert response.json() == result
