# No-as-a-Service

A tiny HTTP API that answers every request with a random way of saying **no**.

Pure Python standard library. One file, zero dependencies.

## Quick start

Requires Python 3.6 or newer.

```bash
python3 no_as_a_service.py
```

The server listens on `http://0.0.0.0:8000`. To use a different port, pass it as an argument:

```bash
python3 no_as_a_service.py 5000
```

Stop it with `Ctrl+C`.

## Usage

```bash
curl http://localhost:8000/
```

```
Not a chance
```

Each request gets a randomly picked phrase from the built-in list:

- No
- Nope
- Not a chance
- Absolutely not
- No way
- Negative
- Nope, sorry

The usage docs are served at `/docs`:

```bash
curl http://localhost:8000/docs
```

## Endpoints

Only `GET` requests are handled.

| Path     | Response               |
|----------|------------------------|
| `/`      | Random "no" phrase     |
| `/<any>` | Random "no" phrase     |
| `/docs`  | Usage documentation    |

All responses are `200 OK` with `Content-Type: text/plain; charset=utf-8` and a `Content-Length` header. `/docs/` (with a trailing slash) also returns the docs.

## How it works

`NoHandler` extends `http.server.BaseHTTPRequestHandler` and implements `do_GET`. It returns the module docstring for `/docs` and `random.choice(ANSWERS)` for everything else. `main()` starts an `HTTPServer` and shuts it down cleanly on `Ctrl+C`.

## Customizing the answers

Edit the `ANSWERS` list at the top of `no_as_a_service.py` to add or remove phrases. Every entry has the same chance of being returned.

## Reading the docs

The docs live in the code's docstrings. You can also read them with Python's built-in tools:

```bash
python3 -m pydoc ./no_as_a_service.py
```

## Notes

This uses Python's built-in development server, which is great for fun and small projects. For heavy traffic, put it behind a proper WSGI/ASGI server or reverse proxy.
