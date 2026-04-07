To run the unit tests, run the following command to install the dependencies:
```bash
cd tests
pip install -r requirements.txt
cd ../backend/api
pip install -r requirements.txt
cd ../../backend/gateway
pip install -r requirements.txt
```
To run the protected Orion auth check:
```bash
cd ..
python -m pytest tests/test_orion_auth.py
```

Required env vars for `tests/test_orion_auth.py`:
- `AUTH_ENABLED=true`
- `AUTH_SERVER_URL` (e.g., `https://sso.example.com`)
- `AUTH_REALM`
- `AUTH_CLIENT_ID`
- `AUTH_CLIENT_SECRET`
