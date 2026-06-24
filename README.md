# Vobiz Python SDK

The official Python SDK for the [Vobiz](https://vobiz.ai) voice & telephony platform.
Make and control calls, manage SIP trunks, phone numbers, conferences, recordings, and
build dynamic call flows — all from Python, with full type hints and async support.

- 📚 **Docs:** https://docs.vobiz.ai
- 🔑 **Dashboard / credentials:** https://console.vobiz.ai
- 🧾 **Full API reference:** [`reference.md`](./reference.md)
- ⚡ **Usage cheat-sheet:** [`USAGE.md`](./USAGE.md)

## Installation

Clone the repository and install it:

```sh
git clone https://github.com/vobiz-ai/Vobiz-Python-SDK.git
cd Vobiz-Python-SDK
pip install .
```

## Authentication

Every request is authenticated with your account **Auth ID** and **Auth Token**
(find them in the [dashboard](https://console.vobiz.ai)). They map to the
`X-Auth-ID` and `X-Auth-Token` headers.

```python
from vobiz import Vobiz

client = Vobiz(
    api_key="YOUR_AUTH_ID",       # X-Auth-ID
    auth_token="YOUR_AUTH_TOKEN", # X-Auth-Token
)
```

> Tip: read the credentials from environment variables (`VOBIZ_AUTH_ID`,
> `VOBIZ_AUTH_TOKEN`) instead of hard-coding them.

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

When the callee answers, Vobiz fetches `answer_url`, which should return
[VobizXML](https://docs.vobiz.ai/xml-builder) describing what happens on the call.

## Async

```python
import asyncio
from vobiz import AsyncVobiz

client = AsyncVobiz(api_key="YOUR_AUTH_ID", auth_token="YOUR_AUTH_TOKEN")

async def main() -> None:
    await client.calls.make_call(
        auth_id="YOUR_AUTH_ID", from_="14155551234", to="+919876543210",
        answer_url="https://example.com/answer", answer_method="POST",
    )

asyncio.run(main())
```

## What you can do

| Area | Client namespace |
|------|------------------|
| Make / control live calls | `client.calls`, `client.live_calls` |
| Play audio, speak text, send DTMF | `client.play_audio`, `client.speak_text`, `client.dtmf` |
| Record calls & manage recordings | `client.record_calls`, `client.recordings` |
| Call detail records | `client.cdr` |
| Phone numbers | `client.phone_numbers` |
| SIP trunks / endpoints / credentials | `client.trunks`, `client.endpoints`, `client.credentials` |
| Conferences | `client.conference`, `client.conferences`, `client.conference_members` |
| Applications | `client.applications` |
| Sub-accounts & KYC | `client.sub_accounts`, `client.sub_account_kyc` |
| Account & balance | `client.account`, `client.balance` |

See [`USAGE.md`](./USAGE.md) for copy-paste examples of each.

## Error handling

```python
from vobiz.core.api_error import ApiError

try:
    client.calls.make_call(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Retries & timeouts

Failed requests (429, 5xx, connection errors) are retried automatically with
exponential backoff. Override per call:

```python
client.calls.make_call(..., request_options={"max_retries": 5, "timeout_in_seconds": 30})
```

## License

MIT
