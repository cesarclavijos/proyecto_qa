import pytest


CAMPOS = {
    "id", "expenseNumber", "description", "vendor", "amount", "date",
    "categoryId", "categoryName", "status", "notes", "receiptUrl", "createdAt",
}


@pytest.mark.api
@pytest.mark.smoke
def test_expenses_check_json(spend_wise):
    resp = spend_wise.expenses()
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert items, "No hay gastos para validar"

    for item in items:
        faltan = CAMPOS - item.keys()
        sobran = item.keys() - CAMPOS
        assert not faltan and not sobran, (
            f"{item.get('expenseNumber', '?')}: faltan {sorted(faltan)}, sobran {sorted(sobran)}"
        )