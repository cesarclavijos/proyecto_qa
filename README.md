python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium

```


## Compuerta (HTTP Basic Auth)
Pon `SPENDWISE_GATE_USER` y `SPENDWISE_GATE_PASSWORD` en `.env`. Se usan en el navegador
(tests de UI) y al pedir el token de la API. Vacías = sin compuerta.


## Ejecutar
```bash
pytest                       # headless
pytest --headed --slowmo 500 # viendo el navegador
pytest -m smoke              # solo smoke
```
Screenshots, videos y traces de fallos quedan en `test-results/`
(ver trace: `playwright show-trace test-results/<carpeta>/trace.zip`).


## Pruebas de API
Usan `requests`. Primero se pide un bearer token
y se manda en el header `Authorization: Bearer <token>` de las siguientes llamadas.


El token se pide con `{"email", "password"}` (JSON). Define en `.env`: 


```bash
pytest tests/api   # solo API
pytest -m api      # igual, por marker
pytest -m "not api"  # solo UI
```

