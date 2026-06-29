# Vobiz Python SDK

The official Python SDK for [Vobiz](https://vobiz.ai) — the AI-first voice & telephony API platform for builders. Programmatically make and control live calls, manage SIP trunks, phone numbers, conferences, and recordings, and build dynamic call flows directly from Python, with full type hints and both sync and async clients.

## Quick Links

- **Vobiz Documentation:** [https://docs.vobiz.ai](https://docs.vobiz.ai)
- **Vobiz Dashboard & Credentials:** [https://console.vobiz.ai](https://console.vobiz.ai)
- **Full API Reference:** [`./reference.md`](./reference.md)
- **Usage Cheat-Sheet:** [`./USAGE.md`](./USAGE.md)

## Features

The Vobiz Python SDK provides comprehensive access to the Vobiz API, enabling you to integrate powerful voice and telephony capabilities into your Python applications:

- **Programmatic Call Control:** Initiate outbound calls, manage live call legs, and control call flows using VobizXML.
- **SIP Trunk Management:** Create, retrieve, update, and delete SIP trunks for flexible voice routing.
- **Phone Number Management:** List, purchase, assign, and unassign phone numbers from your inventory.
- **Conference Calling:** Create and manage conference rooms, including muting/unmuting and kicking members.
- **Call Detail Records (CDRs):** Access detailed records of all calls made and received, with robust filtering and export options.
- **Call Recording:** Start and stop call recordings, and manage stored recordings.
- **In-Call Actions:** Play audio, convert text-to-speech (TTS), and send DTMF tones during live calls.
- **Real-time Audio Streaming:** Stream raw audio from live calls to WebSocket URLs for custom processing.
- **Application Management:** Create and manage applications to define call handling logic via webhooks.
- **Sub-Account & KYC Management:** Programmatically manage sub-accounts and their KYC verification processes.
- **Partner API Access:** For Vobiz partners, manage customer accounts, transfer balances, and access customer-specific CDRs and numbers.

## Requirements

The Vobiz Python SDK requires **Python 3.8** or newer.

## Installation

Install the Vobiz Python SDK using pip:

```sh
pip install vobiz
```

## Authentication

All requests to the Vobiz API require authentication using your account's **Auth ID** and **Auth Token**. These credentials are passed as `api_key` and `auth_token` respectively when initializing the Vobiz client. You can find your Auth ID and Auth Token in your [Vobiz Dashboard](https://console.vobiz.ai).

The `api_key` maps to the `X-Auth-ID` HTTP header, and `auth_token` maps to the `X-Auth-Token` HTTP header.

For production environments, it is highly recommended to load your credentials from environment variables to avoid hard-coding sensitive information directly in your codebase:

```python
import os
from vobiz import Vobiz

client = Vobiz(
    api_key=os.environ.get("VOBIZ_AUTH_ID"),
    auth_token=os.environ.get("VOBIZ_AUTH_TOKEN"),
)
```

## Quickstart — Make a Call

This example demonstrates how to initiate an outbound call using the Vobiz Python SDK. When the callee answers, Vobiz will fetch the `answer_url`, which should return [VobizXML](https://docs.vobiz.ai/xml-builder) to define the call's behavior.

```python
import os
from vobiz import Vobiz

AUTH_ID = os.environ.get("VOBIZ_AUTH_ID")

client = Vobiz(
    api_key=AUTH_ID,
    auth_token=os.environ.get("VOBIZ_AUTH_TOKEN")
)

try:
    response = client.calls.make_call(
        auth_id=AUTH_ID,
        from_="14155551234",          # Your Vobiz phone number or SIP URI
        to="+919876543210",           # Destination phone number
        answer_url="https://example.com/answer",  # URL for VobizXML instructions
        answer_method="POST",
    )
    print(f"Call initiated successfully: {response}")
except Exception as e:
    print(f"Error making call: {e}")
```

## Common Operations

Here are some common operations you can perform with the Vobiz Python SDK. For an exhaustive list of every method and parameter, see [`reference.md`](./reference.md).

### List Live Calls

Retrieve a list of all currently active (live) calls on your account.

```python
from vobiz import Vobiz

AUTH_ID = "YOUR_AUTH_ID"
client = Vobiz(api_key=AUTH_ID, auth_token="YOUR_AUTH_TOKEN")

live_calls = client.live_calls.list_live_calls(
    auth_id=AUTH_ID,
    status="live"
)

print("Live Calls:")
for call in live_calls.data:
    print(f"- Call UUID: {call.call_uuid}, From: {call.from_}, To: {call.to}")
```

### Hang Up a Live Call

Terminate an active call using its unique `call_uuid`.

```python
from vobiz import Vobiz

AUTH_ID = "YOUR_AUTH_ID"
client = Vobiz(api_key=AUTH_ID, auth_token="YOUR_AUTH_TOKEN")

client.live_calls.hangup_call(
    auth_id=AUTH_ID, 
    call_uuid="YOUR_CALL_UUID"
)
print("Call hung up successfully.")
```

### Send DTMF Tones

Send DTMF (keypad) tones on an active call. Use `w` for a 0.5-second pause and `W` for a 1-second pause.

```python
from vobiz import Vobiz

AUTH_ID = "YOUR_AUTH_ID"
client = Vobiz(api_key=AUTH_ID, auth_token="YOUR_AUTH_TOKEN")

client.dtmf.send_dtmf(
    auth_id=AUTH_ID,
    call_uuid="YOUR_CALL_UUID",
    digits="1234w5678", # Sends "1234", pauses, then sends "5678"
    leg="aleg",         # or "bleg" depending on which leg to send to
)
print("DTMF tones sent.")
```

### Convert Text-to-Speech (TTS)

Convert text to speech and play it on a live call.

```python
from vobiz import Vobiz

AUTH_ID = "YOUR_AUTH_ID"
client = Vobiz(api_key=AUTH_ID, auth_token="YOUR_AUTH_TOKEN")

client.speak_text.call(
    auth_id=AUTH_ID,
    call_uuid="YOUR_CALL_UUID",
    text="Hello, your appointment is confirmed for tomorrow at 3 PM.",
    voice="WOMAN",
    language="en-US",
)
print("TTS playback initiated.")
```

### List Recordings

Retrieve a list of all call recordings associated with your account.

```python
from vobiz import Vobiz

AUTH_ID = "YOUR_AUTH_ID"
client = Vobiz(api_key=AUTH_ID, auth_token="YOUR_AUTH_TOKEN")

recordings = client.recordings.list_recordings(
    auth_id=AUTH_ID,
    limit=50
)

print("Recordings:")
for recording in recordings.data:
    print(f"- Recording ID: {recording.recording_id}, Duration: {recording.duration}s")
```

## Configuration

The Vobiz client can be configured with various options during initialization:

- `api_key` (str): Your Vobiz Auth ID.
- `auth_token` (str): Your Vobiz Auth Token.
- `environment` (VobizEnvironment): Specifies the Vobiz API environment (e.g., `VobizEnvironment.PRODUCTION`).
- `base_url` (str): Override the default base URL for the API.
- `timeout` (float): Request timeout in seconds.
- `max_retries` (int): Maximum number of retries for failed requests.

Example with custom configuration:

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="YOUR_AUTH_ID",
    auth_token="YOUR_AUTH_TOKEN",
    environment=VobizEnvironment.PRODUCTION,
    timeout=30.0,  # 30-second timeout
    max_retries=2, # Retry failed requests up to 2 times
)
```

## Error Handling

The Vobiz Python SDK raises `ApiError` for failed HTTP requests. This exception provides access to the HTTP status code and the response body, allowing you to handle API-specific errors gracefully.

```python
from vobiz.core.api_error import ApiError
from vobiz import Vobiz

client = Vobiz(api_key="YOUR_AUTH_ID", auth_token="YOUR_AUTH_TOKEN")

try:
    client.calls.make_call(
        auth_id="YOUR_AUTH_ID",
        from_="14155551234",
        to="+919876543210",
        answer_url="https://example.com/answer",
        answer_method="POST",
    )
except ApiError as e:
    print(f"API Error occurred! Status Code: {e.status_code}")
    print(f"Error Body: {e.body}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

## Async Client

The SDK provides an asynchronous client, `AsyncVobiz`, which can be used in `asyncio` environments for non-blocking operations. It shares the exact same interface and configuration options as the synchronous client.

```python
import asyncio
from vobiz import AsyncVobiz

async def main():
    client = AsyncVobiz(
        api_key="YOUR_AUTH_ID",
        auth_token="YOUR_AUTH_TOKEN"
    )
    
    try:
        response = await client.calls.make_call(
            auth_id="YOUR_AUTH_ID",
            from_="14155551234",
            to="+919876543210",
            answer_url="https://example.com/answer",
            answer_method="POST",
        )
        print(response)
    except Exception as e:
        print(f"Async call failed: {e}")

asyncio.run(main())
```

## Other Vobiz SDKs

If you are building in languages other than Python, Vobiz provides official SDKs for several other runtimes:

| Language | Repository |
| --- | --- |
| **TypeScript / Node.js** | [vobiz-ai/Vobiz-Node-SDK](https://github.com/vobiz-ai/Vobiz-Node-SDK) |
| **Go** | [vobiz-ai/Vobiz-Go-SDK](https://github.com/vobiz-ai/Vobiz-Go-SDK) |
| **Ruby** | [vobiz-ai/Vobiz-Ruby-SDK](https://github.com/vobiz-ai/Vobiz-Ruby-SDK) |
| **C#** | [vobiz-ai/Vobiz-Csharp-sdk](https://github.com/vobiz-ai/Vobiz-Csharp-sdk) |
| **Java** | [vobiz-ai/Vobiz-Java-SDK](https://github.com/vobiz-ai/Vobiz-Java-SDK) |
| **PHP** | [vobiz-ai/Vobiz-PHP-SDK](https://github.com/vobiz-ai/Vobiz-PHP-SDK) |

## Support

- **Documentation:** [https://docs.vobiz.ai](https://docs.vobiz.ai)
- **Console & Dashboard:** [https://console.vobiz.ai](https://console.vobiz.ai)

## License

This SDK is distributed under the [MIT License](LICENSE).
