# Vobiz Python Library

Typed Python client for the Vobiz programmable voice and SIP-trunking API, with a
built-in VobizXML builder for call-control documents.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Docs](https://img.shields.io/badge/docs-docs.vobiz.ai-3b82f6.svg)](https://docs.vobiz.ai)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=Vobiz%2FPython)

## Overview

The Vobiz Python library gives you a typed, fully synchronous **and** asynchronous
client for the Vobiz REST API. It covers the whole platform surface: placing and
controlling calls, live-call inspection, in-call actions such as text-to-speech and
DTMF, recordings, call detail records, phone-number inventory, SIP trunks and
endpoints, conferences, applications, sub-accounts and KYC, IP access control
lists, balance and the partner API.

The client is generated from the Vobiz OpenAPI specification with
[Fern](https://buildwithfern.com), so every resource group, method, parameter and
response model tracks the published API. Requests are made with
[`httpx`](https://www.python-httpx.org/) and payloads are validated and parsed with
[`pydantic`](https://docs.pydantic.dev/), which means responses come back as typed
objects rather than untyped dictionaries, and your editor can autocomplete them.

Alongside the API client the package ships `vobiz.vobizxml`, a small dependency-free
builder for VobizXML — the XML call-control documents that Vobiz fetches from your
`answer_url` when a call connects. It mirrors the `plivoxml` builder API closely, so
code migrating from Plivo usually only changes the import.

At the end of a first integration you should be able to place an outbound call from
Python, serve a VobizXML document that speaks a prompt and collects a DTMF digit,
watch the call in the live-calls list, and read the resulting CDR — all with typed
request and response objects.

## Installation

The package is not yet on PyPI. Install the current release straight from GitHub:

```sh
pip install "git+https://github.com/vobiz-ai/Vobiz-Python-SDK.git"
```

Pin to a tag or commit for reproducible builds:

```sh
pip install "vobiz @ git+https://github.com/vobiz-ai/Vobiz-Python-SDK.git@<commit-sha>"
```

Or clone and install in editable mode if you want to read the generated source:

```sh
git clone https://github.com/vobiz-ai/Vobiz-Python-SDK.git
cd Vobiz-Python-SDK
pip install -e .
```

Requires Python 3.8 or newer. Runtime dependencies are `httpx>=0.21.2`,
`pydantic>=1.9.2` and `typing_extensions>=4.0.0`; `pip` installs them for you.

Once the package is published to PyPI, `pip install vobiz` will be the recommended
route — see [Roadmap](#roadmap).

## Authentication

Vobiz identifies your account with an **Auth ID** and an **Auth Token**, and
authorises the request with a **bearer token**. All three are read from the client
constructor and sent on every request by
[`core/client_wrapper.py`](./src/vobiz/core/client_wrapper.py):

| Header | Constructor argument | Purpose |
| --- | --- | --- |
| `X-Auth-ID` | `auth_id` | Identifies the account or sub-account |
| `X-Auth-Token` | `auth_token` | Account secret paired with the Auth ID |
| `Authorization: Bearer <token>` | `token` | Bearer credential for the request |

All three arguments are keyword-only and required — the client will not construct
without them:

```python
import os

from vobiz import Vobiz

client = Vobiz(
    auth_id=os.environ["VOBIZ_AUTH_ID"],
    auth_token=os.environ["VOBIZ_AUTH_TOKEN"],
    token=os.environ["VOBIZ_TOKEN"],
)
```

`token` also accepts a zero-argument callable, which is the hook for credentials
that rotate. The callable is invoked once per request, so you can refresh a
short-lived token without rebuilding the client:

```python
client = Vobiz(
    auth_id=os.environ["VOBIZ_AUTH_ID"],
    auth_token=os.environ["VOBIZ_AUTH_TOKEN"],
    token=lambda: my_token_store.current(),
)
```

Keep credentials in environment variables or a secrets manager. Never commit them,
and never ship them to a browser or mobile client — the SDK is intended for
server-side use.

Most methods also take `auth_id` as their **first positional argument**. That is the
account the operation acts on, which lets a parent account drive its sub-accounts
with a single client. It is separate from the `auth_id` you passed to the
constructor, even though the two are usually the same value.

Sign up and find your credentials at [vobiz.ai](https://vobiz.ai); the credential
model is documented at
[docs.vobiz.ai/api-reference](https://docs.vobiz.ai/api-reference).

## Quickstart

Place an outbound call. Vobiz dials `to`, and when the callee answers it fetches
your `answer_url` for a VobizXML document describing what should happen next.

```python
import os

from vobiz import Vobiz

client = Vobiz(
    auth_id=os.environ["VOBIZ_AUTH_ID"],
    auth_token=os.environ["VOBIZ_AUTH_TOKEN"],
    token=os.environ["VOBIZ_TOKEN"],
)

AUTH_ID = os.environ["VOBIZ_AUTH_ID"]

response = client.calls.make_call(
    AUTH_ID,
    from_="14155551234",
    to="+15550003333",
    answer_url="https://example.com/answer",
    answer_method="POST",
)

print(response)
```

Notes on the signature, which is generated and worth reading exactly:

- `from_` carries a trailing underscore because `from` is a Python keyword.
- `from_`, `to`, `answer_url` and `answer_method` are all keyword-only and required.
- `to` accepts multiple destinations separated by `<` to fan a single request out to
  up to 1000 destinations, for example `"+15550003333<+15550004444"`.
- The return value is a typed `MakeCallResponse`, not a dictionary.

## Common operations

Every snippet below reuses the `client` and `AUTH_ID` from the quickstart. Method
signatures come from the generated clients under
[`src/vobiz/`](./src/vobiz); the exhaustive list is in
[`reference.md`](./reference.md) and the shorter cheat-sheet in
[`USAGE.md`](./USAGE.md).

### List live calls

`status` is required and accepts `"live"` or `"queued"`.

```python
live = client.live_calls.list_live_calls(AUTH_ID, status="live")
print(live)

detail = client.live_calls.get_live_call(
    AUTH_ID,
    "cdr_XXXXXXXXXX",
    status="live",
)
```

### Hang up a call

```python
client.live_calls.hangup_call(AUTH_ID, "cdr_XXXXXXXXXX")
```

`hangup_call` returns `None` — a successful termination has no response body.

### Speak text and play audio into a live call

```python
client.speak_text.call(
    AUTH_ID,
    "cdr_XXXXXXXXXX",
    text="Your driver is two minutes away.",
    legs="aleg",
)

client.play_audio.call(
    AUTH_ID,
    "cdr_XXXXXXXXXX",
    urls="https://cdn.example.com/hold-music.mp3",
    loop=True,
)

client.speak_text.stop_speak_call(AUTH_ID, "cdr_XXXXXXXXXX")
client.play_audio.stop_audio_call(AUTH_ID, "cdr_XXXXXXXXXX")
```

### Send DTMF

`leg` is optional and accepts `"aleg"`, `"bleg"` or `"both"`.

```python
client.dtmf.send_dtmf(
    AUTH_ID,
    "cdr_XXXXXXXXXX",
    digits="1234#",
    leg="aleg",
)
```

### Record a call and fetch the recording

```python
client.record_calls.start_recording(
    AUTH_ID,
    "cdr_XXXXXXXXXX",
    file_format="mp3",          # "mp3" or "wav"
    time_limit=600,
    callback_url="https://example.com/recording-ready",
)

client.record_calls.stop_recording(AUTH_ID, "cdr_XXXXXXXXXX")

recordings = client.recordings.list_recordings(AUTH_ID, limit=20, offset=0)
one = client.recordings.get_recording(AUTH_ID, "REC_ID")
client.recordings.delete_recording(AUTH_ID, "REC_ID")
```

### Query call detail records

```python
import datetime as dt

page = client.cdr.list_cdrs(
    AUTH_ID,
    start_date=dt.date(2026, 1, 1),
    end_date=dt.date(2026, 1, 31),
    call_direction="outbound",
    min_duration=30,
    page=1,
    per_page=100,
)

recent = client.cdr.list_recent_cdrs(AUTH_ID, limit=25)
single = client.cdr.get_cdr(AUTH_ID, "CALL_ID")
```

`client.cdr.search_cdrs(...)` takes the same filters as `list_cdrs`, and
`client.cdr.export_cdrs(...)` takes the same filters without the paging arguments.

### Other resource groups

The same pattern — `client.<group>.<method>(auth_id, ...)` — covers
`phone_numbers`, `applications`, `trunks`, `endpoints`, `credentials`,
`conferences`, `conference_members`, `conference_recording`, `audio_streams`,
`sub_accounts`, `sub_account_kyc`, `sub_account_kyc_test_mode`, `balance`,
`account`, `ip_access_control_list`, `origination_uri`, `bulk_operations` and
`partner_api`. See [`reference.md`](./reference.md) for every signature.

## VobizXML

`vobiz.vobizxml` builds the call-control documents Vobiz fetches from your
`answer_url`. It has no dependencies beyond the standard library, so you can import
it in a web handler without constructing an API client.

```python
from vobiz import vobizxml

response = vobizxml.ResponseElement()

gather = response.add_gather(
    action="https://example.com/menu",
    method="POST",
    input_type="dtmf",
    num_digits=1,
    execution_timeout=10,
)
gather.add_speak("Press 1 for sales, or 2 for support.")

response.add_speak("We did not receive any input. Goodbye.")
response.add_hangup()

print(response.to_string())
```

That prints:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Gather action="https://example.com/menu" method="POST" inputType="dtmf" numDigits="1" executionTimeout="10">
        <Speak>Press 1 for sales, or 2 for support.</Speak>
    </Gather>
    <Speak>We did not receive any input. Goodbye.</Speak>
    <Hangup/>
</Response>
```

Points worth knowing:

- **snake_case in, camelCase out.** Keyword arguments are converted by `to_camel()`
  in [`vobizxml/base.py`](./src/vobiz/vobizxml/base.py), so `input_type` becomes
  `inputType` and `execution_timeout` becomes `executionTimeout`. `<Gather>` uses
  `executionTimeout`, not `timeout`.
- **A trailing underscore is stripped**, so Python keywords can be passed:
  `async_=True` emits `async="true"` on `<DTMF>`.
- **Booleans render as `true`/`false`**, and text plus attribute values are XML
  escaped for you.
- **`add_*` helpers return the child element**, so you can keep nesting:
  `response.add_dial().add_number("+15550003333")`.
- **`ssml=` injects raw, unescaped content** into `<Speak>` when you need SSML
  markup.

Elements exported by the builder: `ResponseElement`, `SpeakElement`, `PlayElement`,
`WaitElement`, `GatherElement`, `DialElement`, `NumberElement`, `UserElement`,
`RecordElement`, `ConferenceElement`, `DtmfElement`, `RedirectElement`,
`HangupElement`, `PreAnswerElement` and `StreamElement`.

Migrating from Plivo? `add_get_digits()` and `add_get_input()` are kept as aliases
for `add_gather()`, so `plivoxml` call sites keep working after the import change.

Serving it from Flask:

```python
from flask import Flask, Response
from vobiz import vobizxml

app = Flask(__name__)


@app.post("/answer")
def answer():
    r = vobizxml.ResponseElement()
    r.add_speak("Thanks for calling. Connecting you now.")
    r.add_dial().add_number("+15550003333")
    return Response(r.to_string(), mimetype="application/xml")
```

## Configuration

### Environments and base URL

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    auth_id="...", auth_token="...", token="...",
    environment=VobizEnvironment.PRODUCTION,   # https://api.vobiz.ai
)
```

`VobizEnvironment.PRODUCTION` is the default. To point the client at a proxy,
gateway or local mock, pass `base_url` instead — it takes precedence over
`environment`:

```python
client = Vobiz(
    auth_id="...", auth_token="...", token="...",
    base_url="http://localhost:8080",
)
```

### Constructor options

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `auth_id` | `str` | required | Sent as `X-Auth-ID` |
| `auth_token` | `str` | required | Sent as `X-Auth-Token` |
| `token` | `str` or `() -> str` | required | Sent as `Authorization: Bearer …` |
| `base_url` | `str` | from `environment` | Overrides the environment URL |
| `environment` | `VobizEnvironment` | `PRODUCTION` | `https://api.vobiz.ai` |
| `headers` | `dict[str, str]` | `None` | Extra headers on every request |
| `timeout` | `float` | `60` seconds | Per-request timeout |
| `max_retries` | `int` | `2` | Default retry attempts |
| `follow_redirects` | `bool` | `True` | Redirect handling on the default client |
| `httpx_client` | `httpx.Client` | built for you | Bring your own transport |
| `logging` | `LogConfig` or `Logger` | silent | SDK logging configuration |

### Timeouts

The SDK defaults to a 60 second timeout. Set it once on the client, or override it
for a single call:

```python
client = Vobiz(..., timeout=20.0)

client.cdr.list_cdrs(AUTH_ID, request_options={"timeout_in_seconds": 5})
```

If you pass your own `httpx_client`, its timeout is used and the 60 second default
is not enforced.

### Retries

Failed requests are retried with exponential backoff, up to 2 attempts by default,
on 408, 409, 429 and all 5xx responses. Override per request:

```python
client.calls.make_call(AUTH_ID, ..., request_options={"max_retries": 1})
```

### Custom HTTP client

Useful for proxies, custom transports, connection pooling or mTLS:

```python
import httpx
from vobiz import Vobiz

client = Vobiz(
    auth_id="...", auth_token="...", token="...",
    httpx_client=httpx.Client(
        proxy="http://proxy.internal.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

### Logging

```python
client = Vobiz(..., logging={"level": "debug", "silent": False})
```

Logging is silent by default. Enable it when you are diagnosing a request, and
remember that debug output may include request metadata.

## Error handling

Any non-2xx response raises a subclass of `vobiz.core.api_error.ApiError`, which
carries `status_code`, `body` and `headers`:

```python
from vobiz.core.api_error import ApiError

try:
    client.calls.make_call(AUTH_ID, from_="14155551234", to="+15550003333",
                           answer_url="https://example.com/answer", answer_method="POST")
except ApiError as exc:
    print(exc.status_code)
    print(exc.body)
    print(exc.headers)
```

Status-specific subclasses live in `vobiz.errors` and let you branch without
inspecting `status_code`:

| Exception | Status | Typical cause |
| --- | --- | --- |
| `BadRequestError` | 400 | Malformed or missing parameters |
| `UnauthorizedError` | 401 | Wrong Auth ID, Auth Token or bearer token |
| `ForbiddenError` | 403 | Credentials valid, operation not permitted |
| `NotFoundError` | 404 | Unknown call UUID, recording ID or account |
| `ConflictError` | 409 | Resource already exists or is in a conflicting state |
| `UnprocessableEntityError` | 422 | Request understood but semantically invalid |
| `TooManyRequestsError` | 429 | Rate limited |
| `InternalServerError` | 500 | Server-side failure |

```python
from vobiz.errors import NotFoundError, TooManyRequestsError

try:
    client.live_calls.get_live_call(AUTH_ID, call_uuid, status="live")
except NotFoundError:
    ...  # the call has already ended
except TooManyRequestsError as exc:
    ...  # back off; inspect exc.headers for retry hints
```

A malformed or unexpected response body raises `vobiz.core.parse_error.ParseError`
rather than `ApiError`.

### Raw responses

Use `.with_raw_response` when you need status codes or headers alongside the parsed
body — for example to read rate-limit headers:

```python
raw = client.cdr.with_raw_response.list_cdrs(AUTH_ID, per_page=10)
print(raw.status_code)
print(raw.headers)
print(raw.data)
```

## Pagination and async

### Pagination

Listing methods paginate explicitly; there is no auto-paging iterator, so you drive
the loop yourself. Two conventions are in use:

- **`page` / `per_page`** — `cdr.list_cdrs`, `cdr.search_cdrs`
- **`limit` / `offset`** — `recordings.list_recordings`; `cdr.list_recent_cdrs`
  takes `limit` only

```python
page = 1
while True:
    result = client.cdr.list_cdrs(AUTH_ID, page=page, per_page=100)
    rows = result.data or []
    if not rows:
        break
    for row in rows:
        ...
    page += 1
```

### Async client

`AsyncVobiz` mirrors `Vobiz` method for method. If you pass your own HTTP client,
use `httpx.AsyncClient()` rather than `httpx.Client()`.

```python
import asyncio
import os

from vobiz import AsyncVobiz

client = AsyncVobiz(
    auth_id=os.environ["VOBIZ_AUTH_ID"],
    auth_token=os.environ["VOBIZ_AUTH_TOKEN"],
    token=os.environ["VOBIZ_TOKEN"],
)


async def main() -> None:
    live = await client.live_calls.list_live_calls(
        os.environ["VOBIZ_AUTH_ID"], status="live"
    )
    print(live)


asyncio.run(main())
```

Fan several requests out concurrently with `asyncio.gather`:

```python
async def hang_up_all(auth_id, call_uuids):
    await asyncio.gather(*(client.live_calls.hangup_call(auth_id, u) for u in call_uuids))
```

## Troubleshooting

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `TypeError: __init__() missing 3 required keyword-only arguments: 'auth_id', 'auth_token', and 'token'` | The client requires all three credentials; older snippets pass `api_key=` | Pass `auth_id=`, `auth_token=` and `token=` as keyword arguments |
| `TypeError: make_call() got an unexpected keyword argument 'from'` | `from` is a Python keyword, so the generated parameter is `from_` | Use `from_="14155551234"` |
| `UnauthorizedError` (401) on every call | Auth ID, Auth Token or bearer token is wrong, or credentials belong to a different environment | Re-check the three values against your Vobiz console; confirm `environment`/`base_url` points at the intended host |
| `NotFoundError` (404) from `get_live_call` or `hangup_call` | The call has already ended, so it is no longer in the live-call set | Treat 404 as "already finished"; look the call up in `client.cdr.get_cdr(...)` instead |
| `TypeError: list_live_calls() missing 1 required keyword-only argument: 'status'` | `status` is required, not optional | Pass `status="live"` or `status="queued"` |
| `TooManyRequestsError` (429) during a bulk loop | Requests are being issued faster than the account's rate allowance | Raise `max_retries`, add your own backoff, or reduce concurrency in `asyncio.gather` |
| `httpx.ReadTimeout` on a long export | Default 60 second timeout is shorter than the server needs | Raise it per call: `request_options={"timeout_in_seconds": 300}` |
| `<Gather>` never fires the `action` callback | `timeout` was used instead of `executionTimeout` | Pass `execution_timeout=` to `add_gather()`; the builder emits `executionTimeout` |
| VobizXML renders as escaped text in the browser | The response was served as `text/html` | Serve `to_string()` with `Content-Type: application/xml` |
| `ModuleNotFoundError: No module named 'vobiz'` after `pip install vobiz` | The package is not yet on PyPI | Install from GitHub, see [Installation](#installation) |

## Other Vobiz SDKs

| Language | Repository | Package name |
| --- | --- | --- |
| Node.js / TypeScript | [Vobiz-Node-SDK](https://github.com/vobiz-ai/Vobiz-Node-SDK) | `@vobiz/sdk` |
| Go | [Vobiz-Go-SDK](https://github.com/vobiz-ai/Vobiz-Go-SDK) | `github.com/vobiz-ai/Vobiz-Go-SDK` |
| Ruby | [Vobiz-Ruby-SDK](https://github.com/vobiz-ai/Vobiz-Ruby-SDK) | `vobiz` |
| C# / .NET | [Vobiz-Csharp-sdk](https://github.com/vobiz-ai/Vobiz-Csharp-sdk) | `Vobiz` |

All of them are generated from the same OpenAPI specification, so resource groups
and method names line up across languages once you allow for naming conventions.

## Versioning and stability

The library is at version `0.1.0`. While the major version is `0`, minor releases
may contain breaking changes as the generated surface tracks the API specification.
Pin an exact commit or tag in production and review the diff before upgrading.

The API surface is regenerated from the Vobiz OpenAPI specification, so method and
parameter names can change when the specification changes. `vobiz.vobizxml` is
hand-written and follows the `plivoxml` shape; it is the more stable half of the
package.

## Roadmap

> Planned improvements to this library. Ideas and pull requests are welcome —
> open an issue to discuss anything here.

- [ ] Publish `vobiz` to PyPI so `pip install vobiz` works, with signed release
      artefacts and a published changelog.
- [ ] Adopt semantic versioning guarantees from `1.0.0` onward, with a documented
      deprecation window for generated method renames.
- [ ] Add auto-paging iterators for `cdr.list_cdrs` and `recordings.list_recordings`
      so callers stop hand-rolling `while` loops.
- [ ] Richer typed errors that surface the Vobiz error code and message as
      attributes rather than a raw `body` payload.
- [ ] Webhook signature verification helpers, so `answer_url` and callback handlers
      can validate that a request genuinely came from Vobiz.
- [ ] Expand the test suite beyond the transport smoke tests in [`tests/`](./tests)
      to cover the VobizXML builder and a recorded-response contract suite.
- [ ] Streaming helpers for `audio_streams`, mirroring the media-stream flow used by
      AI voice agents.

## Contributing

While we value open-source contributions to this SDK, this library is generated
programmatically. Additions made directly to this library would have to be moved
over to our generation code, otherwise they would be overwritten upon the next
generated release. Feel free to open a PR as a proof of concept, but know that we
will not be able to merge it as-is. We suggest opening an issue first to discuss
with us!

On the other hand, contributions to the README, to [`USAGE.md`](./USAGE.md) and to
the hand-written `vobiz.vobizxml` builder are always very welcome. See
[CONTRIBUTING.md](./CONTRIBUTING.md) for details.

To run the tests locally:

```sh
pip install -e . pytest
python -m pytest tests
```

## License

Released under the [MIT License](./LICENSE) © Vobiz.

MIT is permissive: you may use, modify, and redistribute this code, including in
closed-source commercial products, provided the copyright notice and licence text
are retained. There is no warranty. If your organisation needs a different
licensing arrangement, contact [piyush@vobiz.ai](mailto:piyush@vobiz.ai).

## Built by Team Vobiz

[Vobiz](https://vobiz.ai) is a programmable voice and SIP-trunking platform for
voice APIs, SIP trunking, and AI voice agents. This repository is built and
maintained by the Vobiz team.

**Maintainer:** Piyush Sahoo — [piyush@vobiz.ai](mailto:piyush@vobiz.ai) · [LinkedIn](https://www.linkedin.com/in/piyush-s713/)

Questions, or want to talk through an integration? Open an issue on this repo,
or reach out directly at [piyush@vobiz.ai](mailto:piyush@vobiz.ai).

**Useful links:** [Docs](https://docs.vobiz.ai) · [API reference](https://docs.vobiz.ai/api-reference) · [Sign up](https://vobiz.ai)
