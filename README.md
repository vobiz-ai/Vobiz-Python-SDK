# Vobiz Python SDK

The official Python SDK for [Vobiz](https://vobiz.ai) — the AI-first voice & telephony API platform for builders. Make and control live calls, manage SIP trunks, phone numbers, conferences, and recordings, and build dynamic call flows directly from Python, with full type hints and both sync and async clients.

- **Docs:** https://docs.vobiz.ai
- **Dashboard & credentials:** https://console.vobiz.ai
- **Full API reference:** [`./reference.md`](./reference.md)
- **Usage cheat-sheet:** [`./USAGE.md`](./USAGE.md)

## Installation

```sh
pip install vobiz
```

Requires Python 3.8+.

## Authentication

Every request is authenticated with your account **Auth ID** and **Auth Token** (find them in the [dashboard](https://console.vobiz.ai)). They map to the `X-Auth-ID` and `X-Auth-Token` headers.

```python
from vobiz import Vobiz

client = Vobiz(
    api_key="YOUR_AUTH_ID",        # X-Auth-ID
    auth_token="YOUR_AUTH_TOKEN",  # X-Auth-Token
)
```

We recommend loading credentials from environment variables rather than hard-coding them:

```python
import os
from vobiz import Vobiz

client = Vobiz(
    api_key=os.environ["VOBIZ_AUTH_ID"],
    auth_token=os.environ["VOBIZ_AUTH_TOKEN"],
)
```

## Quickstart — make a call

```python
from vobiz import Vobiz

client = Vobiz(api_key="YOUR_AUTH_ID", auth_token="YOUR_AUTH_TOKEN")

response = client.calls.make_call(
    auth_id="YOUR_AUTH_ID",
    from_="14155551234",
    to="+919876543210",
    answer_url="https://example.com/answer",  # returns VobizXML
    answer_method="POST",
)
print(response)
```

When the callee answers, Vobiz fetches `answer_url`, which should return [VobizXML](https://docs.vobiz.ai/xml-builder) describing what happens on the call.

## Async

Every method is also available on the async client, `AsyncVobiz`:

```python
import asyncio
from vobiz import AsyncVobiz

client = AsyncVobiz(api_key="YOUR_AUTH_ID", auth_token="YOUR_AUTH_TOKEN")

async def main() -> None:
    response = await client.calls.make_call(
        auth_id="YOUR_AUTH_ID",
        from_="14155551234",
        to="+919876543210",
        answer_url="https://example.com/answer",
        answer_method="POST",
    )
    print(response)

asyncio.run(main())
```

## Error handling

Failed requests raise `ApiError`, which exposes the HTTP status code and response body:

```python
from vobiz.core.api_error import ApiError

try:
    client.calls.make_call(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Other SDKs

Vobiz publishes official SDKs for every major language under [github.com/vobiz-ai](https://github.com/vobiz-ai):

| Language   | Repository |
|------------|------------|
| TypeScript | [Vobiz-Node-SDK](https://github.com/vobiz-ai/Vobiz-Node-SDK) |
| Go         | [Vobiz-Go-SDK](https://github.com/vobiz-ai/Vobiz-Go-SDK) |
| Java       | [Vobiz-Java-SDK](https://github.com/vobiz-ai/Vobiz-Java-SDK) |
| Ruby       | [Vobiz-Ruby-SDK](https://github.com/vobiz-ai/Vobiz-Ruby-SDK) |
| C#         | [Vobiz-Csharp-sdk](https://github.com/vobiz-ai/Vobiz-Csharp-sdk) |
| PHP        | [Vobiz-PHP-SDK](https://github.com/vobiz-ai/Vobiz-PHP-SDK) |

## License

MIT
