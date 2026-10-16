import pytest


@pytest.mark.api
@pytest.mark.smoke
def test_categories_check_total(spend_wise):
    resp = spend_wise.categories()
    assert resp.status_code == 200
    assert len(resp.json()) == 9, f"Se esperaban 9 categorías y llegaron {len(resp.json())}"