# Receipt service
Zero-dependency reference implementation.

```bash
python receipt_service/server.py
```

- POST `/v1/receipts`
- GET `/v1/stats`

Binds to localhost only. Public deployment must add rate limiting and appropriate abuse controls.
v0.1 never claims cryptographic agent identity.
