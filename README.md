# No-as-a-Service

A tiny HTTP API that answers every request with one word: **No.**

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
No
```

## Endpoints

Only `GET` requests are handled.

| Path     | Response               |
|----------|------------------------|
| `/`      | `No`                   |
| `/<any>` | `No`                   |
| `/docs`  | Usage documentation    |

All responses are `200 OK` with `Content-Type: text/plain; charset=utf-8`.

## How it works

`NoHandler` extends `http.server.BaseHTTPRequestHandler` and implements `do_GET`. It returns the module docstring for `/docs` and `"No"` for everything else. `main()` starts an `HTTPServer` and shuts it down cleanly on `Ctrl+C`.

## Reading the docs

The docs live in the code's docstrings. You can also read them with Python's built-in tools:

```bash
python3 -m pydoc ./no_as_a_service.py
```

## Notes

This uses Python's built-in development server, which is great for fun and small projects. For heavy traffic, put it behind a proper WSGI/ASGI server or reverse proxy.

## License

Choose a license for your repo (for example [MIT](https://choosealicense.com/licenses/mit/)) and add a `LICENSE` file.
