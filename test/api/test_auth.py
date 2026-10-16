import pytest
import os


@pytest.mark.api
@pytest.mark.smoke
def test_me_devuelve_la_cuenta(spend_wise):
    resp = spend_wise.me()
    assert resp.status_code == 200
    body = resp.json()
    assert str(body["email"]) == str(os.getenv("ADMIN_EMAIL"))