# Reference
## Account
<details><summary><code>client.account.<a href="src/vobiz/account/client.py">retrieve_account</a>() -> RetrieveAccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve complete account details including pricing tier and credentials.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.account.retrieve_account()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.account.<a href="src/vobiz/account/client.py">get_concurrency</a>(...) -> GetConcurrencyResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the current concurrent call usage and configured limits.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.account.get_concurrency(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Balance
<details><summary><code>client.balance.<a href="src/vobiz/balance/client.py">get_balance</a>(...) -> GetBalanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the current account balance for a specific currency.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.balance.get_balance(
    auth_id="MA_XXXXXX",
    currency="INR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — Currency code (e.g. INR, USD)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.balance.<a href="src/vobiz/balance/client.py">list_transactions</a>(...) -> ListTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve paginated transaction history for the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.balance.list_transactions(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Live Calls
<details><summary><code>client.live_calls.<a href="src/vobiz/live_calls/client.py">list_queued_calls</a>(...) -> ListQueuedCallsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all queued (pending, not yet connected) calls on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.live_calls.list_queued_calls(
    auth_id="MA_XXXXXX",
    status="live",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `ListQueuedCallsRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_calls.<a href="src/vobiz/live_calls/client.py">list_live_calls</a>(...) -> ListLiveCallsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all currently active (live) calls on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.live_calls.list_live_calls(
    auth_id="MA_XXXXXX",
    status="live",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**status:** `ListLiveCallsRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_calls.<a href="src/vobiz/live_calls/client.py">get_live_call</a>(...) -> GetLiveCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific live or queued call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.live_calls.get_live_call(
    auth_id="MA_XXXXXX",
    call_uuid="cdr_XXXXXXXXXX",
    status="live",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetLiveCallRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_calls.<a href="src/vobiz/live_calls/client.py">hangup_call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate an active call by its UUID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.live_calls.hangup_call(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.live_calls.<a href="src/vobiz/live_calls/client.py">get_queued_call</a>(...) -> GetQueuedCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific queued (pending) call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.live_calls.get_queued_call(
    auth_id="MA_XXXXXX",
    call_uuid="cdr_XXXXXXXXXX",
    status="live",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetQueuedCallRequestStatus` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Calls
<details><summary><code>client.calls.<a href="src/vobiz/calls/client.py">make_call</a>(...) -> MakeCallResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiate an outbound call to a PSTN number or SIP endpoint.
Use `<` to separate multiple destinations (max 1000).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.calls.make_call(
    auth_id="MA_XXXXXX",
    from_="14155551234",
    to="+919876543210",
    answer_url="https://example.com/answer",
    answer_method="POST",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**from:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**answer_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**answer_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## CDR
<details><summary><code>client.cdr.<a href="src/vobiz/cdr/client.py">list_cdrs</a>(...) -> ListCdrsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all CDRs for your account. Supports filtering by phone numbers,
date range, call direction, duration, and pagination.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment
import datetime

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.cdr.list_cdrs(
    auth_id="MA_XXXXXX",
    from_number="9876543210",
    to_number="1234567890",
    start_date=datetime.date.fromisoformat("2026-03-01"),
    end_date=datetime.date.fromisoformat("2026-03-17"),
    min_duration=10,
    sip_call_id="dD1qwu5VZ5iK3ed5u3uspjY5RKL",
    bridge_uuid="4b7ae653-f40d-42f1-b582-6b05dfcd0c0a",
    hangup_cause="NORMAL_CLEARING",
    hangup_disposition="send_refuse",
    context="sip-trunking",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**from_number:** `typing.Optional[str]` — Filter by the originating phone number (caller).
    
</dd>
</dl>

<dl>
<dd>

**to_number:** `typing.Optional[str]` — Filter by the destination phone number (callee).
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Beginning of the search period (YYYY-MM-DD). Required when using `end_date`.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End of the search period (YYYY-MM-DD). Required when using `start_date`.
    
</dd>
</dl>

<dl>
<dd>

**call_direction:** `typing.Optional[ListCdrsRequestCallDirection]` — Filter by direction.
    
</dd>
</dl>

<dl>
<dd>

**min_duration:** `typing.Optional[int]` — Minimum call duration in seconds. Excludes calls shorter than this value.
    
</dd>
</dl>

<dl>
<dd>

**sip_call_id:** `typing.Optional[str]` — Filter by the SIP Call-ID of the call (matches the cdr's sip_call_id field).
    
</dd>
</dl>

<dl>
<dd>

**bridge_uuid:** `typing.Optional[str]` — Filter by the UUID of the bridged leg (matches the cdr's bridge_uuid field).
    
</dd>
</dl>

<dl>
<dd>

**hangup_cause:** `typing.Optional[str]` — Filter by telephony hangup cause, e.g. NORMAL_CLEARING.
    
</dd>
</dl>

<dl>
<dd>

**hangup_disposition:** `typing.Optional[str]` — Filter by how the leg was released, e.g. send_refuse.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — Filter by the call context, e.g. sip-trunking.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Filter by the campaign identifier associated with the call.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Free-text search across CDR fields (numbers, IDs, etc.).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for paginated results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of records per page. Max: 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cdr.<a href="src/vobiz/cdr/client.py">search_cdrs</a>(...) -> SearchCdrsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Identical filters to the list endpoint, but the response also includes a
`filter_summary` object describing the active filters applied.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment
import datetime

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.cdr.search_cdrs(
    auth_id="MA_XXXXXX",
    from_number="9876543210",
    to_number="1234567890",
    start_date=datetime.date.fromisoformat("2026-03-01"),
    end_date=datetime.date.fromisoformat("2026-03-17"),
    min_duration=10,
    sip_call_id="dD1qwu5VZ5iK3ed5u3uspjY5RKL",
    bridge_uuid="4b7ae653-f40d-42f1-b582-6b05dfcd0c0a",
    hangup_cause="NORMAL_CLEARING",
    hangup_disposition="send_refuse",
    context="sip-trunking",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**from_number:** `typing.Optional[str]` — Filter by the originating phone number (caller).
    
</dd>
</dl>

<dl>
<dd>

**to_number:** `typing.Optional[str]` — Filter by the destination phone number (callee).
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Beginning of the search period (YYYY-MM-DD). Required when using `end_date`.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End of the search period (YYYY-MM-DD). Required when using `start_date`.
    
</dd>
</dl>

<dl>
<dd>

**call_direction:** `typing.Optional[SearchCdrsRequestCallDirection]` — Filter by direction.
    
</dd>
</dl>

<dl>
<dd>

**min_duration:** `typing.Optional[int]` — Minimum call duration in seconds. Excludes calls shorter than this value.
    
</dd>
</dl>

<dl>
<dd>

**sip_call_id:** `typing.Optional[str]` — Filter by the SIP Call-ID of the call (matches the cdr's sip_call_id field).
    
</dd>
</dl>

<dl>
<dd>

**bridge_uuid:** `typing.Optional[str]` — Filter by the UUID of the bridged leg (matches the cdr's bridge_uuid field).
    
</dd>
</dl>

<dl>
<dd>

**hangup_cause:** `typing.Optional[str]` — Filter by telephony hangup cause, e.g. NORMAL_CLEARING.
    
</dd>
</dl>

<dl>
<dd>

**hangup_disposition:** `typing.Optional[str]` — Filter by how the leg was released, e.g. send_refuse.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — Filter by the call context, e.g. sip-trunking.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Filter by the campaign identifier associated with the call.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Free-text search across CDR fields (numbers, IDs, etc.).
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number for paginated results.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of records per page. Max: 100.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cdr.<a href="src/vobiz/cdr/client.py">list_recent_cdrs</a>(...) -> ListRecentCdrsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the most recent CDRs for your account without requiring a date range.
Default 20 records; use `limit` to retrieve more.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.cdr.list_recent_cdrs(
    auth_id="MA_XXXXXX",
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of recent CDRs to return.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cdr.<a href="src/vobiz/cdr/client.py">export_cdrs</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns CDR data as a downloadable CSV file. Same filters as the list endpoint.

**Note:** Do NOT send `Accept: application/json` on this endpoint - the response is `text/csv`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
client.cdr.export_cdrs(...)
```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**from_number:** `typing.Optional[str]` — Filter by the originating phone number (caller).
    
</dd>
</dl>

<dl>
<dd>

**to_number:** `typing.Optional[str]` — Filter by the destination phone number (callee).
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` — Beginning of the search period (YYYY-MM-DD). Required when using `end_date`.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` — End of the search period (YYYY-MM-DD). Required when using `start_date`.
    
</dd>
</dl>

<dl>
<dd>

**call_direction:** `typing.Optional[ExportCdrsRequestCallDirection]` — Filter by direction.
    
</dd>
</dl>

<dl>
<dd>

**min_duration:** `typing.Optional[int]` — Minimum call duration in seconds. Excludes calls shorter than this value.
    
</dd>
</dl>

<dl>
<dd>

**sip_call_id:** `typing.Optional[str]` — Filter by the SIP Call-ID of the call (matches the cdr's sip_call_id field).
    
</dd>
</dl>

<dl>
<dd>

**bridge_uuid:** `typing.Optional[str]` — Filter by the UUID of the bridged leg (matches the cdr's bridge_uuid field).
    
</dd>
</dl>

<dl>
<dd>

**hangup_cause:** `typing.Optional[str]` — Filter by telephony hangup cause, e.g. NORMAL_CLEARING.
    
</dd>
</dl>

<dl>
<dd>

**hangup_disposition:** `typing.Optional[str]` — Filter by how the leg was released, e.g. send_refuse.
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — Filter by the call context, e.g. sip-trunking.
    
</dd>
</dl>

<dl>
<dd>

**campaign_id:** `typing.Optional[str]` — Filter by the campaign identifier associated with the call.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Free-text search across CDR fields (numbers, IDs, etc.).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.cdr.<a href="src/vobiz/cdr/client.py">get_cdr</a>(...) -> GetCdrResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the CDR for a specific completed call using its `call_id`.
Useful when you have a `call_id` from a callback or previous API response.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.cdr.get_cdr(
    auth_id="MA_XXXXXX",
    call_id="abc123-def456-ghi789",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_id:** `str` — The unique call ID of the completed call.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sub-Accounts
<details><summary><code>client.sub_accounts.<a href="src/vobiz/sub_accounts/client.py">list_subaccounts</a>(...) -> ListSubaccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all sub-accounts under the master account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_accounts.list_subaccounts(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_accounts.<a href="src/vobiz/sub_accounts/client.py">create_subaccount</a>(...) -> CreateSubaccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new sub-account under the master account.

Set `kyc_mode` to control how the sub-account is verified:

- `personal_use` *(default)* — the sub-account inherits the parent's
  KYC; no separate verification is required.
- `customer_use` — the sub-account must complete its own KYC before it
  can place calls. A fresh `customer_use` sub-account is returned with
  `kyc_calls_blocked: true`. `customer_use` **requires** `email`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_accounts.create_subaccount(
    auth_id="MA_XXXXXX",
    name="Customer Co",
    email="customer@example.com",
    password="Customer@12345",
    kyc_mode="customer_use",
    business_type="private_limited",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for the sub-account.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Required when `kyc_mode` is `customer_use`.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Login password for the sub-account.
    
</dd>
</dl>

<dl>
<dd>

**kyc_mode:** `typing.Optional[CreateSubaccountRequestKycMode]` 

`personal_use` inherits parent KYC. `customer_use` requires
the sub-account to complete its own KYC and requires `email`.
    
</dd>
</dl>

<dl>
<dd>

**business_type:** `typing.Optional[CreateSubaccountRequestBusinessType]` — Legal constitution of the customer. Drives which KYC documents are required.
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_accounts.<a href="src/vobiz/sub_accounts/client.py">retrieve_subaccount</a>(...) -> RetrieveSubaccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve details of a specific sub-account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_accounts.retrieve_subaccount(
    auth_id="MA_XXXXXX",
    sub_auth_id="SA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**sub_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_accounts.<a href="src/vobiz/sub_accounts/client.py">update_subaccount</a>(...) -> UpdateSubaccountResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the name or status of a sub-account, or change its `kyc_mode`.

Promoting an existing sub-account to `customer_use` requires the
sub-account to already have an `email` (otherwise `400`). On any
`kyc_mode` change, `kyc_calls_blocked` is re-derived from the
sub-account's current KYC state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_accounts.update_subaccount(
    auth_id="MA_XXXXXX",
    sub_auth_id="sub_auth_id",
    kyc_mode="customer_use",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**sub_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**kyc_mode:** `typing.Optional[UpdateSubaccountRequestKycMode]` — Change the verification mode. Promoting to `customer_use` requires the sub-account to have an `email`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_accounts.<a href="src/vobiz/sub_accounts/client.py">delete_subaccount</a>(...) -> typing.Optional[DeleteSubaccountResponse]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a sub-account and revoke its credentials.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_accounts.delete_subaccount(
    auth_id="MA_XXXXXX",
    sub_auth_id="sub_auth_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**sub_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sub-Account KYC
<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">get_subaccount_kyc_status</a>(...) -> SubAccountKycStatus</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the aggregated KYC state for a `customer_use` sub-account —
which verifications have passed, whether calls are still blocked, and
the business type. The caller must be the parent main account that owns
the sub-account (or an admin).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.get_subaccount_kyc_status(
    sub_auth_id="SA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">verify_subaccount_pan</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a real PAN verification (Perfios) for the sub-account. `pan` must
be exactly 10 characters. Persists a `kyc_verifications` row and
recomputes the sub-account's aggregated `kyc_status`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.verify_subaccount_pan(
    sub_auth_id="SA_XXXXXX",
    pan="ABCDE1234F",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**pan:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">verify_subaccount_gst</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Runs a real GSTIN verification. `gstin` must be a 15-character GSTIN.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.verify_subaccount_gst(
    sub_auth_id="SA_XXXXXX",
    gstin="29AAJCN5983D1Z0",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**gstin:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">search_subaccount_cin</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Name-based CIN lookup. Returns candidate company matches; pick one and
pass it to [CIN confirm](#operation/confirm-subaccount-cin).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.search_subaccount_cin(
    sub_auth_id="SA_XXXXXX",
    company_name="ACME PRIVATE LIMITED",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">confirm_subaccount_cin</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Confirm the CIN selected from the search results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.confirm_subaccount_cin(
    sub_auth_id="SA_XXXXXX",
    company_name="ACME PRIVATE LIMITED",
    selected_cin="U72900KA2024PTC123456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**selected_cin:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">subaccount_digilocker_initiate</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the DigiLocker authorization link and an `access_request_id`.
The customer completes the OAuth flow on the DigiLocker portal, after
which you finalize with
[DigiLocker verify](#operation/subaccount-digilocker-verify).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.subaccount_digilocker_initiate(
    sub_auth_id="SA_XXXXXX",
    redirect_url="https://partner.example.com/kyc/callback",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**oauth_state:** `typing.Optional[str]` — Opaque value echoed back on the redirect for CSRF protection.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">subaccount_digilocker_verify</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Finalize Aadhaar via DigiLocker after the customer completes OAuth.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.subaccount_digilocker_verify(
    sub_auth_id="SA_XXXXXX",
    access_request_id="AR_xxxxxxxx",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**access_request_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**linked_number:** `typing.Optional[str]` — Optional. Binds the Aadhaar to a specific number (92-series).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc.<a href="src/vobiz/sub_account_kyc/client.py">create_subaccount_kyc_session</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a Vobiz-hosted KYC session for the sub-account. With
`flow_type=email` (default) Vobiz emails the customer a signed link
(from `kyc@vobiz.ai`, hosted at `kyc.vobiz.ai`) and `customer_email` is
required. With `flow_type=redirect`, omit `customer_email`, pass a
`redirect_url`, and the `widget_url` is returned directly for an inline
redirect.

This is the sub-account–scoped equivalent of the partner-level
[KYC Sessions](/partner/api/kyc-sessions) endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc.create_subaccount_kyc_session(
    sub_auth_id="SA_XXXXXX",
    account_auth_id="SA_XXXXXX",
    flow_type="email",
    customer_email="customer@example.com",
    webhook_url="https://your-app.example.com/kyc/webhook",
    expires_in_days=30,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**account_auth_id:** `str` — The sub-account's auth_id (typically equal to the path `sub_auth_id`).
    
</dd>
</dl>

<dl>
<dd>

**flow_type:** `CreateSubaccountKycSessionRequestFlowType` 
    
</dd>
</dl>

<dl>
<dd>

**customer_email:** `typing.Optional[str]` — Required when `flow_type` is `email`.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 

Required when `flow_type` is `redirect`. After verification the customer's
browser is sent to this URL.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — HTTPS endpoint VoBiz POSTs the KYC result to. Omit it and no callbacks are sent.
    
</dd>
</dl>

<dl>
<dd>

**expires_in_days:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sub-Account KYC (Test Mode)
<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_verify_subaccount_pan</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mock PAN verification — never hits the provider. Magic `pan` inputs:

| Input | Outcome |
|---|---|
| `TESTSUCCESS0001` | verified |
| `TESTFAIL0001` | failed |
| `TESTERROR0001` | HTTP 500 |
| `TESTPENDING001` | pending (finalize as verified) |
| `TESTPENDING_FAIL` | pending (finalize as failed) |

Persists a real `kyc_verifications` row and recomputes `kyc_status`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_verify_subaccount_pan(
    sub_auth_id="SA_XXXXXX",
    pan="TESTSUCCESS0001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**pan:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_verify_subaccount_gst</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mock GST verification. Same magic-input matrix as [Mock verify PAN](#operation/mock-verify-subaccount-pan).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_verify_subaccount_gst(
    sub_auth_id="SA_XXXXXX",
    gstin="TESTSUCCESS0001GST",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**gstin:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_search_subaccount_cin</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns deterministic fake company matches.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_search_subaccount_cin(
    sub_auth_id="SA_XXXXXX",
    company_name="ACME",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_confirm_subaccount_cin</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Succeeds when `selected_cin` starts with `U72900KA2024PTC123456`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_confirm_subaccount_cin(
    sub_auth_id="SA_XXXXXX",
    company_name="ACME",
    selected_cin="U72900KA2024PTC123456",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**company_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**selected_cin:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_subaccount_digilocker_initiate</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a deterministic `access_request_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_subaccount_digilocker_initiate(
    sub_auth_id="SA_XXXXXX",
    redirect_url="https://partner.example.com/kyc/callback",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_subaccount_digilocker_verify</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

`access_request_id` `MOCK_AR_SUCCESS` → verified; `MOCK_AR_FAIL` → failed.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_subaccount_digilocker_verify(
    sub_auth_id="SA_XXXXXX",
    access_request_id="MOCK_AR_SUCCESS",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**access_request_id:** `MockSubaccountDigilockerVerifyRequestAccessRequestId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sub_account_kyc_test_mode.<a href="src/vobiz/sub_account_kyc_test_mode/client.py">mock_finalize_pending_kyc</a>(...) -> KycVerificationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Promotes the most recent **pending** mock verification of the given
type to a terminal outcome — this drives the async (`TESTPENDING…`)
path without webhooks. `verification_type` ∈ `pan | aadhaar | gst | cin`;
`outcome` ∈ `verified | failed`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sub_account_kyc_test_mode.mock_finalize_pending_kyc(
    sub_auth_id="SA_XXXXXX",
    verification_type="pan",
    outcome="verified",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sub_auth_id:** `str` — The sub-account's Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**verification_type:** `MockFinalizePendingKycRequestVerificationType` 
    
</dd>
</dl>

<dl>
<dd>

**outcome:** `MockFinalizePendingKycRequestOutcome` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Phone Numbers
<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">list_numbers</a>(...) -> ListNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all phone numbers on your account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.list_numbers(
    auth_id="MA_XXXXXX",
    search="+919876543210",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Page number, starting at 1
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Number of phone numbers to return per page
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filter by phone number. Include the country code and URL-encode a leading plus sign.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">unrent_number</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Release a phone number from your account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.unrent_number(
    auth_id="MA_XXXXXX",
    e164="919876543210",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**e164:** `str` — Phone number in E.164 format (without the +)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">list_inventory_numbers</a>(...) -> ListInventoryNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Browse available phone numbers in inventory that are not assigned to
any account. Only numbers with `status='active'` and `auth_id=NULL`
are returned. These numbers are ready to be purchased.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.list_inventory_numbers(
    auth_id="MA_XXXXXX",
    country="IN",
    exclude="9180,9192",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**country:** `typing.Optional[str]` — Filter by country code (e.g., "US", "IN").
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Substring match against the E.164 number (e.g., "80" matches "+918065...").
    
</dd>
</dl>

<dl>
<dd>

**exclude:** `typing.Optional[str]` — One or more E.164 prefixes to remove from results. Include the country code (e.g. "9180" for India +91 80-series, "1415" for US +1 415); a leading "+" is optional. Matched against the full E.164 form, so it works for any country. Accepts a comma-separated list ("9180,9192") or repeated params ("exclude=9180&exclude=9192"), and the two forms can be combined. It is ANDed with all other filters, so it takes priority over `search`; duplicates are de-duplicated silently and `total` reflects the filtered result set.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">purchase_from_inventory</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purchase a phone number from inventory and assign it to your account.
Debits your account balance for the setup fee and monthly fee. For
sub-accounts (SA_), the parent master account (MA_) is charged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.purchase_from_inventory(
    auth_id="MA_XXXXXX",
    e164="+919876543210",
    currency="USD",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**e164:** `str` — Phone number to purchase in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency for transaction. Defaults to the number's currency or "USD".
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">assign_number_to_trunk</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign a phone number to a specific SIP trunk. Once assigned, all
inbound calls to that phone number will be routed through the
designated trunk. The phone number must be URL-encoded; use `%2B`
instead of `+` (e.g., `%2B912271264217`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.assign_number_to_trunk(
    auth_id="MA_XXXXXX",
    phone_number="%2B912271264217",
    trunk_group_id="e3e55a78-1234-5678-90ab-cdef12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — The phone number to assign, URL-encoded (use %2B instead of +).
    
</dd>
</dl>

<dl>
<dd>

**trunk_group_id:** `str` — The UUID of the trunk to assign this number to.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">unassign_number_from_trunk</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the assignment between a phone number and a SIP trunk. After
unassignment, the number remains in your account inventory but will
no longer route inbound calls through the previously assigned trunk.
URL-encode the phone number (use `%2B` instead of `+`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.unassign_number_from_trunk(
    auth_id="MA_XXXXXX",
    phone_number="%2B912271264217",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**phone_number:** `str` — The phone number to unassign, URL-encoded (use %2B instead of +).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">get_number_health</a>(...) -> GetNumberHealthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the health & analytics dashboard for one of your numbers: current
status, spam flag, and call metrics over the selected window (total and
answered calls, answer rate, minutes, average duration) plus a per-period
time series of snapshots.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.get_number_health(
    auth_id="MA_XXXXXX",
    e164="%2B919876543210",
    days=30,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**e164:** `str` — The number in E.164, URL-encoded (use %2B instead of +).
    
</dd>
</dl>

<dl>
<dd>

**granularity:** `typing.Optional[GetNumberHealthRequestGranularity]` — Snapshot granularity.
    
</dd>
</dl>

<dl>
<dd>

**days:** `typing.Optional[int]` — Size of the window (in days) for the summary and snapshots.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">assign_did_to_subaccount</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assign a parent-pool DID to a sub-account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.assign_did_to_subaccount(
    auth_id="MA_XXXXXX",
    e164="%2B919876543210",
    sub_account_id="SA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**e164:** `str` — The number in E.164, URL-encoded (use %2B instead of +).
    
</dd>
</dl>

<dl>
<dd>

**sub_account_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">unassign_did_from_subaccount</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Move the DID back to the parent pool.

A **15-day cool-off** is enforced: if the DID had a call within the last
15 days, the request is rejected with `409` and a
`did_cool_off_in_effect` error that includes `cool_off_until` and
`cool_off_remaining_seconds`. Never-used DIDs (`last_call_at` is `NULL`)
move back immediately.

Admins can bypass the cool-off with `?force=true` (see below); the
bypass writes a `did_assignment_audit` row and requires an
admin-role account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.phone_numbers.unassign_did_from_subaccount(
    auth_id="MA_XXXXXX",
    e164="%2B919876543210",
    force=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**e164:** `str` — The number in E.164, URL-encoded (use %2B instead of +).
    
</dd>
</dl>

<dl>
<dd>

**force:** `typing.Optional[bool]` 

Admin-only cool-off bypass. Requires an admin-role account
(enforced at the gateway) and writes a `did_assignment_audit` row.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Trunks
<details><summary><code>client.trunks.<a href="src/vobiz/trunks/client.py">list_trunks</a>(...) -> ListTrunksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all SIP trunks configured on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.trunks.list_trunks(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trunks.<a href="src/vobiz/trunks/client.py">create_trunk</a>(...) -> CreateTrunkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new SIP trunk for inbound or outbound calling.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.trunks.create_trunk(
    auth_id="MA_XXXXXX",
    name="Retell AI SIP",
    trunk_direction="outbound",
    transport="udp",
    concurrent_calls_limit=50,
    cps_limit=15,
    credential_uuid="b1e2...",
    ipacl_uuid="c3d4...",
    recording=True,
    enable_transcription=True,
    webhook_url="https://example.com/vobiz/webhook",
    webhook_method="POST",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Trunk name.
    
</dd>
</dl>

<dl>
<dd>

**trunk_direction:** `typing.Optional[CreateTrunkRequestTrunkDirection]` — Direction of the trunk — **`inbound` or `outbound` only** (a trunk is one direction, not both).
    
</dd>
</dl>

<dl>
<dd>

**trunk_status:** `typing.Optional[CreateTrunkRequestTrunkStatus]` — Trunk status — `enabled` or `disabled` (note: not `active`).
    
</dd>
</dl>

<dl>
<dd>

**secure:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**trunk_domain:** `typing.Optional[str]` — SIP domain. Auto-generated as `{first8ofUUID}.sip.vobiz.ai` if omitted.
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[CreateTrunkRequestTransport]` 
    
</dd>
</dl>

<dl>
<dd>

**inbound_destination:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**concurrent_calls_limit:** `typing.Optional[int]` — Stored on the trunk. The **enforced** concurrency limit is account-level (account base + channel subscriptions), not this field.
    
</dd>
</dl>

<dl>
<dd>

**cps_limit:** `typing.Optional[int]` — Stored on the trunk. The **enforced** CPS is account-level, not this field.
    
</dd>
</dl>

<dl>
<dd>

**credential_uuid:** `typing.Optional[str]` — Attach an existing SIP credential (username / password / realm) by UUID.
    
</dd>
</dl>

<dl>
<dd>

**ipacl_uuid:** `typing.Optional[str]` — Attach an existing IP access-control list (IP-based auth) by UUID.
    
</dd>
</dl>

<dl>
<dd>

**primary_uri_uuid:** `typing.Optional[str]` — Primary origination URI UUID.
    
</dd>
</dl>

<dl>
<dd>

**fallback_uri_uuid:** `typing.Optional[str]` — Fallback origination URI UUID.
    
</dd>
</dl>

<dl>
<dd>

**recording:** `typing.Optional[bool]` — Enable call recording.
    
</dd>
</dl>

<dl>
<dd>

**enable_transcription:** `typing.Optional[bool]` — Auto-transcribe recordings when `recording=true`.
    
</dd>
</dl>

<dl>
<dd>

**pii_redaction:** `typing.Optional[bool]` — Redact PII from transcriptions.
    
</dd>
</dl>

<dl>
<dd>

**pii_entity_types:** `typing.Optional[str]` — Comma-separated list of entity types to redact.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` 

Customer webhook for call-admission events (`CallInitiated` / `Hangup`).
Must be a valid **public** http/https URL. SSRF-validated — localhost,
private (RFC1918), and cloud-metadata (`169.254.169.254`) URLs are
rejected with `invalid webhook_url`. See [Trunk Webhooks](/trunks/webhook).
    
</dd>
</dl>

<dl>
<dd>

**webhook_method:** `typing.Optional[CreateTrunkRequestWebhookMethod]` — HTTP method for the webhook callback.
    
</dd>
</dl>

<dl>
<dd>

**recording_webhook_enabled:** `typing.Optional[bool]` — Fire a `recording.completed` webhook to `webhook_url` after a recording is saved.
    
</dd>
</dl>

<dl>
<dd>

**username:** `typing.Optional[str]` — Deprecated — use `credential_uuid`.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Deprecated — use `credential_uuid`.
    
</dd>
</dl>

<dl>
<dd>

**ip_whitelist:** `typing.Optional[typing.List[str]]` — Deprecated — use `ipacl_uuid`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trunks.<a href="src/vobiz/trunks/client.py">retrieve_trunk</a>(...) -> RetrieveTrunkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific SIP trunk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.trunks.retrieve_trunk(
    auth_id="MA_XXXXXX",
    trunk_id="trunk_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**trunk_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trunks.<a href="src/vobiz/trunks/client.py">update_trunk</a>(...) -> UpdateTrunkResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update a SIP trunk's name, configuration, or status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.trunks.update_trunk(
    auth_id="MA_XXXXXX",
    trunk_id="trunk_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**trunk_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**trunk_direction:** `typing.Optional[UpdateTrunkRequestTrunkDirection]` — Direction of the trunk — `inbound` or `outbound` only.
    
</dd>
</dl>

<dl>
<dd>

**trunk_status:** `typing.Optional[UpdateTrunkRequestTrunkStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**secure:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**trunk_domain:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**transport:** `typing.Optional[UpdateTrunkRequestTransport]` 
    
</dd>
</dl>

<dl>
<dd>

**inbound_destination:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**concurrent_calls_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**cps_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**credential_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**ipacl_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**primary_uri_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**fallback_uri_uuid:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**recording:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**enable_transcription:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pii_redaction:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**pii_entity_types:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — Customer webhook for call-admission events (`CallInitiated` / `Hangup`). Public http/https URL; SSRF-validated. See [Trunk Webhooks](/trunks/webhook).
    
</dd>
</dl>

<dl>
<dd>

**webhook_method:** `typing.Optional[UpdateTrunkRequestWebhookMethod]` 
    
</dd>
</dl>

<dl>
<dd>

**recording_webhook_enabled:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.trunks.<a href="src/vobiz/trunks/client.py">delete_trunk</a>(...) -> typing.Optional[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a SIP trunk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.trunks.delete_trunk(
    auth_id="MA_XXXXXX",
    trunk_id="trunk_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**trunk_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conference
<details><summary><code>client.conference.<a href="src/vobiz/conference/client.py">kick_member</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove one or more participants from a conference while allowing their XML flow to continue.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference.kick_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference.<a href="src/vobiz/conference/client.py">hangup_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate one or more active conference member calls. A normal active-member request disconnects the member. If a member was kicked, continued its XML flow, and rejoined with the same numeric member ID, confirm removal through conference exit or call hangup callbacks.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference.hangup_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference.<a href="src/vobiz/conference/client.py">play_audio_member</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Play an audio file to a specific conference member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference.play_audio_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
    url="https://example.com/audio.mp3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — URL of the audio file to play
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference.<a href="src/vobiz/conference/client.py">stop_audio_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop audio playback for a specific conference member.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference.stop_audio_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference.<a href="src/vobiz/conference/client.py">deaf_member</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prevent a conference member from hearing other participants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference.deaf_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference.<a href="src/vobiz/conference/client.py">undeaf_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore a conference member's ability to hear other participants.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference.undeaf_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## RecordCalls
<details><summary><code>client.record_calls.<a href="src/vobiz/record_calls/client.py">start_recording</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Begin recording an active call. Set format, enable transcription, and configure a callback URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.record_calls.start_recording(
    auth_id="MA_XXXXXX",
    call_uuid="cdr_XXXXXXXXXX",
    time_limit=120,
    file_format="mp3",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**time_limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**file_format:** `typing.Optional[StartRecordingRequestFileFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**transcription_type:** `typing.Optional[str]` — Set to `auto` to enable transcription
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**record_channel_type:** `typing.Optional[StartRecordingRequestRecordChannelType]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.record_calls.<a href="src/vobiz/record_calls/client.py">stop_recording</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop an active recording on an in-progress call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.record_calls.stop_recording(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PlayAudio
<details><summary><code>client.play_audio.<a href="src/vobiz/play_audio/client.py">call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Play an audio file to a live call leg.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.play_audio.call(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
    urls="https://example.com/audio.mp3",
    legs="aleg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**urls:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**legs:** `typing.Optional[PlayAudioCallRequestLegs]` 
    
</dd>
</dl>

<dl>
<dd>

**loop:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.play_audio.<a href="src/vobiz/play_audio/client.py">stop_audio_call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop audio playing on a live call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.play_audio.stop_audio_call(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SpeakText
<details><summary><code>client.speak_text.<a href="src/vobiz/speak_text/client.py">call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Convert text to speech and play it on a live call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.speak_text.call(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
    text="Hello, your appointment is confirmed for tomorrow at 3 PM.",
    voice="WOMAN",
    language="en-US",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**voice:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**language:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**legs:** `typing.Optional[SpeakTextCallRequestLegs]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.speak_text.<a href="src/vobiz/speak_text/client.py">stop_speak_call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop ongoing TTS playback on a live call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.speak_text.stop_speak_call(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Dtmf
<details><summary><code>client.dtmf.<a href="src/vobiz/dtmf/client.py">send_dtmf</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send DTMF (keypad) tones on an active call. Use `w` for 0.5s pause, `W` for 1s pause.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.dtmf.send_dtmf(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
    digits="1234",
    leg="aleg",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**digits:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**leg:** `typing.Optional[SendDtmfRequestLeg]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AudioStreams
<details><summary><code>client.audio_streams.<a href="src/vobiz/audio_streams/client.py">list_streams</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all audio streams on a live call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.audio_streams.list_streams(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audio_streams.<a href="src/vobiz/audio_streams/client.py">start_stream</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Start streaming raw audio from a live call to a WebSocket URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.audio_streams.start_stream(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
    service_url="wss://your-server.com/ws",
    bidirectional=True,
    audio_track="both",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**service_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**bidirectional:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**audio_track:** `typing.Optional[StartStreamRequestAudioTrack]` 
    
</dd>
</dl>

<dl>
<dd>

**audio_format:** `typing.Optional[StartStreamRequestAudioFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audio_streams.<a href="src/vobiz/audio_streams/client.py">get_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a specific audio stream.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.audio_streams.get_stream(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
    stream_id="stream_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stream_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.audio_streams.<a href="src/vobiz/audio_streams/client.py">stop_stream</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop a specific audio stream on a live call.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.audio_streams.stop_stream(
    auth_id="MA_XXXXXX",
    call_uuid="call_uuid",
    stream_id="stream_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**stream_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Conferences
<details><summary><code>client.conferences.<a href="src/vobiz/conferences/client.py">list_conferences</a>(...) -> ListConferencesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve conference room names reported by the API. An empty array is inconclusive and can occur while conferences are active. Maintain your own room registry for authoritative discovery, billing, cleanup, and destructive workflows.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conferences.list_conferences(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conferences.<a href="src/vobiz/conferences/client.py">delete_all_conferences</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate all active conference rooms.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conferences.delete_all_conferences(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conferences.<a href="src/vobiz/conferences/client.py">get_conference</a>(...) -> GetConferenceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific conference room. A live conference can currently return a 200 response with an error payload instead of conference details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conferences.get_conference(
    auth_id="MA_XXXXXX",
    conference_name="My Conf Room",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conferences.<a href="src/vobiz/conferences/client.py">delete_conference</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Terminate a specific conference room and disconnect all members.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conferences.delete_conference(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConferenceMembers
<details><summary><code>client.conference_members.<a href="src/vobiz/conference_members/client.py">mute_member</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prevent a member from speaking. Use `all` as member_id to mute everyone.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference_members.mute_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` — Member ID, comma-separated IDs, or `all`
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference_members.<a href="src/vobiz/conference_members/client.py">unmute_member</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Allow a muted member to speak again.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference_members.unmute_member(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
    member_id="member_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**member_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ConferenceRecording
<details><summary><code>client.conference_recording.<a href="src/vobiz/conference_recording/client.py">start_conference_recording</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue recording for all audio in a conference room. The response does not include a recording ID or download URL.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference_recording.start_conference_recording(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**file_format:** `typing.Optional[StartConferenceRecordingRequestFileFormat]` 
    
</dd>
</dl>

<dl>
<dd>

**callback_url:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.conference_recording.<a href="src/vobiz/conference_recording/client.py">stop_conference_recording</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stop recording a conference room.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.conference_recording.stop_conference_recording(
    auth_id="MA_XXXXXX",
    conference_name="conference_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Recordings
<details><summary><code>client.recordings.<a href="src/vobiz/recordings/client.py">list_recordings</a>(...) -> ListRecordingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all call recordings on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.recordings.list_recordings(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recordings.<a href="src/vobiz/recordings/client.py">get_recording</a>(...) -> GetRecordingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details and download URL for a specific recording.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.recordings.get_recording(
    auth_id="MA_XXXXXX",
    recording_id="rec_XXXXXXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.recordings.<a href="src/vobiz/recordings/client.py">delete_recording</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete a recording from the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.recordings.delete_recording(
    auth_id="MA_XXXXXX",
    recording_id="recording_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credentials
<details><summary><code>client.credentials.<a href="src/vobiz/credentials/client.py">create_credential</a>(...) -> CreateCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create SIP credentials for trunk authentication.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.credentials.create_credential(
    auth_id="MA_XXXXXX",
    username="myuser",
    password="securepassword123",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/vobiz/credentials/client.py">list_credentials</a>(...) -> ListCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all SIP credentials on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.credentials.list_credentials(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/vobiz/credentials/client.py">update_credential</a>(...) -> UpdateCredentialResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the password for an existing SIP credential.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.credentials.update_credential(
    auth_id="MA_XXXXXX",
    credential_id="credential_id",
    password="password",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/vobiz/credentials/client.py">delete_credential</a>(...) -> typing.Optional[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an existing SIP credential.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.credentials.delete_credential(
    auth_id="MA_XXXXXX",
    credential_id="credential_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**credential_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## IpAccessControlList
<details><summary><code>client.ip_access_control_list.<a href="src/vobiz/ip_access_control_list/client.py">create_ip_acl</a>(...) -> CreateIpAclResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an IP access control rule to restrict SIP trunk access.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.ip_access_control_list.create_ip_acl(
    auth_id="MA_XXXXXX",
    name="Office IP",
    ip_address="ip_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_access_control_list.<a href="src/vobiz/ip_access_control_list/client.py">list_ip_acls</a>(...) -> ListIpAclsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all IP access control rules on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.ip_access_control_list.list_ip_acls(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_access_control_list.<a href="src/vobiz/ip_access_control_list/client.py">update_ip_acl</a>(...) -> UpdateIpAclResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing IP access control rule.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.ip_access_control_list.update_ip_acl(
    auth_id="MA_XXXXXX",
    ip_acl_id="ip_acl_id",
    name="name",
    ip_address="ip_address",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**ip_acl_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**ip_address:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.ip_access_control_list.<a href="src/vobiz/ip_access_control_list/client.py">delete_ip_acl</a>(...) -> typing.Optional[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove an IP access control rule.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.ip_access_control_list.delete_ip_acl(
    auth_id="MA_XXXXXX",
    ip_acl_id="ip_acl_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**ip_acl_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## OriginationUri
<details><summary><code>client.origination_uri.<a href="src/vobiz/origination_uri/client.py">create_origination_uri</a>(...) -> CreateOriginationUriResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add an inbound SIP endpoint (origination URI) to a trunk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.origination_uri.create_origination_uri(
    auth_id="MA_XXXXXX",
    name="Primary SBC",
    sip_uri="sip:sbc.example.com",
    priority=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**sip_uri:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.origination_uri.<a href="src/vobiz/origination_uri/client.py">list_origination_uris</a>(...) -> ListOriginationUrisResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all origination URIs on the account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.origination_uri.list_origination_uris(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.origination_uri.<a href="src/vobiz/origination_uri/client.py">update_origination_uri</a>(...) -> UpdateOriginationUriResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing origination URI.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.origination_uri.update_origination_uri(
    auth_id="MA_XXXXXX",
    uri_id="uri_id",
    name="name",
    priority=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**uri_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**priority:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.origination_uri.<a href="src/vobiz/origination_uri/client.py">delete_origination_uri</a>(...) -> typing.Optional[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an origination URI from a trunk.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.origination_uri.delete_origination_uri(
    auth_id="MA_XXXXXX",
    uri_id="uri_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**uri_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Applications
<details><summary><code>client.applications.<a href="src/vobiz/applications/client.py">list_applications</a>(...) -> ListApplicationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of all applications created under your Vobiz account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.applications.list_applications(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/vobiz/applications/client.py">create_application</a>(...) -> CreateApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an Application with webhook URLs for call handling.
Creating an application is usually a first step, after which you
attach the application to either a number or an endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.applications.create_application(
    auth_id="MA_XXXXXX",
    app_name="My Voice Application",
    answer_url="https://example.com/answer",
    answer_method="POST",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**app_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**answer_url:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**answer_method:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/vobiz/applications/client.py">retrieve_application</a>(...) -> RetrieveApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get details of a particular application by passing the app_id.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.applications.retrieve_application(
    auth_id="MA_XXXXXX",
    app_id="12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` — Unique identifier for the application
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/vobiz/applications/client.py">update_application</a>(...) -> UpdateApplicationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Modify an application using this API. You can update any subset of
fields (partial update). Fields not provided will remain unchanged.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.applications.update_application(
    auth_id="MA_XXXXXX",
    app_id="12345678",
    app_name="Updated Application Name",
    default_number_app=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**app_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**default_number_app:** `bool` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.applications.<a href="src/vobiz/applications/client.py">delete_application</a>(...) -> typing.Optional[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an Application. If the application is associated
with phone numbers, the deletion may be blocked unless those
associations are removed first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.applications.delete_application(
    auth_id="MA_XXXXXX",
    app_id="12345678",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**app_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Endpoints
<details><summary><code>client.endpoints.<a href="src/vobiz/endpoints/client.py">list_endpoints</a>(...) -> ListEndpointsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a paginated list of all SIP endpoints in your account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.endpoints.list_endpoints(
    auth_id="MA_XXXXXX",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**username_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username_exact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**username_startswith:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**alias_contains:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**alias_exact:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**application_id_exact:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**application_id_isnull:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**sub_account:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.endpoints.<a href="src/vobiz/endpoints/client.py">create_endpoint</a>(...) -> CreateEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new SIP endpoint that can be used to make and receive calls
through IP phones, softphones, or SIP clients. Each endpoint is
assigned a unique SIP URI and endpoint ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.endpoints.create_endpoint(
    auth_id="MA_XXXXXX",
    username="john_doe",
    password="SecurePassword123!",
    alias="John\'s Desktop Phone",
    application=12345678,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**username:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**alias:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**application:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.endpoints.<a href="src/vobiz/endpoints/client.py">retrieve_endpoint</a>(...) -> RetrieveEndpointResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the details of an existing endpoint. The response includes
all endpoint attributes and, if the endpoint is currently registered
on a SIP client, additional registration details.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.endpoints.retrieve_endpoint(
    auth_id="MA_XXXXXX",
    endpoint_id="87654321",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.endpoints.<a href="src/vobiz/endpoints/client.py">update_endpoint</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an existing endpoint's configuration. You can change the
password, alias, or attached application. The fields `username`,
`endpoint_id`, `domain`, `allow_same_domain`, `allow_other_domains`,
`allow_phones`, and `allow_apps` are locked after creation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.endpoints.update_endpoint(
    auth_id="MA_XXXXXX",
    endpoint_id="87654321",
    alias="John\'s Updated Desktop Phone",
    password="NewSecurePassword456!",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**alias:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.endpoints.<a href="src/vobiz/endpoints/client.py">delete_endpoint</a>(...) -> typing.Optional[str]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently delete an endpoint from your Vobiz account. Once deleted,
the SIP URI will no longer be accessible, and any devices registered
with this endpoint will be disconnected.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.endpoints.delete_endpoint(
    auth_id="MA_XXXXXX",
    endpoint_id="87654321",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**auth_id:** `str` — Your account Auth ID
    
</dd>
</dl>

<dl>
<dd>

**endpoint_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Partner API
<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">get_partner_profile</a>() -> GetPartnerProfileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the authenticated partner's profile and balance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.get_partner_profile()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">get_partner_dashboard</a>() -> GetPartnerDashboardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Aggregated partner metrics - total customers, active accounts, balance
held across the partner ecosystem, MTD revenue, etc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.get_partner_dashboard()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">list_customer_accounts</a>(...) -> ListCustomerAccountsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all customer sub-accounts under your partner account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.list_customer_accounts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Substring match on name or email.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">create_customer_account</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new customer sub-account under your partner account. VoBiz
emails the customer their login credentials and (separately) a KYC link
via the kyc-sessions endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.create_customer_account(
    name="John Doe",
    email="john@example.com",
    phone="+919876543210",
    password="SecurePass123!",
    country="IN",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Customer's full name.
    
</dd>
</dl>

<dl>
<dd>

**email:** `str` — Customer's email. KYC link is sent here.
    
</dd>
</dl>

<dl>
<dd>

**phone:** `str` — E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — Min 8 chars, must include a number and a special character.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — ISO 2-letter country code.
    
</dd>
</dl>

<dl>
<dd>

**company:** `typing.Optional[str]` — Legal company or business name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">partner_transfer_balance</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Atomically debits your partner master balance and credits the customer's
wallet. Both legs are recorded in each account's ledger. Transfers are
**permanent and cannot be reversed.**
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.partner_transfer_balance(
    customer_auth_id="MA_ZKITB8Z2",
    amount=500,
    currency="INR",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — Positive decimal. Your master balance must be ≥ this amount.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `str` — Must match your partner account currency.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Note for your records. Appears in both ledgers.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">list_customer_transactions</a>(...) -> ListCustomerTransactionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the customer's transaction ledger. Filter by date range or
transaction type. Useful for billing reconciliation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment
import datetime

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.list_customer_transactions(
    customer_auth_id="customer_auth_id",
    from_date=datetime.date.fromisoformat("2026-03-01"),
    to_date=datetime.date.fromisoformat("2026-03-31"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**transaction_type:** `typing.Optional[ListCustomerTransactionsRequestTransactionType]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">list_customer_cdrs</a>(...) -> ListCustomerCdrsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Look up any customer's call history. Same filter set as the
customer-side CDR endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.list_customer_cdrs(
    customer_auth_id="customer_auth_id",
    hangup_cause="NO_ANSWER",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.date]` 
    
</dd>
</dl>

<dl>
<dd>

**call_direction:** `typing.Optional[ListCustomerCdrsRequestCallDirection]` 
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListCustomerCdrsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**min_duration:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**hangup_cause:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">list_customer_numbers</a>(...) -> ListCustomerNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Phone numbers currently assigned to a customer account.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.list_customer_numbers(
    customer_auth_id="customer_auth_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**customer_auth_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Substring match against the E.164 number.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">list_kyc_sessions</a>(...) -> ListKycSessionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the authenticated partner's KYC sessions. Filter the list by
session status or customer account, and use `page` and `size` to
paginate the results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.list_kyc_sessions()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**status:** `typing.Optional[ListKycSessionsRequestStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**account_auth_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">create_kyc_session</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers VoBiz to email a KYC link to the customer. KYC is OTP-based
(PAN + Aadhaar via DigiLocker for individuals, PAN + GSTIN for
companies). No document uploads required.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.create_kyc_session(
    account_auth_id="MA_ZKITB8Z2",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**account_auth_id:** `str` — Customer's auth_id (from create-customer-account).
    
</dd>
</dl>

<dl>
<dd>

**flow_type:** `typing.Optional[CreateKycSessionRequestFlowType]` 

Delivery mode. `email` (default) emails the customer the KYC link.
`redirect` returns a `widget_url` in the response for immediate redirect.
    
</dd>
</dl>

<dl>
<dd>

**customer_email:** `typing.Optional[str]` — Required when `flow_type` is `email`. Ignored otherwise.
    
</dd>
</dl>

<dl>
<dd>

**redirect_url:** `typing.Optional[str]` 

Required when `flow_type` is `redirect`. After verification the customer's
browser is sent to this URL with query params `session_id`, `status`, `auth_id`.
    
</dd>
</dl>

<dl>
<dd>

**webhook_url:** `typing.Optional[str]` — VoBiz POSTs the KYC result here.
    
</dd>
</dl>

<dl>
<dd>

**expires_in_days:** `typing.Optional[int]` — Days before the KYC link expires.
    
</dd>
</dl>

<dl>
<dd>

**reminder_schedule:** `typing.Optional[typing.List[CreateKycSessionRequestReminderScheduleItem]]` — Auto reminder emails before expiry. Email flow only.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Dict[str, typing.Any]]` — Free-form key/value object echoed back on GET and webhooks.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">get_kyc_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the current status and available details for one KYC session
owned by the authenticated partner.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.get_kyc_session(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">revoke_kyc_session</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels an outstanding KYC session. Customer can no longer use the link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.revoke_kyc_session(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.partner_api.<a href="src/vobiz/partner_api/client.py">resend_kyc_session</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Re-dispatches the KYC link to the customer. Rate-limited to once per 30 minutes.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from vobiz import Vobiz
from vobiz.environment import VobizEnvironment

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.partner_api.resend_kyc_session(
    session_id="session_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

