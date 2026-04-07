To run the unit tests, run the following command to install the dependencies:
```bash
cd tests
pip install -r requirements.txt
cd ../backend/api
pip install -r requirements.txt
cd ../../backend/gateway
pip install -r requirements.txt
```

To run the protected forwarding test against a gateway configured for a protected Orion:
```bash
cd ..
python -m pytest tests/test_forwarding_auth.py
```

Required env vars for `tests/test_forwarding_auth.py`:
- `AUTH_ENABLED=true`
- `AUTH_SERVER_URL`
- `AUTH_REALM`
- `AUTH_CLIENT_ID`
- `AUTH_CLIENT_SECRET`
