import pytest
import os
from api.spendwise_api import SpendWiseAPI, get_token, sesion_con_compuerta




@pytest.fixture(scope="session")
def token(sesion):
    return get_token( sesion, os.getenv("ADMIN_EMAIL"), os.getenv("ADMIN_PASSWORD"))




@pytest.fixture(scope="session")
def spend_wise(sesion, token):
    sesion.headers["Authorization"] = f"Bearer {token}"   # cookie + Bearer en cada llamada
    return SpendWiseAPI(sesion)


@pytest.fixture(scope="session")
def sesion():
    return sesion_con_compuerta()          # navegador -> cookie sw_session -> requests