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

<details><summary><code>client.account.<a href="src/vobiz/account/client.py">preview_channel_pricing</a>(...) -> ChannelPricingPreview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the monthly price for CPS or concurrent-call capacity without purchasing capacity or debiting the account.
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

client.account.preview_channel_pricing(
    auth_id="MA_XXXX",
    resource_type="concurrent_calls",
    quantity=30,
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

**auth_id:** `str` — Target account Auth ID. An account can preview only its own pricing; administrators may act for another account.
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `CapacityResourceType` — Capacity type to price.
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `int` — Capacity quantity to price. Pricing-tier block and quantity rules also apply.
    
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

<details><summary><code>client.account.<a href="src/vobiz/account/client.py">create_channel_subscription</a>(...) -> ChannelSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Purchase recurring CPS or concurrent-call capacity. A successful request immediately debits the first monthly charge and activates a subscription that renews every 30 days.
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

client.account.create_channel_subscription(
    auth_id="MA_XXXX",
    resource_type="concurrent_calls",
    quantity=30,
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

**auth_id:** `str` — Target account Auth ID. An account can purchase only for itself; administrators may act for another account.
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `CapacityResourceType` 
    
</dd>
</dl>

<dl>
<dd>

**quantity:** `int` — Capacity quantity to purchase. Pricing-tier block and quantity rules also apply.
    
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

Retrieve paginated transaction history for the account, ordered by
`created_at` descending. Filter to a single day by setting `from_date`
and `to_date` to the same date - a bare `YYYY-MM-DD` in `to_date` is
expanded to `23:59:59`, so both bounds are inclusive. Bare dates resolve
in the server timezone (UTC); send an explicit offset such as
`2026-08-28T00:00:00+05:30` to pin a local calendar day.

`limit` and `offset` are not supported - unknown parameters are silently
dropped. `total` and `summary` are computed over the whole filtered set
and ignore pagination, so `per_page=1` returns full-window totals.
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
    from_date="2026-08-25",
    to_date="2026-08-25",
    type="debit",
    currency="INR",
    reference_type="cdr",
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

**page:** `typing.Optional[int]` — Page number, 1-indexed.
    
</dd>
</dl>

<dl>
<dd>

**per_page:** `typing.Optional[int]` — Records per page. A value above the maximum falls back to the default of 50 rather than clamping.
    
</dd>
</dl>

<dl>
<dd>

**from_date:** `typing.Optional[str]` — Start of the window, inclusive. Date-only or full ISO 8601 timestamp. Day boundaries are UTC.
    
</dd>
</dl>

<dl>
<dd>

**to_date:** `typing.Optional[str]` — End of the window, inclusive. A date-only value covers the whole day.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[str]` — `credit` or `debit` act as broad classifications and sweep in legacy entry types such as `did_rental`; any other value is an exact match on `transactions[].type`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListTransactionsRequestStatus]` — Exact match on transaction status.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[str]` — Currency code. Uppercased server-side, exact match.
    
</dd>
</dl>

<dl>
<dd>

**reference_type:** `typing.Optional[str]` — Spend source, matching `transactions[].reference_type`.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Case-insensitive substring match on the description.
    
</dd>
</dl>

<dl>
<dd>

**reference:** `typing.Optional[str]` — Case-insensitive substring match on the reference.
    
</dd>
</dl>

<dl>
<dd>

**transaction_id:** `typing.Optional[str]` — Fetch a single ledger entry by its UUID.
    
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

<details><summary><code>client.balance.<a href="src/vobiz/balance/client.py">list_transaction_reference_types</a>(...) -> ListTransactionReferenceTypesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the distinct `reference_type` values present on the account's ledger. Use it to discover valid values for the `reference_type` filter on the transactions endpoint.
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

client.balance.list_transaction_reference_types(
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

Destination PSTN number or SIP endpoint. Separate multiple destinations with
the `<` character to fan out a single request to up to 1000 destinations,
for example `+919876543210<+919876543211`.
    
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

- `personal_use` *(default)* - the sub-account inherits the parent's
  KYC; no separate verification is required.
- `customer_use` - the sub-account must complete its own KYC before it
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

**webhook_url:** `typing.Optional[str]` — HTTPS endpoint Vobiz POSTs the KYC result to. Omit it and no callbacks are sent.
    
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

Mock PAN verification - never hits the provider. Magic `pan` inputs:

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
type to a terminal outcome - this drives the async (`TESTPENDING…`)
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

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">unrent_number</a>(...) -> UnrentNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Release a phone number from your account. Releasing a number incurs the
number-release fee configured for the account; the response returns the
charged amount in `release_fee`. By default, the number enters
`pending_release` for a 24-hour cooldown. Cancelling during that window
refunds the release fee. Set `immediate=true` to skip the cooldown; an
immediate release cannot be cancelled.
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
    e164="%2B919876543210",
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

**e164:** `str` — The URL-encoded phone number in E.164 format. Encode `+` as `%2B`.
    
</dd>
</dl>

<dl>
<dd>

**immediate:** `typing.Optional[bool]` — Skip the 24-hour cooldown and release the number immediately.
    
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

<details><summary><code>client.phone_numbers.<a href="src/vobiz/phone_numbers/client.py">cancel_number_release</a>(...) -> CancelNumberReleaseResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancel a pending number release during the 24-hour cooldown. The number is
restored to `active`, the cooldown timer is cleared, and the release fee is
refunded in full to the account balance. Any trunk or voice application
detached by the release is not re-attached automatically.
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

client.phone_numbers.cancel_number_release(
    account_id="MA_XXXXXX",
    e164="%2B919876543210",
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

**account_id:** `str` — Your account Auth ID.
    
</dd>
</dl>

<dl>
<dd>

**e164:** `str` — The URL-encoded phone number in E.164 format. Encode `+` as `%2B`.
    
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

**trunk_direction:** `typing.Optional[CreateTrunkRequestTrunkDirection]` — Direction of the trunk - **`inbound` or `outbound` only** (a trunk is one direction, not both).
    
</dd>
</dl>

<dl>
<dd>

**trunk_status:** `typing.Optional[CreateTrunkRequestTrunkStatus]` — Trunk status - `enabled` or `disabled` (note: not `active`).
    
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
Must be a valid **public** http/https URL. SSRF-validated - localhost,
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

**username:** `typing.Optional[str]` — Deprecated - use `credential_uuid`.
    
</dd>
</dl>

<dl>
<dd>

**password:** `typing.Optional[str]` — Deprecated - use `credential_uuid`.
    
</dd>
</dl>

<dl>
<dd>

**ip_whitelist:** `typing.Optional[typing.List[str]]` — Deprecated - use `ipacl_uuid`.
    
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

**trunk_direction:** `typing.Optional[UpdateTrunkRequestTrunkDirection]` — Direction of the trunk - `inbound` or `outbound` only.
    
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

## Bulk Operations
<details><summary><code>client.bulk_operations.<a href="src/vobiz/bulk_operations/client.py">bulk_export_recordings</a>(...) -> BulkExportRecordingsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Queue a bulk export of the recordings matching your filter criteria. The request is
validated and accepted for background processing, and the resulting archive is emailed
as a download link to every address in `recipient.customer_account`. The archive is
typically available within 15-60 minutes depending on volume.

Results are delivered by email only; the export runs to completion in the background
after the `202` response.

One export runs at a time per account. While an export is in progress, further requests
return `403`.

Filter rules:
- Use either `from`/`to` or the `recording_storage_duration*` filters, not both.
- Use one of `__gt` or `__gte`, and one of `__lt` or `__lte`.
- When using range filters (`__gte`/`__lte`), provide both.
- Maximum date range is 1 year (366 days); maximum storage duration range is 30 days.
- The additional filters (`from_number`, `to_number`, `call_uuid`, `conference_name`,
  `recording_format`, `recording_id`) apply when the range is 30 days or less.
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
from vobiz.bulk_operations import BulkExportRecordingsRequestRecipient

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.bulk_operations.bulk_export_recordings(
    auth_id="MA_XXXXXX",
    recipient=BulkExportRecordingsRequestRecipient(
        customer_account=[
            "admin@example.com"
        ],
    ),
    from_="2025-01-23 00:00:00",
    to="2025-01-30 23:59:59",
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

**recipient:** `BulkExportRecordingsRequestRecipient` — Email delivery targets for the export archive.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — Start date for the export. Format: YYYY-MM-DD HH:MM:SS. Defaults to 7 days ago.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — End date for the export. Format: YYYY-MM-DD HH:MM:SS. Defaults to the current time.
    
</dd>
</dl>

<dl>
<dd>

**recording_storage_duration:** `typing.Optional[str]` — Export recordings exactly N days old. `"7"` exports recordings from exactly 7 days ago.
    
</dd>
</dl>

<dl>
<dd>

**recording_storage_duration_gte:** `typing.Optional[str]` — Export recordings N days old or older. `"7"` exports recordings 7 days old and older.
    
</dd>
</dl>

<dl>
<dd>

**recording_storage_duration_gt:** `typing.Optional[str]` — Export recordings older than N days. `"7"` exports recordings 8 days old and older.
    
</dd>
</dl>

<dl>
<dd>

**recording_storage_duration_lte:** `typing.Optional[str]` — Export recordings N days old or newer. `"30"` exports recordings 0-30 days old.
    
</dd>
</dl>

<dl>
<dd>

**recording_storage_duration_lt:** `typing.Optional[str]` — Export recordings newer than N days. `"30"` exports recordings 0-29 days old.
    
</dd>
</dl>

<dl>
<dd>

**from_number:** `typing.Optional[str]` — Filter by caller phone number. Applies when the range is 30 days or less.
    
</dd>
</dl>

<dl>
<dd>

**to_number:** `typing.Optional[str]` — Filter by destination phone number. Applies when the range is 30 days or less.
    
</dd>
</dl>

<dl>
<dd>

**call_uuid:** `typing.Optional[str]` — Filter by call UUID. Also use this field for a conference_uuid or mpc_uuid. Applies when the range is 30 days or less.
    
</dd>
</dl>

<dl>
<dd>

**conference_name:** `typing.Optional[str]` — Filter by conference name. Also use this field for an mpc_name. Applies when the range is 30 days or less.
    
</dd>
</dl>

<dl>
<dd>

**recording_format:** `typing.Optional[BulkExportRecordingsRequestRecordingFormat]` — Filter by recording format. Applies when the range is 30 days or less.
    
</dd>
</dl>

<dl>
<dd>

**recording_id:** `typing.Optional[str]` — Filter by a specific recording ID. Applies when the range is 30 days or less.
    
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

Creates a new customer sub-account under your partner account. Vobiz
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

Triggers Vobiz to email a KYC link to the customer. KYC is OTP-based
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

**webhook_url:** `typing.Optional[str]` — Vobiz POSTs the KYC result here.
    
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

## Messages
<details><summary><code>client.sms.messages.<a href="src/vobiz/sms/messages/client.py">list_messages</a>(...) -> MessageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the messages on your account, sent and received, newest first. Combine the filters to find a message you did not keep the `id` for, such as the other recipients of a multi-recipient send (filter by `tag` or `to`). Every filter is an exact match, and filters you omit are not applied. Page through results with `limit` and `offset`, and use `total` to know when to stop.
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

client.sms.messages.list_messages()

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

**status:** `typing.Optional[ListMessagesRequestStatus]` — Only messages with this status: `scheduled`, `sent`, `delivered`, `failed`, `received` (inbound) or `unknown`.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[ListMessagesRequestChannel]` — Only messages sent or received on this channel: `sms`, `mms` or `rcs`. This is the channel actually used, so an SMS that was upgraded to MMS appears under `mms`.
    
</dd>
</dl>

<dl>
<dd>

**direction:** `typing.Optional[ListMessagesRequestDirection]` — `out` for messages you sent, `in` for messages your numbers received.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — Recipient number to filter on, in E.164 format, exact match. For inbound messages this is your number.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — Sender to filter on, exact match: one of your numbers in E.164 format (for example `+14155550100`), or the `senderName` of your RCS sender for RCS messages. For inbound messages this is the contact's number.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Only messages whose `tag` equals this value, exact match. Set the same `tag` on related sends to retrieve them together.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[datetime.datetime]` — Only messages created at or after this time, as an RFC 3339 / ISO 8601 timestamp such as `2026-10-01T00:00:00Z`.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[datetime.datetime]` — Only messages created before this time, as an RFC 3339 / ISO 8601 timestamp such as `2026-11-01T00:00:00Z`. Combine with `startDate` for a date range.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return, from `1` to `100`. Defaults to `20`; a value outside that range also returns `20`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of records to skip before the page starts, `0` or greater. Defaults to `0`. Add the page size to it to fetch the next page.
    
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

<details><summary><code>client.sms.messages.<a href="src/vobiz/sms/messages/client.py">send_message</a>(...) -> Message</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends an SMS, MMS or RCS message from one of your numbers or RCS senders to one or more recipients. Each number in `to` becomes its own message, with its own `id`, status and conversation, and the response body is the first recipient's message. Every recipient is checked against your opt-out list first, and a send with a future `scheduledAt` is stored with status `scheduled`.

- `201` when every recipient was accepted, including an idempotent replay and a successful SMS fallback.
- `202` when at least one recipient was recorded and at least one errored. Find the other recipients with `GET /messages` filtered by `tag` or `to`.
- `422` when the recipient has opted out and nothing was recorded.
- `502` when the send was rejected before a message was recorded. Retry with the same `idempotencyKey`.

Track delivery with `GET /messages/{id}`, your webhooks (callbacks) or the WebSocket.
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

client.sms.messages.send_message(
    from_="+14155550100",
    to=[
        "+14155550123"
    ],
    channel="sms",
    text="Your verification code is 482913",
    idempotency_key="otp-482913-user-77",
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

**from:** `str` — The sender. For `sms` and `mms`, one of your Vobiz numbers in E.164 format, for example `+14155550100`. For `rcs`, the `senderName` of your RCS sender (from `GET /senders`); with `failoverToSms`, the SMS copy is sent from a number on your account.
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.List[str]` — One or more recipient numbers in E.164 format. Each one becomes a separate message with its own `id`; blank entries and duplicates are ignored. At least one recipient is required.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[SendMessageRequestChannel]` — Channel to send on: `sms`, `mms` or `rcs`. Defaults to `sms`. An `sms` with `mediaUrls` to US or Canadian recipients is sent as MMS automatically.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — Message body. Required for `sms` and `rcs`. A long SMS is split into segments and billed per segment (160 GSM-7 or 70 UCS-2 characters fit in one segment). For `mms`, provide `text`, `mediaUrls` or both, with `text` up to 5000 characters.
    
</dd>
</dl>

<dl>
<dd>

**media_urls:** `typing.Optional[typing.List[str]]` — Publicly reachable `https` URLs of media to attach. MMS accepts up to 10. RCS sends the first URL as a file. An SMS to recipients outside the US and Canada is sent as text only.
    
</dd>
</dl>

<dl>
<dd>

**title:** `typing.Optional[str]` — Subject line of an MMS. Used only when the message is sent as MMS.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Your own label, stored on every message the request creates. Filter `GET /messages` by it to find all recipients of one send or to group messages for reporting.
    
</dd>
</dl>

<dl>
<dd>

**idempotency_key:** `typing.Optional[str]` — A unique string you choose, for example a UUID or your own order ID, scoped to your account. Retrying with the same key returns the original message instead of sending again. With several recipients the key is applied per recipient.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[datetime.datetime]` — Time to hold the message until, as an RFC 3339 / ISO 8601 timestamp such as `2026-11-01T09:00:00Z`. A future time stores the message with status `scheduled`; a past time or now sends immediately.
    
</dd>
</dl>

<dl>
<dd>

**failover_to_sms:** `typing.Optional[bool]` — Used only when `channel` is `rcs`. When `true` and the RCS send cannot go through, Vobiz sends the same `text` as SMS and the message's `channel` becomes `sms`. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**rcs_suggestions:** `typing.Optional[typing.List[RcsSuggestion]]` — Suggestion buttons (suggested replies and actions) to show under an RCS message. Used only when `channel` is `rcs`. See the RCS suggestion object for each `type`.
    
</dd>
</dl>

<dl>
<dd>

**dlt_entity_id:** `typing.Optional[str]` — India (TRAI DLT): the Principal Entity ID you registered on a TRAI DLT portal. Pass it on every message to Indian numbers.
    
</dd>
</dl>

<dl>
<dd>

**dlt_header_id:** `typing.Optional[str]` — India (TRAI DLT): the ID of the sender header you registered on a TRAI DLT portal. Pass it on every message to Indian numbers.
    
</dd>
</dl>

<dl>
<dd>

**dlt_template_id:** `typing.Optional[str]` — India (TRAI DLT): the ID of the content template you registered on a TRAI DLT portal. `text` must match that template with its variables filled in.
    
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

<details><summary><code>client.sms.messages.<a href="src/vobiz/sms/messages/client.py">preview_message_cost</a>(...) -> CostPreview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Prices a message before you send it, without sending anything. It splits `text` into segments for the chosen channel and returns the segment count, the price per segment and the total in your account currency. Use it to show a cost estimate in your app or to keep long messages within a budget. The figures are for one recipient; multiply `totalCost` by the number of recipients for a multi-recipient send.
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

client.sms.messages.preview_message_cost(
    from_="+14155550100",
    to="+14155550123",
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

**from:** `str` — Required. The sender you plan to use: one of your numbers in E.164 format, or the `senderName` of your RCS sender when `channel` is `rcs`. It determines the route the message is priced on.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Required. One recipient number in E.164 format, for example `+14155550123`. Its destination country determines the price.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[PreviewMessageCostRequestChannel]` — Channel to price: `sms`, `mms` or `rcs`. Defaults to `sms`.
    
</dd>
</dl>

<dl>
<dd>

**text:** `typing.Optional[str]` — The message body to segment and price, URL-encoded. Pass the exact text you plan to send: the segment count depends on its length and on whether it fits the GSM-7 character set. Defaults to an empty string.
    
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

<details><summary><code>client.sms.messages.<a href="src/vobiz/sms/messages/client.py">check_rcs_reachability</a>(...) -> RcsReachability</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks whether a phone number can receive RCS messages from your RCS sender, without sending anything. Call it before an RCS send to choose between RCS and SMS for that contact. If `reachable` is `false`, send with `channel: "sms"` instead, or send RCS with `failoverToSms: true` so Vobiz falls back to SMS automatically.
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

client.sms.messages.check_rcs_reachability(
    from_="YOUR_RCS_SENDER_NAME",
    to="+14155550123",
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

**from:** `str` — Required. The `senderName` of your RCS sender, as returned by `GET /senders`.
    
</dd>
</dl>

<dl>
<dd>

**to:** `str` — Required. The recipient number to check, in E.164 format, for example `+14155550123`.
    
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

<details><summary><code>client.sms.messages.<a href="src/vobiz/sms/messages/client.py">get_message</a>(...) -> MessageWithHistory</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one message with its full status history. Use it to follow a message from `sent` to `delivered` or `failed`, and to read `errorCode` and `errorMessage` when it fails. The `statusHistory` array lists every status change, oldest first. For real-time updates, subscribe to webhooks (callbacks) or the WebSocket instead of polling.
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

client.sms.messages.get_message(
    id="9b2e1c40-8a3d-4f5e-9c1a-7d6b2e8f4a01",
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

**id:** `str` — The message `id` (UUID) returned by `POST /messages`, `GET /messages`, a conversation, or an event.
    
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

## Numbers
<details><summary><code>client.sms.numbers.<a href="src/vobiz/sms/numbers/client.py">list_numbers</a>() -> SmsNumberList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every number on your account that is routed for SMS or MMS, sorted by `countryCode` and then `e164`. Each number carries its US registration state, the last message it sent and a `sendable` summary of where it can send right now. Check `sendable.usDomestic` before you send to US recipients from a US number. To add numbers, search with `GET /numbers/available` and buy with `POST /numbers/purchase`.
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

client.sms.numbers.list_numbers()

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

<details><summary><code>client.sms.numbers.<a href="src/vobiz/sms/numbers/client.py">list_countries</a>() -> NumberCountries</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the countries where you can buy messaging numbers, with the number types and capabilities in stock in each. The list is a snapshot that refreshes in the background: while `ready` is `false`, `countries` is empty and you retry shortly. India is not listed, because traffic to Indian recipients is sent from DLT-registered sender IDs. Pass a returned `country` to `GET /numbers/available` to see individual numbers.
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

client.sms.numbers.list_countries()

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

<details><summary><code>client.sms.numbers.<a href="src/vobiz/sms/numbers/client.py">search_available_numbers</a>(...) -> AvailableNumbersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Searches the inventory for numbers you can buy in one country, with their setup and monthly prices in your wallet currency. Each search returns up to 10 numbers. Pass the chosen `e164`, the `country` and any non-empty `numberKey` to `POST /numbers/purchase`. For `country=IN` the list is empty and `hint` explains that Indian traffic uses DLT-registered sender IDs. A country outside the set Vobiz sells numbers in returns `422`.
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

client.sms.numbers.search_available_numbers(
    country="US",
    capabilities="SMS,MMS",
    area_code="415",
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

**country:** `str` — Country to search, as an ISO 3166-1 alpha-2 code such as `US`, `CA` or `GB`. Case-insensitive. A value that is not two letters returns `400` with `country must be an ISO 3166-1 alpha-2 code`.
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[str]` — Comma-separated capabilities the number must have: `SMS`, `MMS`, or `SMS,MMS`. Case-insensitive, defaults to `SMS`. Any other value returns `400` with `capabilities must be SMS and/or MMS`.
    
</dd>
</dl>

<dl>
<dd>

**area_code:** `typing.Optional[str]` — Three-digit area code to search in, for example `415`. Accepted only when `country` is `US` or `CA`; other countries return `400` with `areaCode is only supported for US and CA`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results, from `1` to `100`. Defaults to `10`, and each search returns at most 10 numbers whatever you pass. A value outside the range returns `400` with `limit must be between 1 and 100`.
    
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

<details><summary><code>client.sms.numbers.<a href="src/vobiz/sms/numbers/client.py">purchase_number</a>(...) -> PurchaseNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Buys a number returned by `GET /numbers/available` and routes it to your account for messaging. This call spends money: it debits the setup fee and the first month's rental from your wallet before the number is bought, and the rental renews monthly until you release the number. If the purchase cannot complete after the debit, your wallet is refunded and the error message says so. Run it only with your own credentials once you have confirmed the number and price. A `numbers.updated` WebSocket event is published when the number goes live; a US number then needs a 10DLC campaign or toll-free verification before it can send to US recipients.
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

client.sms.numbers.purchase_number(
    e164="+14155550100",
    country="US",
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

**e164:** `str` — The number to buy, in E.164 format, exactly as returned in `e164` by `GET /numbers/available`. Required.
    
</dd>
</dl>

<dl>
<dd>

**country:** `str` — ISO 3166-1 alpha-2 code of the number's country, for example `US`. Required, and must match the number; a mismatch returns `400`.
    
</dd>
</dl>

<dl>
<dd>

**number_key:** `typing.Optional[str]` — The `numberKey` from `GET /numbers/available`. Required when the search result has a non-empty `numberKey`, as for `CA` and `GB` numbers; omit it for US numbers, which are bought by `e164` alone.
    
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

<details><summary><code>client.sms.numbers.<a href="src/vobiz/sms/numbers/client.py">list_purchases</a>() -> NumberPurchaseList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the numbers you have bought through Vobiz, newest first, each with its full list of wallet charges. Released numbers stay in the list with `status: released`, so this is the billing history of every number you have owned. Use `nextBillingAt` to see when each active number renews and `charges` to reconcile setup and rental debits.
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

client.sms.numbers.list_purchases()

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

<details><summary><code>client.sms.numbers.<a href="src/vobiz/sms/numbers/client.py">release_number</a>(...) -> ReleaseNumberResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Cancels a number you bought through Vobiz and removes it from your account. The number stops sending and receiving messages immediately, and monthly rental stops. The setup fee and the current month are not refunded, and a released number cannot be restored. The call has no request body and returns the purchase with `status: released`. Run it only with your own credentials once you are sure you no longer need the number.
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

client.sms.numbers.release_number(
    e164="+14155550100",
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

**e164:** `str` — The number to release, in E.164 format, for example `+14155550100`. In raw HTTP requests, URL-encode the `+` as `%2B`; the SDKs encode it for you. A value that is not an E.164 number returns `400`, and a number that is not on your account returns `404`.
    
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

## Coverage
<details><summary><code>client.sms.coverage.<a href="src/vobiz/sms/coverage/client.py">list_coverage</a>(...) -> CoverageList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one summary row per destination country, sorted by country name: the sender types it accepts, whether sender registration is required, two-way support, opt-out rules and whether a sending window applies. Use it to plan where to send and which sender to use before you buy numbers or register. Filters combine, so `region` plus `twoWay=true` returns only two-way countries in that region. For the full record of one country, call `GET /coverage/{country}`.
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

client.sms.coverage.list_coverage(
    q="united",
    region="Northern America",
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

**q:** `typing.Optional[str]` — Search text, case-insensitive. Matches a substring of the country name (`united`), an exact ISO 3166-1 alpha-2 code (`GB`) or the start of the dial code (`44` or `+44`); spaces and a leading `+` are ignored.
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Exact region name, case-insensitive, for example `Northern America`, `Western Europe` or `South-central Asia`. Partial names match nothing; read the `region` values from an unfiltered list to see the full set.
    
</dd>
</dl>

<dl>
<dd>

**two_way:** `typing.Optional[bool]` — `true` returns only countries where recipients can reply; `false` returns the rest, including countries where two-way support is unknown. Also accepts `1`/`0` and `t`/`f`; any other value returns `400` with `twoWay must be true or false`.
    
</dd>
</dl>

<dl>
<dd>

**registration_required:** `typing.Optional[bool]` — `true` returns countries that require sender registration for local or international traffic; `false` returns countries that require neither. Accepts the same values as `twoWay`; anything else returns `400` with `registrationRequired must be true or false`.
    
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

<details><summary><code>client.sms.coverage.<a href="src/vobiz/sms/coverage/client.py">get_coverage</a>(...) -> CoverageDetail</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the full coverage record for one country: accepted sender types, registration requirements and lead time, link rules, prohibited topics, the permitted sending window and free-text market notes. Read it before your first send to a new country so your sender, content and send times match the local rules. An unknown code returns `404` with `country not found`.
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

client.sms.coverage.get_coverage(
    country="US",
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

**country:** `str` — ISO 3166-1 alpha-2 code of the destination country, for example `US`, `GB` or `IN`. Case-insensitive. Three-letter codes and dial codes return `404`.
    
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

## Conversations
<details><summary><code>client.sms.conversations.<a href="src/vobiz/sms/conversations/client.py">list_conversations</a>(...) -> typing.List[Conversation]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns your conversations, most recently active first (ordered by `lastMessageAt`). A conversation is the thread between one of your numbers and one contact on one channel, and Vobiz creates it with the first message in either direction. The response is a bare JSON array, `[]` when you have none. Page with `limit` and `offset`; when a page returns fewer items than `limit`, you have reached the end.
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

client.sms.conversations.list_conversations()

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

**limit:** `typing.Optional[int]` — Maximum number of conversations to return, from `1` to `100`. Defaults to `20`; a value outside that range also returns `20`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of conversations to skip before the page starts, `0` or greater. Defaults to `0`. Add the page size to it to fetch the next page.
    
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

<details><summary><code>client.sms.conversations.<a href="src/vobiz/sms/conversations/client.py">unread_count</a>() -> UnreadCount</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the total of `unreadCount` across all your conversations. Use it for an inbox badge, then call `GET /conversations` to see which threads are unread. The total drops when you mark a conversation read with `POST /conversations/{id}/read`.
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

client.sms.conversations.unread_count()

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

<details><summary><code>client.sms.conversations.<a href="src/vobiz/sms/conversations/client.py">get_conversation</a>(...) -> Conversation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one conversation with its participants, channel and counters. Use it to refresh a thread's `unreadCount` or `lastMessageAt` after a new message arrives. To read the messages themselves, call `GET /conversations/{id}/messages`.
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

client.sms.conversations.get_conversation(
    id="c7d1e9a3-2b4f-4a6c-8d5e-1f3a9b7c2e04",
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

**id:** `str` — The conversation `id` (UUID), from `GET /conversations` or the `conversationId` on any message.
    
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

<details><summary><code>client.sms.conversations.<a href="src/vobiz/sms/conversations/client.py">list_conversation_messages</a>(...) -> typing.List[Message]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the messages in one conversation, in both directions, newest first. Use it to render a chat thread: reverse the page to show it oldest to newest. The response is a bare JSON array of message objects without `statusHistory`; call `GET /messages/{id}` for one message's history. Page with `limit` and `offset`.
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

client.sms.conversations.list_conversation_messages(
    id="c7d1e9a3-2b4f-4a6c-8d5e-1f3a9b7c2e04",
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

**id:** `str` — The conversation `id` (UUID), from `GET /conversations` or the `conversationId` on any message.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of messages to return, from `1` to `100`. Defaults to `50`; a value outside that range also returns `50`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of messages to skip before the page starts, `0` or greater. Defaults to `0`. Add the page size to it to load older messages.
    
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

<details><summary><code>client.sms.conversations.<a href="src/vobiz/sms/conversations/client.py">mark_conversation_read</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks a conversation as read: it sets `unreadCount` to `0` and `lastReadAt` to the current time. Call it when a user opens the thread in your inbox. It takes no request body, and calling it on a thread that is already read is harmless. The account-wide total from `GET /conversations/unread-count` drops by the thread's previous `unreadCount`.
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

client.sms.conversations.mark_conversation_read(
    id="c7d1e9a3-2b4f-4a6c-8d5e-1f3a9b7c2e04",
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

**id:** `str` — The conversation `id` (UUID) to mark as read.
    
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

## Opt-outs
<details><summary><code>client.sms.opt_outs.<a href="src/vobiz/sms/opt_outs/client.py">list_opt_outs</a>(...) -> typing.Optional[typing.List[OptOut]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the numbers on your opt-out list, newest first, including entries created from STOP, START and HELP keyword replies and the ones you added. Pass both `limit` and `offset` on every call: the response is a bare JSON array, and it is `null` when the page has no records (including when `limit` is missing). Page by increasing `offset` until a page returns fewer items than `limit` or `null`. To check a single number, use `GET /opt-outs/{phoneNumber}` instead.
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

client.sms.opt_outs.list_opt_outs(
    limit=1,
    offset=1,
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

**limit:** `int` — Required. Maximum number of opt-outs to return, `1` or greater. Without it the response is `null`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `int` — Required. Number of records to skip before the page starts. Pass `0` for the first page, then add `limit` for each following page.
    
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

<details><summary><code>client.sms.opt_outs.<a href="src/vobiz/sms/opt_outs/client.py">create_opt_out</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a phone number to your opt-out list for one channel, so Vobiz stops messages to it. After this, `POST /messages` to that number on that channel returns `422` and broadcasts skip it. An `sms` opt-out also blocks `mms`. Use it to record consent withdrawn outside a keyword reply, for example on a call or a web form. Creating the same number and channel again updates the stored `reason` instead of adding a second record.
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

client.sms.opt_outs.create_opt_out(
    phone_number="+14155550123",
    channel="sms",
    reason="customer request",
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

**phone_number:** `str` — Required. The phone number to block, in E.164 format, for example `+14155550123`.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Channel to block: `sms`, `mms` or `rcs`. Defaults to `sms`. An `sms` opt-out also blocks `mms`.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `typing.Optional[str]` — Free-text note stored on the record, for example `customer request`. Defaults to `manual`. Repeating the request for the same number and channel replaces it.
    
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

<details><summary><code>client.sms.opt_outs.<a href="src/vobiz/sms/opt_outs/client.py">check_opt_out</a>(...) -> OptOutCheck</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Tells you whether a phone number is on your opt-out list for a channel. Call it before a send to skip a blocked contact instead of handling a `422` from `POST /messages`. The response is always `200` with `optedOut` set to `true` or `false`.
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

client.sms.opt_outs.check_opt_out(
    phone_number="+14155550123",
    channel="sms",
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

**phone_number:** `str` — The number in E.164 format, for example `+14155550123`. In raw HTTP requests, URL-encode the `+` as `%2B` (`/opt-outs/%2B14155550123`); the SDKs encode it for you.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Channel to check: `sms`, `mms` or `rcs`. Defaults to `sms`.
    
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

<details><summary><code>client.sms.opt_outs.<a href="src/vobiz/sms/opt_outs/client.py">delete_opt_out</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a phone number from your opt-out list for one channel, so you can message it again on that channel. Do this only after the contact has given consent again, for example after they reply `START`. The response is `200` whether or not a record existed, so it is safe to retry. Removing an opt-out on one channel leaves entries on other channels in place; delete each one separately.
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

client.sms.opt_outs.delete_opt_out(
    phone_number="+14155550123",
    channel="sms",
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

**phone_number:** `str` — The number in E.164 format, for example `+14155550123`. In raw HTTP requests, URL-encode the `+` as `%2B` (`/opt-outs/%2B14155550123`); the SDKs encode it for you.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[str]` — Channel to remove the opt-out from: `sms`, `mms` or `rcs`. Defaults to `sms`.
    
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

## Webhooks
<details><summary><code>client.sms.webhooks.<a href="src/vobiz/sms/webhooks/client.py">list_webhooks</a>() -> typing.Optional[typing.List[WebhookSubscription]]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all of your webhook subscriptions, newest first, as a bare JSON array. The body is `null` rather than `[]` when you have none, so treat `null` as an empty list. The response includes each subscription's `secret`, so keep it out of logs and client-side code.
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

client.sms.webhooks.list_webhooks()

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

<details><summary><code>client.sms.webhooks.<a href="src/vobiz/sms/webhooks/client.py">create_webhook</a>(...) -> WebhookSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers an HTTPS endpoint that receives the events you subscribe to as signed `POST` requests. Only `url` is required; omit `events` to subscribe to `message.received`, `message.delivered` and `message.failed`. Every delivery carries `X-Webhook-ID`, `X-Webhook-Event` and `X-Webhook-Signature`, a lower-case hex HMAC-SHA256 of the raw body keyed with your `secret`. The subscription is active as soon as it is created; see the Webhooks guide for the payload envelope and a verification example.
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

client.sms.webhooks.create_webhook(
    url="https://example.com/vobiz/webhooks",
    secret="YOUR_WEBHOOK_SECRET",
    events=[
        "message.received",
        "message.delivered",
        "message.failed"
    ],
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

**url:** `str` — The HTTPS URL that receives `POST` deliveries, for example `https://example.com/vobiz/webhooks`. Required; an empty or missing value returns `400` with `url is required`.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — Shared secret used to compute `X-Webhook-Signature` on every delivery. Choose a long random value and store it on your server; if you omit it the subscription is created with an empty secret.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[WebhookEvent]]` — Event names to deliver to this URL, matched exactly. Defaults to `message.received`, `message.delivered` and `message.failed` when you omit it or send an empty array.
    
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

<details><summary><code>client.sms.webhooks.<a href="src/vobiz/sms/webhooks/client.py">get_webhook</a>(...) -> WebhookSubscription</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one webhook subscription with its URL, events, `active` flag and signing secret. Use it to confirm the result of an update, since `PUT /webhooks/{id}` returns only `{"status":"ok"}`.
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

client.sms.webhooks.get_webhook(
    id="2a4c6e8f-1b3d-4f5a-8c7e-9d0b2f4a6c8e",
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

**id:** `str` — The subscription `id` (UUID) returned when you created it or by `GET /webhooks`.
    
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

<details><summary><code>client.sms.webhooks.<a href="src/vobiz/sms/webhooks/client.py">update_webhook</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes any subset of `url`, `secret`, `events` and `active`. Fields you omit keep their current value; a field you send, including an empty string, replaces it. Set `active` to `false` to pause deliveries without losing the subscription, and back to `true` to resume. The response is `{"status":"ok"}`, so call `GET /webhooks/{id}` to read the updated subscription.
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

client.sms.webhooks.update_webhook(
    id="2a4c6e8f-1b3d-4f5a-8c7e-9d0b2f4a6c8e",
    events=[
        "message.delivered",
        "message.failed"
    ],
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

**id:** `str` — The subscription `id` (UUID) to change.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — New HTTPS URL for deliveries. Replaces the current URL as sent, so always send a full valid URL.
    
</dd>
</dl>

<dl>
<dd>

**secret:** `typing.Optional[str]` — New signing secret for `X-Webhook-Signature`. Deliveries are signed with the new value from this point, so update your verifier at the same time.
    
</dd>
</dl>

<dl>
<dd>

**events:** `typing.Optional[typing.List[WebhookEvent]]` — New list of event names to deliver, matched exactly. Replaces the whole list; it is not merged with the current events.
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` — `false` pauses deliveries and keeps the subscription; `true` resumes them.
    
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

<details><summary><code>client.sms.webhooks.<a href="src/vobiz/sms/webhooks/client.py">delete_webhook</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the subscription and stops all deliveries to its URL. The response is `200` with `{"status":"ok"}`. To stop deliveries temporarily and keep the configuration, set `active` to `false` with `PUT /webhooks/{id}` instead.
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

client.sms.webhooks.delete_webhook(
    id="2a4c6e8f-1b3d-4f5a-8c7e-9d0b2f4a6c8e",
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

**id:** `str` — The subscription `id` (UUID) to delete.
    
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

## Broadcasts
<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">list_broadcasts</a>(...) -> BroadcastList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the broadcasts on your account, newest first, each with freshly counted `stats`. The response wraps the page in `broadcasts` and gives the account-wide count in `total`, so you can page with `limit` and `offset` until `offset` reaches `total`.
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

client.sms.broadcasts.list_broadcasts()

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

**limit:** `typing.Optional[int]` — Maximum number of broadcasts to return, from 1 to 500. Defaults to 50 when you omit it or pass `0`. A value above 500 returns `400` with `limit must be between 1 and 500`, and a non-integer returns `400` with `limit must be an integer`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of broadcasts to skip before the page starts, for paging through results with `limit`. Defaults to `0`. A negative value returns `400` with `offset must be >= 0`, and a non-integer returns `400` with `offset must be an integer`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">create_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a broadcast in `draft` status with zero `stats` and no recipients. Only `name` and `from` are required; `channel` defaults to `sms` and `ratePerSecond` to 5. Nothing is sent when you create a broadcast. Next, upload recipients with `POST /broadcasts/{id}/recipients`, check the rendered text with `GET /broadcasts/{id}/preview`, then start sending with `POST /broadcasts/{id}/launch`.
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

client.sms.broadcasts.create_broadcast(
    name="October pricing update",
    from_="+14155550100",
    template="Hi {{name}}, your refund of {{amount}} is on its way.",
    rate_per_second=5,
    tag="pricing-oct",
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

**name:** `typing.Optional[str]` — A label for the broadcast in the console and in listings, 1 to 255 characters. Required on create; on update it cannot be set to an empty string.
    
</dd>
</dl>

<dl>
<dd>

**from:** `typing.Optional[str]` — The sender every message goes out from: an SMS number on your account in E.164 format, a short code of up to 8 digits, or an alphanumeric sender ID of 1 to 11 letters, digits and spaces that starts with a letter or digit. Spaces, hyphens and brackets in phone numbers are removed before storing. Launch checks that a phone-number sender is an SMS number on your account. Required on create.
    
</dd>
</dl>

<dl>
<dd>

**channel:** `typing.Optional[BroadcastUpdateInputChannel]` — The channel the broadcast sends on. Broadcasts send SMS, so the only value is `sms` (matched case-insensitively), which is also the default.
    
</dd>
</dl>

<dl>
<dd>

**template:** `typing.Optional[str]` — Message body, up to 5,000 characters, with `{{variable}}` placeholders filled per recipient from the columns of your upload. Placeholder names are matched case-insensitively and trimmed, so `{{ Name }}` matches a `name` column. Launch requires a non-empty template.
    
</dd>
</dl>

<dl>
<dd>

**scheduled_at:** `typing.Optional[datetime.datetime]` — RFC 3339 timestamp at which sending starts after you launch, for example `2026-11-01T09:00:00Z`; offsets are converted to UTC. Omit it, or pass `null` or `""`, to send as soon as you launch. On update, `null` clears a previous value.
    
</dd>
</dl>

<dl>
<dd>

**rate_per_second:** `typing.Optional[int]` — Maximum messages sent per second while the broadcast runs, an integer from 1 to 50. Defaults to 5, and `0` also selects the default. Lower it to spread load on your own systems or replies.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[str]` — Your own label of up to 255 characters, copied onto every message the broadcast sends so you can find them with the `tag` filter on `GET /messages`.
    
</dd>
</dl>

<dl>
<dd>

**dlt_entity_id:** `typing.Optional[str]` — India (TRAI DLT). The Principal Entity ID you registered on a TRAI DLT portal, up to 64 characters. Pass it when the list contains Indian numbers; it is copied onto every message.
    
</dd>
</dl>

<dl>
<dd>

**dlt_header_id:** `typing.Optional[str]` — India (TRAI DLT). The sender header ID you registered on a TRAI DLT portal, up to 64 characters. Copied onto every message.
    
</dd>
</dl>

<dl>
<dd>

**dlt_template_id:** `typing.Optional[str]` — India (TRAI DLT). The content template ID you registered on a TRAI DLT portal, up to 64 characters. Your template text must match the registered template with the variables filled.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">get_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one broadcast with its configuration, current `status` and freshly counted `stats`. Poll it while a broadcast runs to follow progress, or subscribe to the `broadcast.updated` WebSocket event. For per-recipient results, use `GET /broadcasts/{id}/recipients` or `GET /broadcasts/{id}/export`.
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

client.sms.broadcasts.get_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">update_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Changes a `draft` broadcast. Send only the fields you want to change; fields you leave out, or send as `null`, keep their value, except `scheduledAt`, where `null` or `""` clears a scheduled start. The same validation as create applies, so `name` and `from` cannot be set to an empty string. A broadcast in any other status returns `409` with `cannot edit a broadcast that is <status>`.
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

client.sms.broadcasts.update_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
    template="Hi {{name}}, your refund of {{amount}} has been issued.",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `BroadcastUpdateInput` 
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">delete_broadcast</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently removes a `draft` or `cancelled` broadcast together with its recipient list and returns `204` with no body. Any other status returns `409` with `cannot delete a broadcast that is <status>`, so cancel a scheduled, running or paused broadcast first. Completed broadcasts are kept as your sending record.
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

client.sms.broadcasts.delete_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">list_recipients</a>(...) -> BroadcastRecipientList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the broadcast's recipients in upload order, each with its template `variables` and per-recipient send state. Filter by `status` to find failures, opted-out numbers or rows still waiting to send. The response gives the page in `recipients` and the count matching your filter in `total`. For a downloadable file of the same data, use `GET /broadcasts/{id}/export`.
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

client.sms.broadcasts.list_recipients(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[ListRecipientsRequestStatus]` — Return only recipients in this state, matched case-insensitively. `pending` waits to send, `sending` is in progress, `sent` and `delivered` track the message, `failed` has an `errorCode`, `opted_out` was excluded because the number opted out, and `skipped` was still pending when the broadcast was cancelled. Omit it to return every recipient; any other value returns `400`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of recipients to return, from 1 to 500. Defaults to 50 when you omit it or pass `0`. A value above 500 returns `400` with `limit must be between 1 and 500`, and a non-integer returns `400` with `limit must be an integer`.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of recipients to skip before the page starts, for paging through results with `limit`. Defaults to `0`. A negative value returns `400` with `offset must be >= 0`, and a non-integer returns `400` with `offset must be an integer`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">upload_recipients</a>(...) -> UploadResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets the recipient list of a `draft` broadcast; each upload replaces the previous list. Send `multipart/form-data` with a `.csv` or `.xlsx` `file` (10 MB maximum) to use template variables from extra columns, or JSON with a `numbers` array for a plain list. Numbers without a country code are normalised to E.164 with `defaultCountry` (default `US`). Duplicates are dropped, invalid rows are reported in `invalid`, and numbers that opted out of SMS from you are kept with status `opted_out` and never sent. A broadcast can hold up to 10,000 recipients; a larger list returns `422`.
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

client.sms.broadcasts.upload_recipients(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
    numbers=[
        "+14155550123",
        "+14155550124",
        "415 555 0125"
    ],
    default_country="US",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
</dd>
</dl>

<dl>
<dd>

**numbers:** `typing.List[str]` — Phone numbers, one per recipient, up to 10,000. Numbers without a country code are normalised with `defaultCountry`. An empty array clears the list.
    
</dd>
</dl>

<dl>
<dd>

**default_country:** `typing.Optional[UploadRecipientsJsonDefaultCountry]` — ISO 3166-1 alpha-2 country code, matched case-insensitively, used to normalise numbers that have no country code. Defaults to `US`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">preview_broadcast</a>(...) -> BroadcastPreview</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Renders the template for the first pending recipients so you can check personalisation, encoding and segment counts before you launch. Nothing is sent and nothing is charged. `missingVariables` lists placeholders that have no matching upload column; they render as empty text, so fix the template or re-upload before launching. `estimatedSegments` totals the segments across every pending recipient, not only the samples shown.
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

client.sms.broadcasts.preview_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of pending recipients to render in `samples`, from 1 to 50. Defaults to 5 when you omit it or pass `0`. A value above 50 returns `400` with `limit must be between 1 and 50`, and a non-integer returns `400` with `limit must be an integer`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">export_broadcast</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads every recipient with its send result as a CSV file (`text/csv`), named `broadcast-<id>.csv`. The columns are `row`, `to`, `status`, `message_id`, `error_code`, `error_message` and `sent_at`, followed by one column per column of your upload. Text cells that start with `=`, `+`, `-`, `@`, a tab or a carriage return are prefixed with `'` so they open safely in spreadsheet applications. You can export a broadcast in any status, including a draft, to check the parsed list.
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

client.sms.broadcasts.export_broadcast(
    id="id",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">launch_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts sending. This sends real SMS to every `pending` recipient and charges your account per segment, so call it only with your own credentials on a list you have consent to message. Only a `draft` can be launched; it moves to `running`, or to `scheduled` when `scheduledAt` is in the future. Launch returns `422` when the template is empty, when no recipient is pending, or when a phone-number `from` is not an SMS number on your account. Each recipient is sent like `POST /messages` with the broadcast's `tag` and DLT IDs and the idempotency key `broadcast:<broadcastId>:<recipientId>`, so no recipient is messaged twice.
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

client.sms.broadcasts.launch_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">pause_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Pauses a `running` broadcast. Sending stops after the messages already in flight, and pending recipients stay `pending` until you resume or cancel. Any other status returns `409` with `cannot pause a broadcast that is <status>`.
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

client.sms.broadcasts.pause_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">resume_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Continues sending to the pending recipients of a `paused` broadcast and moves it back to `running`. This sends real messages and charges your account per segment. It also resumes a broadcast paused with `pauseReason` `insufficient_balance` once you have topped up. Any other status returns `409` with `cannot resume a broadcast that is <status>`.
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

client.sms.broadcasts.resume_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

<details><summary><code>client.sms.broadcasts.<a href="src/vobiz/sms/broadcasts/client.py">cancel_broadcast</a>(...) -> Broadcast</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops a broadcast for good and sets `completedAt`. You can cancel from `draft`, `scheduled`, `running` or `paused`; a `completed`, `failed` or already `cancelled` broadcast returns `409`. Pending recipients become `skipped`, and messages already sent are unaffected. A cancelled broadcast cannot be resumed or edited, but it can be deleted.
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

client.sms.broadcasts.cancel_broadcast(
    id="3f8d2a6e-5b1c-4e7f-a9d0-2c4b6e8f1a35",
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

**id:** `str` — The broadcast's `id` (UUID), as returned by `POST /broadcasts` or `GET /broadcasts`. An id that is not a UUID, or that belongs to another account, returns `404` with `broadcast not found`.
    
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

## RCS Senders
<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">list_senders</a>(...) -> typing.List[Sender]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the RCS senders on your account as a bare JSON array, without a total count. Page through them with `limit` and `offset`; an empty array means you have reached the end. `status` here is the last stored value, so call `GET /senders/{id}/status` for the latest state.
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

client.sms.rcs_senders.list_senders()

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

**limit:** `typing.Optional[int]` — Maximum number of items to return, from 1 to 100. Defaults to 20; a value outside that range or a non-integer is replaced by the default.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before the page starts. Defaults to `0`. Pass a whole number of 0 or more.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">create_sender</a>(...) -> Sender</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a new RCS sender (agent) with the RCS platform and stores it on your account with status `pending`. `provider` and `senderName` are required; the profile fields are reviewed by the RCS platform and the carriers before the sender can reach real users. Poll `GET /senders/{id}/status` until the platform reports it as launched, then send with its `senderName` as `from` and `channel: rcs` on `POST /messages`. A rejected request returns `400` with the platform's reason in `error`.
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
from vobiz.sms import SenderBrand, SenderPhone, SenderEmail, SenderWebsite, SenderLink

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sms.rcs_senders.create_sender(
    provider="YOUR_ROUTING_IDENTIFIER",
    sender_name="example-brand",
    display_name="Example Brand",
    description="Order updates and support for Example Brand customers.",
    billing_category="CONVERSATIONAL",
    use_case="TRANSACTIONAL",
    hosting_region="NORTH_AMERICA",
    brand=SenderBrand(
        brand_name="Example Brand",
    ),
    color="#1A73E8",
    phones=[
        SenderPhone(
            phone_number="+14155550100",
            label="Support",
        )
    ],
    emails=[
        SenderEmail(
            address="support@example.com",
            label="Support",
        )
    ],
    websites=[
        SenderWebsite(
            url="https://example.com",
            label="Website",
        )
    ],
    banner_url="https://example.com/rcs/banner.jpg",
    logo_url="https://example.com/rcs/logo.png",
    privacy=SenderLink(
        url="https://example.com/privacy",
        label="Privacy policy",
    ),
    terms_of_service=SenderLink(
        url="https://example.com/terms",
        label="Terms of service",
    ),
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

**provider:** `str` — The routing identifier your account was provisioned with for RCS. Contact support if you are unsure which value to use; an unknown value returns `400`.
    
</dd>
</dl>

<dl>
<dd>

**sender_name:** `str` — Unique technical name of the sender on the RCS platform. You pass it as `from` when you send RCS, and it cannot be changed later.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The brand name recipients see at the top of the conversation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Short description of your business or the sender's purpose, shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**billing_category:** `typing.Optional[str]` — How the RCS platform bills conversations from this sender. Values accepted by the platform include `CONVERSATIONAL` and `NON_CONVERSATIONAL`.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[str]` — The kind of traffic the sender carries, reviewed by the RCS platform. Values accepted by the platform include `OTP`, `TRANSACTIONAL`, `PROMOTIONAL` and `MULTI_USE`.
    
</dd>
</dl>

<dl>
<dd>

**hosting_region:** `typing.Optional[str]` — The region where the RCS platform hosts the sender. Values accepted by the platform include `NORTH_AMERICA`, `EUROPE` and `ASIA_PACIFIC`. Cannot be changed later.
    
</dd>
</dl>

<dl>
<dd>

**brand:** `typing.Optional[SenderBrand]` — The brand the sender represents.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Accent colour for the sender's buttons and header, as a hex code such as `#1A73E8`.
    
</dd>
</dl>

<dl>
<dd>

**phones:** `typing.Optional[typing.List[SenderPhone]]` — Contact phone numbers shown on the sender's info page, each with a label.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.List[SenderEmail]]` — Contact email addresses shown on the sender's info page, each with a label.
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.List[SenderWebsite]]` — Websites shown on the sender's info page, each with a label.
    
</dd>
</dl>

<dl>
<dd>

**banner_url:** `typing.Optional[str]` — Publicly reachable HTTPS URL of the banner image shown at the top of the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — Publicly reachable HTTPS URL of the logo shown next to every message.
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `typing.Optional[SenderLink]` — Link to your privacy policy, shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**terms_of_service:** `typing.Optional[SenderLink]` — Link to your terms of service, shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**platform:** `typing.Optional[SenderPlatform]` — Identifiers the RCS platform has already assigned to your agent, if you have any.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">get_sender</a>(...) -> Sender</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one RCS sender as stored on your account, including its full profile. `status` is the last value stored on your account; call `GET /senders/{id}/status` to refresh it from the RCS platform. An unknown id returns `404`.
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

client.sms.rcs_senders.get_sender(
    id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
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

**id:** `str` — The sender's `id` (UUID), as returned by `POST /senders` or `GET /senders`. An unknown id returns `sender not found`.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">update_sender</a>(...) -> Sender</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates the sender's profile on the RCS platform and then on your account, and returns the updated sender. Send only the fields you want to change; fields you leave out keep their value. `provider`, `senderName` and `hostingRegion` are fixed after creation. Every failure, including an unknown id, returns `400`.
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
from vobiz.sms import SenderWebsite

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sms.rcs_senders.update_sender(
    id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
    display_name="Example Brand Support",
    description="Order updates, returns and support for Example Brand customers.",
    websites=[
        SenderWebsite(
            url="https://example.com/help",
            label="Help centre",
        )
    ],
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

**id:** `str` — The sender's `id` (UUID), as returned by `POST /senders` or `GET /senders`. An unknown id returns `sender not found`.
    
</dd>
</dl>

<dl>
<dd>

**display_name:** `typing.Optional[str]` — The brand name recipients see at the top of the conversation.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Short description of your business or the sender's purpose, shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**billing_category:** `typing.Optional[str]` — How the RCS platform bills conversations from this sender, for example `CONVERSATIONAL` or `NON_CONVERSATIONAL`.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[str]` — The kind of traffic the sender carries, for example `OTP`, `TRANSACTIONAL`, `PROMOTIONAL` or `MULTI_USE`.
    
</dd>
</dl>

<dl>
<dd>

**brand:** `typing.Optional[SenderBrand]` — The brand the sender represents.
    
</dd>
</dl>

<dl>
<dd>

**color:** `typing.Optional[str]` — Accent colour for the sender's buttons and header, as a hex code such as `#1A73E8`.
    
</dd>
</dl>

<dl>
<dd>

**phones:** `typing.Optional[typing.List[SenderPhone]]` — Contact phone numbers shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**emails:** `typing.Optional[typing.List[SenderEmail]]` — Contact email addresses shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**websites:** `typing.Optional[typing.List[SenderWebsite]]` — Websites shown on the sender's info page.
    
</dd>
</dl>

<dl>
<dd>

**banner_url:** `typing.Optional[str]` — Publicly reachable HTTPS URL of the banner image.
    
</dd>
</dl>

<dl>
<dd>

**logo_url:** `typing.Optional[str]` — Publicly reachable HTTPS URL of the logo image.
    
</dd>
</dl>

<dl>
<dd>

**privacy:** `typing.Optional[SenderLink]` — Link to your privacy policy.
    
</dd>
</dl>

<dl>
<dd>

**terms_of_service:** `typing.Optional[SenderLink]` — Link to your terms of service.
    
</dd>
</dl>

<dl>
<dd>

**platform:** `typing.Optional[SenderPlatform]` — Identifiers the RCS platform has assigned to your agent.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">get_sender_status</a>(...) -> Sender</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asks the RCS platform for the sender's current launch status, stores it on the sender and returns the full sender. Poll it after `POST /senders` or a profile update until `status` shows the sender is live, then start sending. Every failure, including an unknown id, returns `400`.
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

client.sms.rcs_senders.get_sender_status(
    id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
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

**id:** `str` — The sender's `id` (UUID), as returned by `POST /senders` or `GET /senders`. An unknown id returns `sender not found`.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">list_templates</a>(...) -> typing.List[Template]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the templates registered on one RCS sender as a bare JSON array, without a total count. Page through them with `limit` and `offset`. `status` is the last stored value; refresh one template with its `/status` endpoint.
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

client.sms.rcs_senders.list_templates(
    sender_id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
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

**sender_id:** `str` — The `id` (UUID) of the RCS sender that owns the templates. An unknown sender returns `sender not found`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return, from 1 to 100. Defaults to 20; a value outside that range or a non-integer is replaced by the default.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before the page starts. Defaults to `0`. Pass a whole number of 0 or more.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">create_template</a>(...) -> Template</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Registers a message template on an RCS sender with the RCS platform and returns it with status `pending`. `templateName`, `type` and `content` are passed to the platform unchanged, so use the template types and content shapes the RCS platform defines. Call `GET /senders/{senderId}/templates/{templateName}/status` to follow approval. An unknown sender or a platform rejection returns `400`.
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

client.sms.rcs_senders.create_template(
    sender_id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
    template_name="order-shipped",
    type="TEXT",
    content={
        "text": "Your order {{orderId}} has shipped and arrives on {{eta}}."
    },
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

**sender_id:** `str` — The `id` (UUID) of the RCS sender that owns the templates. An unknown sender returns `sender not found`.
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — Unique name for the template on this sender. You use it in the path of every template endpoint.
    
</dd>
</dl>

<dl>
<dd>

**type:** `str` — Template type as defined by the RCS platform. It decides which `content` shape the platform expects.
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Dict[str, typing.Any]` — Template content as a JSON object in the shape the RCS platform defines for the chosen `type`. Stored and returned exactly as you submit it.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">get_template</a>(...) -> Template</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one template as stored on your account, including the `content` you submitted. For the latest approval state from the RCS platform, call `GET /senders/{senderId}/templates/{templateName}/status`. An unknown sender or template returns `404`.
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

client.sms.rcs_senders.get_template(
    sender_id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
    template_name="appointment_reminder",
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

**sender_id:** `str` — The `id` (UUID) of the RCS sender that owns the templates. An unknown sender returns `sender not found`.
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template's `templateName`, exactly as you set it when you created the template on this sender.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">delete_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes the template from the RCS platform and from your account, and returns `204` with no body. You cannot send with the template afterwards. An unknown sender or template returns `400`.
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

client.sms.rcs_senders.delete_template(
    sender_id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
    template_name="appointment_reminder",
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

**sender_id:** `str` — The `id` (UUID) of the RCS sender that owns the templates. An unknown sender returns `sender not found`.
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template's `templateName`, exactly as you set it when you created the template on this sender.
    
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

<details><summary><code>client.sms.rcs_senders.<a href="src/vobiz/sms/rcs_senders/client.py">get_template_status</a>(...) -> Template</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asks the RCS platform for the template's current approval status, stores it on the template and returns the full template. Poll it after `POST /senders/{senderId}/templates` until the template is approved. Every failure, including an unknown sender or template, returns `400`.
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

client.sms.rcs_senders.get_template_status(
    sender_id="5d7f9b1c-3e5a-4c7e-9f1b-3d5f7a9c1e3b",
    template_name="appointment_reminder",
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

**sender_id:** `str` — The `id` (UUID) of the RCS sender that owns the templates. An unknown sender returns `sender not found`.
    
</dd>
</dl>

<dl>
<dd>

**template_name:** `str` — The template's `templateName`, exactly as you set it when you created the template on this sender.
    
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

## Brands
<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">list_brands</a>() -> typing.List[Brand]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every brand on your account as a bare JSON array, newest first. The list is not paginated and reads the records stored on your account without contacting the registry; deleted brands are left out. Call `GET /10dlc/brands/{id}` for the latest registry state of one brand.
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

client.sms.brands.list_brands()

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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">create_brand</a>(...) -> Brand</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a brand, the business identity that US carriers associate with your 10DLC traffic, and mirrors it to the US 10DLC registry in `DRAFT` stage. `name` and `brandType` are required; send every other field your business has, because the registry reviews them when you register. Nothing is submitted for review until you call `POST /10dlc/brands/{id}/register`. Pass a `referenceId` so that a retried request (for example after a `502`) reconciles to the same brand instead of creating a second one. Next, register the brand, then create a campaign under it with `POST /10dlc/campaigns`.
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
from vobiz.sms import BrandAddress

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sms.brands.create_brand(
    reference_id="brand-example-corp-01",
    name="Example Corp",
    legal_name="Example Corporation Inc.",
    brand_type="TENDLC_PRIVATE_COMPANY",
    website="https://example.com",
    support_email="support@example.com",
    support_phone="+14155550100",
    vertical="TECHNOLOGY",
    tax_id="12-3456789",
    tax_id_issuing_country="US",
    country_code="US",
    address=BrandAddress(
        street="100 Example Street",
        city="San Francisco",
        state="CA",
        zip_code="94105",
    ),
    business_contact_first_name="Alex",
    business_contact_last_name="Doe",
    business_contact_email="alex.doe@example.com",
    legal_entity_type="PRIVATE_COMPANY",
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

**request:** `CreateBrandRequest` 
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">get_brand</a>(...) -> Brand</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one brand after refreshing its `stage`, `registrationStatus`, `brandIdentityStatus` and `rejectionReasons` from the US 10DLC registry. The refresh is best-effort: if the registry is slow to answer, you get the stored record and `lastSyncedAt` tells you how fresh it is. Poll this endpoint (or listen for the `10dlc.brand.updated` WebSocket event) after registering to follow the review.
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

client.sms.brands.get_brand(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">update_brand</a>(...) -> Brand</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the brand with the body you send and pushes the change to the US 10DLC registry. This is a full replacement, not a patch: send the same shape as create, including `name` and `brandType`, and any field you leave out is cleared. `referenceId` is ignored on update. Use it to correct a brand before registering it, or to fix the points listed in `rejectionReasons` before resubmitting.
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
from vobiz.sms import BrandAddress

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sms.brands.update_brand(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
    name="Example Corp",
    legal_name="Example Corporation Inc.",
    brand_type="TENDLC_PRIVATE_COMPANY",
    website="https://example.com",
    support_email="help@example.com",
    support_phone="+14155550100",
    vertical="TECHNOLOGY",
    tax_id="12-3456789",
    tax_id_issuing_country="US",
    country_code="US",
    address=BrandAddress(
        street="100 Example Street",
        city="San Francisco",
        state="CA",
        zip_code="94105",
    ),
    business_contact_first_name="Alex",
    business_contact_last_name="Doe",
    business_contact_email="alex.doe@example.com",
    legal_entity_type="PRIVATE_COMPANY",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CreateBrandRequest` 
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">delete_brand</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the brand from your account and from the US 10DLC registry and returns `204` with no body. A brand that still owns campaigns returns `409` with `conflict: brand still has N campaign(s); delete them first`, so delete or deregister its campaigns first. Deletion cannot be undone; a new brand needs a new registration.
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

client.sms.brands.delete_brand(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">register_brand</a>(...) -> Brand</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits the brand to the US 10DLC registry for identity verification. The brand moves from `DRAFT` to `SUBMITTED` and `registrationStatus` starts tracking the registrar's decision (`PENDING`, then `ACTIVE` or `REJECTED`). The request has no body and returns the refreshed brand. Submit only when the brand details are final and you intend to register this business. Follow progress with `GET /10dlc/brands/{id}` or `GET /10dlc/brands/{id}/registrar-statuses`.
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

client.sms.brands.register_brand(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">brand_registrar_statuses</a>(...) -> typing.List[BrandRegistrarStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the brand's state at each registrar that has reviewed it, read live from the US 10DLC registry. Each entry carries the registrar's `state` and, when the registrar reports them, the identity result, the authentication status and a rejection reason. An empty array means no registrar has recorded a state yet. Use it to see why a brand is pending or rejected.
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

client.sms.brands.brand_registrar_statuses(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">brand_auth_verification</a>(...) -> BrandAuthRequested</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts the registry's brand authentication for a brand whose `brandType` is `TENDLC_PUBLIC_COMPANY`. The registry sends a two-factor verification request to the brand's `businessContactEmail`, and the brand shows `registrationStatus` `PENDING_2FA` until the contact completes it. The request has no body and returns `202` with `{"status":"requested"}`. Any other brand type returns `400` with `invalid request: brand authentication is only available for TENDLC_PUBLIC_COMPANY brands`.
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

client.sms.brands.brand_auth_verification(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">resend2fa</a>(...) -> BrandAuthRequested</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asks the registry to send the brand-authentication verification again to the brand's `businessContactEmail`. Use it when a `TENDLC_PUBLIC_COMPANY` brand is `PENDING_2FA` and the contact did not receive or let the first request expire. The request has no body and returns `202` with `{"status":"requested"}`. Any other brand type returns `400`.
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

client.sms.brands.resend2fa(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">vet_brand</a>(...) -> RegistryRecord</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Requests an external vet of a registered brand from the US 10DLC registry. A successful vet can raise the brand's trust tier and, with it, the throughput carriers grant its campaigns. `type` defaults to `STANDARD`; any value other than `STANDARD`, `ENHANCED` or `POLITICAL` returns `400`. Every call files a new vetting request, so send it only when you intend to. The response is the registry's vetting record, returned as received; list past vets with `GET /10dlc/brands/{id}/vets`.
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

client.sms.brands.vet_brand(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
    type="STANDARD",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[BrandVetRequestType]` — Kind of vet to request: `STANDARD` (the default), `ENHANCED` (a deeper review) or `POLITICAL` (for political organisations). Case-insensitive; any other value returns `400` with `invalid request: type must be one of STANDARD, ENHANCED, POLITICAL`.
    
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

<details><summary><code>client.sms.brands.<a href="src/vobiz/sms/brands/client.py">list_brand_vets</a>(...) -> BrandVetList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the brand's vetting records from the US 10DLC registry, one page at a time. The body is `{"results": [...], "paging": {...}}`, where each result is a registry vetting record passed through as received. `page` must be 0 or more and `size` between 0 and 100; other values return `400` with `page must be >= 0 and size between 0 and 100`.
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

client.sms.brands.list_brand_vets(
    id="8e6c4a2f-0d9b-4b7a-a5c3-1e9f7d5b3a10",
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

**id:** `str` — Brand ID (UUID) returned by `POST /10dlc/brands`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"brand not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**page:** `typing.Optional[int]` — Zero-based page index. Defaults to `0`. Must be 0 or more; a negative value returns `400`. A value that is not an integer is treated as `0`.
    
</dd>
</dl>

<dl>
<dd>

**size:** `typing.Optional[int]` — Records per page, from 0 to 100. Defaults to `20`; `0` or a value that is not an integer also gives the default page size. A value above 100 returns `400`.
    
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

## Campaigns
<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">list_campaigns</a>() -> typing.List[Campaign]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every 10DLC and toll-free campaign on your account as a bare JSON array, newest first. The list is not paginated and reads the records stored on your account without contacting the registry. Toll-free campaigns have `campaignType` `TOLL_FREE_UNIFIED_NUMBER` and no `brandId`. Call `GET /10dlc/campaigns/{id}` for the latest registry state of one campaign.
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

client.sms.campaigns.list_campaigns()

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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">create_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a 10DLC campaign, the messaging program you run under one of your brands, and mirrors it to the US 10DLC registry in `DRAFT` stage. `name` and `brandId` are required; `campaignType` defaults to `TEN_DIGIT_LONG_CODE`. Upload any `supportingDocuments` or `mmsSampleFiles` with `POST /10dlc/documents` first. Pass a `referenceId` so a retried request reconciles to the same campaign. Next, submit the campaign with `POST /10dlc/campaigns/{id}/register`; toll-free verification uses `POST /10dlc/campaigns/toll-free` instead.
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

client.sms.campaigns.create_campaign(
    name="Example Corp account alerts",
    program_summary="Example Corp sends account and support alerts to customers who opted in on the sign-up form. Reply STOP to opt out, HELP for help.",
    confirmation_message="Example Corp: You are subscribed to account alerts. Msg frequency varies. Msg & data rates may apply. Reply HELP for help, STOP to opt out.",
    help_message="Example Corp: For help email support@example.com. Reply STOP to opt out.",
    stop_message="Example Corp: You have been unsubscribed. Reply HELP for help.",
    customer_care_phone="+14155550100",
    customer_care_email="support@example.com",
    terms_and_conditions_url="https://example.com/terms",
    privacy_policy_url="https://example.com/privacy",
    example_messages=[
        "Example Corp: Your support ticket #48213 was updated. View it at https://example.com/support. Reply STOP to opt out.",
        "Example Corp: Your account balance is low. Add funds at https://example.com/wallet. Reply STOP to opt out."
    ],
    use_cases=[
        "ALERTS"
    ],
    message_types=[
        "SMS"
    ],
    opt_ins={
        "web": {"url": "https://example.com/signup", "callToAction": "By checking this box you agree to receive account alerts from Example Corp. Msg frequency varies. Msg & data rates may apply. Reply STOP to opt out, HELP for help."}
    },
    low_volume=True,
    embedded_link=True,
    numbers=[
        "14155550100"
    ],
    reference_id="campaign-account-alerts-01",
    brand_id="5f1c3a2e-7b4d-4e8f-9a0b-1c2d3e4f5a60",
    campaign_type="TEN_DIGIT_LONG_CODE",
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

**brand_id:** `str` — Required. ID of the brand from `POST /10dlc/brands` that runs this campaign. A missing, unknown or non-UUID value returns `404` with `{"error":"brand not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for the campaign, for your reference. Required on create and on update.
    
</dd>
</dl>

<dl>
<dd>

**program_summary:** `typing.Optional[str]` — Plain-language description of the program: what you send, to whom, how often and how recipients opt in. Reviewers read this first.
    
</dd>
</dl>

<dl>
<dd>

**confirmation_message:** `typing.Optional[str]` — Message you send when a recipient opts in. Include your brand name and how to get help or opt out.
    
</dd>
</dl>

<dl>
<dd>

**help_message:** `typing.Optional[str]` — Reply you send when a recipient texts HELP. Include your brand name and a way to reach support.
    
</dd>
</dl>

<dl>
<dd>

**stop_message:** `typing.Optional[str]` — Reply you send when a recipient texts STOP, confirming they will receive no further messages.
    
</dd>
</dl>

<dl>
<dd>

**customer_care_phone:** `typing.Optional[str]` — Customer care phone number for the program, in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**customer_care_email:** `typing.Optional[str]` — Customer care email address for the program.
    
</dd>
</dl>

<dl>
<dd>

**terms_and_conditions_url:** `typing.Optional[str]` — Public URL of the terms and conditions that cover the program.
    
</dd>
</dl>

<dl>
<dd>

**privacy_policy_url:** `typing.Optional[str]` — Public URL of your privacy policy.
    
</dd>
</dl>

<dl>
<dd>

**example_messages:** `typing.Optional[typing.List[str]]` — Sample messages exactly as the campaign will send them, including your brand name and opt-out language. Cover each use case you list.
    
</dd>
</dl>

<dl>
<dd>

**use_cases:** `typing.Optional[typing.List[str]]` — Use-case codes the campaign covers. Values accepted by the US 10DLC registry: `TWO_FACTOR_AUTH`, `ALERTS`, `FRAUD_ALERTS`, `CHAT`, `PROMOTIONAL_MARKETING`, `EDUCATION`, `DONATION`, `PUBLIC_SERVICE_ANNOUNCEMENT`, `VOTING_POLLING`, `POLITICAL`, `M2M`, `SWEEPSTAKE`.
    
</dd>
</dl>

<dl>
<dd>

**message_types:** `typing.Optional[typing.List[str]]` — Message types the campaign sends, for example `SMS` and `MMS`.
    
</dd>
</dl>

<dl>
<dd>

**opt_ins:** `typing.Optional[typing.Dict[str, typing.Any]]` — How recipients give consent, as an object keyed by opt-in channel (for example `web`, `keyword`, `paper`). Each entry describes that flow, for example `url` and `callToAction` for `web`; the object is passed to the registry as given.
    
</dd>
</dl>

<dl>
<dd>

**low_volume:** `typing.Optional[bool]` — Declares the campaign as low volume to the registry. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**age_gated:** `typing.Optional[bool]` — Set `true` when the content is restricted to adults. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**direct_lending:** `typing.Optional[bool]` — Set `true` when the content relates to direct lending or loan arrangements. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**embedded_link:** `typing.Optional[bool]` — Set `true` when messages contain URLs. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**embedded_phone:** `typing.Optional[bool]` — Set `true` when messages contain phone numbers. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**numbers:** `typing.Optional[typing.List[str]]` — Numbers on your account to attach to the campaign, as digits with country code and no `+` (for example `14155550100`).
    
</dd>
</dl>

<dl>
<dd>

**supporting_documents:** `typing.Optional[typing.List[str]]` — `documentId` values of supporting documents uploaded with `POST /10dlc/documents`. Every ID must be on your account, otherwise the request returns `400`.
    
</dd>
</dl>

<dl>
<dd>

**mms_sample_files:** `typing.Optional[typing.List[str]]` — `documentId` values of MMS sample files uploaded with `POST /10dlc/documents`. Every ID must be on your account, otherwise the request returns `400`.
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Your own idempotency reference. Repeating a create with the same value reconciles to the same campaign instead of creating a second one. Ignored on update.
    
</dd>
</dl>

<dl>
<dd>

**campaign_type:** `typing.Optional[CreateCampaignRequestCampaignType]` — Kind of campaign. Defaults to `TEN_DIGIT_LONG_CODE`, the standard 10DLC campaign. Toll-free types return `400`; use `POST /10dlc/campaigns/toll-free` for those.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">create_toll_free_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Starts toll-free verification for one or more toll-free numbers. The business details travel inside the request, so no brand is needed; only `name` is required, but the registry reviews every field you send. The campaign is created with `campaignType` `TOLL_FREE_UNIFIED_NUMBER` and no `brandId`. Pass a `referenceId` so a retried request reconciles to the same campaign, then submit it with `POST /10dlc/campaigns/{id}/register`.
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
from vobiz.sms import BrandAddress

client = Vobiz(
    api_key="<value>",
    auth_token="<X-Auth-Token>",
    environment=VobizEnvironment.PRODUCTION,
)

client.sms.campaigns.create_toll_free_campaign(
    reference_id="tollfree-notifications-01",
    name="Example Corp toll-free notifications",
    privacy_policy_url="https://example.com/privacy",
    terms_and_conditions_url="https://example.com/terms",
    message_volume="TEN_THOUSAND",
    numbers=[
        "+18335550100"
    ],
    use_case="NOTIFICATIONS",
    program_summary="Example Corp sends account and support notifications to customers who opted in on the contact form. Reply STOP to opt out, HELP for help.",
    example_message="Example Corp: Your account balance is low. Add funds at https://example.com/wallet. Reply STOP to opt out, HELP for help.",
    opt_ins={
        "web": {"url": "https://example.com/contact", "callToAction": "By checking this box you agree to receive account notifications from Example Corp. Reply STOP to opt out, HELP for help."}
    },
    opt_in_image_ur_ls=[
        "https://example.com/opt-in-screenshot.png"
    ],
    country_code="US",
    address=BrandAddress(
        street="100 Example Street",
        city="San Francisco",
        state="CA",
        zip_code="94105",
    ),
    support_phone="+14155550100",
    support_email="support@example.com",
    business_contact_first_name="Alex",
    business_contact_last_name="Doe",
    legal_name="Example Corporation Inc.",
    business_name="Example Corp",
    business_website="https://example.com",
    customer_care_email="support@example.com",
    tax_id="12-3456789",
    tax_id_issuing_country="US",
    legal_entity_type="PRIVATE_COMPANY",
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

**name:** `str` — Name for the toll-free campaign, for your reference. Required (`400` with `invalid request: name is required` otherwise).
    
</dd>
</dl>

<dl>
<dd>

**reference_id:** `typing.Optional[str]` — Your own idempotency reference. Repeating a create with the same value reconciles to the same campaign instead of creating a second one.
    
</dd>
</dl>

<dl>
<dd>

**privacy_policy_url:** `typing.Optional[str]` — Public URL of your privacy policy.
    
</dd>
</dl>

<dl>
<dd>

**terms_and_conditions_url:** `typing.Optional[str]` — Public URL of the terms and conditions that cover the program.
    
</dd>
</dl>

<dl>
<dd>

**message_volume:** `typing.Optional[str]` — Expected monthly message volume. Values accepted by the US 10DLC registry: `HUNDRED`, `TEN_THOUSAND`, `TWO_HUNDRED_FIFTY_THOUSAND`, `SEVEN_HUNDRED_FIFTY_THOUSAND`, `FIVE_MILLION`.
    
</dd>
</dl>

<dl>
<dd>

**numbers:** `typing.Optional[typing.List[str]]` — Toll-free numbers on your account to verify, in E.164 format (for example `+18885550100`).
    
</dd>
</dl>

<dl>
<dd>

**number_keys:** `typing.Optional[typing.List[str]]` — Registry number keys of the numbers to verify, as an alternative to `numbers`.
    
</dd>
</dl>

<dl>
<dd>

**use_case:** `typing.Optional[str]` — Main use case of the program. Values accepted by the US 10DLC registry: `TWO_FACTOR_AUTH`, `NOTIFICATIONS`, `SYSTEM_ALERTS`, `APP_NOTIFICATIONS`, `BANKING`, `BOOKING_CONFIRMATIONS`, `CHATBOT`, `COURIER_SERVICES_DELIVERIES`, `EMERGENCY_ALERTS`, `EVENTS_PLANNING`, `FRAUD_ALERTS`, `GENERAL_MARKETING`, `HEALTHCARE`, `INSURANCE_SERVICES`, `LEGAL_SERVICES`, `MOTIVATIONAL_REMINDERS`, `POLITICAL`, `REAL_ESTATE_SERVICES`, `RELIGIOUS_SERVICES`, `REWARDS_PROGRAM`, `WEBINAR_REMINDERS`, `AUCTIONS`, `COVID_19_ALERTS`.
    
</dd>
</dl>

<dl>
<dd>

**program_summary:** `typing.Optional[str]` — Plain-language description of the program: what you send, to whom, how often and how recipients opt in.
    
</dd>
</dl>

<dl>
<dd>

**example_message:** `typing.Optional[str]` — A sample message exactly as you will send it, including your brand name and opt-out language.
    
</dd>
</dl>

<dl>
<dd>

**opt_ins:** `typing.Optional[typing.Dict[str, typing.Any]]` — How recipients give consent, as an object keyed by opt-in channel (for example `web` with `url` and `callToAction`). Passed to the registry as given.
    
</dd>
</dl>

<dl>
<dd>

**opt_in_image_ur_ls:** `typing.Optional[typing.List[str]]` — Public URLs of screenshots or images that show the opt-in flow to the reviewer.
    
</dd>
</dl>

<dl>
<dd>

**additional_information:** `typing.Optional[str]` — Anything else the reviewer should know about the program, in plain text.
    
</dd>
</dl>

<dl>
<dd>

**country_code:** `typing.Optional[str]` — ISO 3166-1 alpha-2 code of the country where the business is registered.
    
</dd>
</dl>

<dl>
<dd>

**address:** `typing.Optional[BrandAddress]` — Postal address of the business as it appears on its registration records.
    
</dd>
</dl>

<dl>
<dd>

**support_phone:** `typing.Optional[str]` — Support phone number for the business, in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**support_email:** `typing.Optional[str]` — Support email address for the business.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_first_name:** `typing.Optional[str]` — First name of the person the reviewer can contact about the business.
    
</dd>
</dl>

<dl>
<dd>

**business_contact_last_name:** `typing.Optional[str]` — Last name of the person the reviewer can contact about the business.
    
</dd>
</dl>

<dl>
<dd>

**legal_name:** `typing.Optional[str]` — Registered legal name of the business, exactly as it appears on tax records.
    
</dd>
</dl>

<dl>
<dd>

**business_dba:** `typing.Optional[str]` — Trading name ("doing business as") when it differs from `legalName`. Note the casing `businessDBA` on this endpoint, unlike `businessDba` on brands.
    
</dd>
</dl>

<dl>
<dd>

**business_name:** `typing.Optional[str]` — Business name customers know you by.
    
</dd>
</dl>

<dl>
<dd>

**business_website:** `typing.Optional[str]` — Business website. It must be live and match the business.
    
</dd>
</dl>

<dl>
<dd>

**customer_care_email:** `typing.Optional[str]` — Customer care email address for the program.
    
</dd>
</dl>

<dl>
<dd>

**tax_id:** `typing.Optional[str]` — Tax identifier of the business, for example the US EIN.
    
</dd>
</dl>

<dl>
<dd>

**tax_id_issuing_country:** `typing.Optional[str]` — ISO 3166-1 alpha-2 code of the country that issued `taxId`.
    
</dd>
</dl>

<dl>
<dd>

**legal_entity_type:** `typing.Optional[str]` — Legal form of the business. Values accepted by the US 10DLC registry: `PRIVATE_COMPANY`, `PUBLIC_COMPANY`, `NON_PROFIT`, `GOVERNMENT`, `SOLE_PROPRIETOR`.
    
</dd>
</dl>

<dl>
<dd>

**business_registration_type:** `typing.Optional[str]` — Type of registration number for a business outside the US. Values accepted by the US 10DLC registry: `VAT`, `CBN`, `PROVINCIAL_NUMBER`, `ABN`, `SIREN`, `NZBN`, `CIF`, `CNPJ`, `OTHER`.
    
</dd>
</dl>

<dl>
<dd>

**campaign_verify_token:** `typing.Optional[str]` — Campaign Verify token for a US political program. Omit it for every other program.
    
</dd>
</dl>

<dl>
<dd>

**priority_id:** `typing.Optional[str]` — ID (UUID) of a priority option from `GET /10dlc/campaigns/priorities`. A value that is not a UUID returns `400`; omit it when the list is empty.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">campaign_priorities</a>() -> typing.List[PriorityOption]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the priority options available to your account at the US 10DLC registry, as a JSON array. Pass an option's `id` as `priorityId` when you create or register a toll-free campaign. An empty array means no priority options apply to your account, and you can omit `priorityId`.
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

client.sms.campaigns.campaign_priorities()

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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">get_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns one campaign after refreshing its `stage` and review feedback (`rejectionReasons`) from the US 10DLC registry. If the registry is slow to answer, you get the stored record and `lastSyncedAt` tells you how fresh it is. Poll this endpoint (or listen for the `10dlc.campaign.updated` WebSocket event) after registering until `stage` settles at `REGISTERED` or `REJECTED`.
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

client.sms.campaigns.get_campaign(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">update_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replaces the editable fields of a 10DLC campaign and pushes the change to the US 10DLC registry. This is a full replacement: `name` is required and any field you leave out is cleared. `campaignType` and the brand stay as created, and `referenceId` is ignored. The registry accepts updates while the campaign is `DRAFT` or `REJECTED`. Toll-free campaigns return `400` on this endpoint.
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

client.sms.campaigns.update_campaign(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
    name="Example Corp account alerts",
    program_summary="Example Corp sends account, billing and support alerts to customers who opted in on the sign-up form. Reply STOP to opt out, HELP for help.",
    confirmation_message="Example Corp: You are subscribed to account alerts. Msg frequency varies. Msg & data rates may apply. Reply HELP for help, STOP to opt out.",
    help_message="Example Corp: For help email support@example.com. Reply STOP to opt out.",
    stop_message="Example Corp: You have been unsubscribed. Reply HELP for help.",
    customer_care_phone="+14155550100",
    customer_care_email="support@example.com",
    terms_and_conditions_url="https://example.com/terms",
    privacy_policy_url="https://example.com/privacy",
    example_messages=[
        "Example Corp: Your support ticket #48213 was updated. View it at https://example.com/support. Reply STOP to opt out."
    ],
    use_cases=[
        "ALERTS"
    ],
    message_types=[
        "SMS"
    ],
    opt_ins={
        "web": {"url": "https://example.com/signup", "callToAction": "By checking this box you agree to receive account alerts from Example Corp. Msg frequency varies. Msg & data rates may apply. Reply STOP to opt out, HELP for help."}
    },
    low_volume=True,
    embedded_link=True,
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Name for the campaign, for your reference. Required on create and on update.
    
</dd>
</dl>

<dl>
<dd>

**program_summary:** `typing.Optional[str]` — Plain-language description of the program: what you send, to whom, how often and how recipients opt in. Reviewers read this first.
    
</dd>
</dl>

<dl>
<dd>

**confirmation_message:** `typing.Optional[str]` — Message you send when a recipient opts in. Include your brand name and how to get help or opt out.
    
</dd>
</dl>

<dl>
<dd>

**help_message:** `typing.Optional[str]` — Reply you send when a recipient texts HELP. Include your brand name and a way to reach support.
    
</dd>
</dl>

<dl>
<dd>

**stop_message:** `typing.Optional[str]` — Reply you send when a recipient texts STOP, confirming they will receive no further messages.
    
</dd>
</dl>

<dl>
<dd>

**customer_care_phone:** `typing.Optional[str]` — Customer care phone number for the program, in E.164 format.
    
</dd>
</dl>

<dl>
<dd>

**customer_care_email:** `typing.Optional[str]` — Customer care email address for the program.
    
</dd>
</dl>

<dl>
<dd>

**terms_and_conditions_url:** `typing.Optional[str]` — Public URL of the terms and conditions that cover the program.
    
</dd>
</dl>

<dl>
<dd>

**privacy_policy_url:** `typing.Optional[str]` — Public URL of your privacy policy.
    
</dd>
</dl>

<dl>
<dd>

**example_messages:** `typing.Optional[typing.List[str]]` — Sample messages exactly as the campaign will send them, including your brand name and opt-out language. Cover each use case you list.
    
</dd>
</dl>

<dl>
<dd>

**use_cases:** `typing.Optional[typing.List[str]]` — Use-case codes the campaign covers. Values accepted by the US 10DLC registry: `TWO_FACTOR_AUTH`, `ALERTS`, `FRAUD_ALERTS`, `CHAT`, `PROMOTIONAL_MARKETING`, `EDUCATION`, `DONATION`, `PUBLIC_SERVICE_ANNOUNCEMENT`, `VOTING_POLLING`, `POLITICAL`, `M2M`, `SWEEPSTAKE`.
    
</dd>
</dl>

<dl>
<dd>

**message_types:** `typing.Optional[typing.List[str]]` — Message types the campaign sends, for example `SMS` and `MMS`.
    
</dd>
</dl>

<dl>
<dd>

**opt_ins:** `typing.Optional[typing.Dict[str, typing.Any]]` — How recipients give consent, as an object keyed by opt-in channel (for example `web`, `keyword`, `paper`). Each entry describes that flow, for example `url` and `callToAction` for `web`; the object is passed to the registry as given.
    
</dd>
</dl>

<dl>
<dd>

**low_volume:** `typing.Optional[bool]` — Declares the campaign as low volume to the registry. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**age_gated:** `typing.Optional[bool]` — Set `true` when the content is restricted to adults. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**direct_lending:** `typing.Optional[bool]` — Set `true` when the content relates to direct lending or loan arrangements. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**embedded_link:** `typing.Optional[bool]` — Set `true` when messages contain URLs. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**embedded_phone:** `typing.Optional[bool]` — Set `true` when messages contain phone numbers. Defaults to `false`.
    
</dd>
</dl>

<dl>
<dd>

**numbers:** `typing.Optional[typing.List[str]]` — Numbers on your account to attach to the campaign, as digits with country code and no `+` (for example `14155550100`).
    
</dd>
</dl>

<dl>
<dd>

**supporting_documents:** `typing.Optional[typing.List[str]]` — `documentId` values of supporting documents uploaded with `POST /10dlc/documents`. Every ID must be on your account, otherwise the request returns `400`.
    
</dd>
</dl>

<dl>
<dd>

**mms_sample_files:** `typing.Optional[typing.List[str]]` — `documentId` values of MMS sample files uploaded with `POST /10dlc/documents`. Every ID must be on your account, otherwise the request returns `400`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">delete_campaign</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes the campaign from your account and from the US 10DLC registry and returns `204` with no body. The registry accepts deletion while the campaign is `DRAFT`, `DEREGISTERED` or `REJECTED`; deregister a registered campaign with `POST /10dlc/campaigns/{id}/deregister` first. Delete all of a brand's campaigns before you delete the brand.
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

client.sms.campaigns.delete_campaign(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">register_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits the campaign to the US 10DLC registry for review and returns the refreshed campaign. The `stage` moves out of `DRAFT`; poll `GET /10dlc/campaigns/{id}` until it settles at `REGISTERED` or `REJECTED`. The body is optional and carries a `priorityId` from `GET /10dlc/campaigns/priorities` for toll-free campaigns; a value that is not a UUID returns `400`. Submit only when the campaign details are final and you intend to run this program.
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

client.sms.campaigns.register_campaign(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
    priority_id="2c9e4b7a-1d3f-4a5b-8c6d-0e9f8a7b6c5d",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**priority_id:** `typing.Optional[str]` — ID (UUID) of a priority option from `GET /10dlc/campaigns/priorities`, for toll-free campaigns. A value that is not a UUID returns `400` with `invalid request: priorityId must be a UUID`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">deregister_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Withdraws a registered campaign from the US 10DLC registry and returns the campaign. Once deregistration completes, traffic on the campaign's numbers is no longer covered by this registration, so move the numbers to another registered campaign first if you keep sending. The request has no body. A deregistered campaign can then be deleted with `DELETE /10dlc/campaigns/{id}`.
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

client.sms.campaigns.deregister_campaign(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">appeal_campaign</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asks the US 10DLC registry to reconsider a `REJECTED` campaign and returns the campaign after the appeal is filed. Fix the campaign with `PUT /10dlc/campaigns/{id}` first, then explain what changed in `reason`, which is required (`400` with `invalid request: reason is required` otherwise). Follow the outcome with `GET /10dlc/campaigns/{id}`.
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

client.sms.campaigns.appeal_campaign(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
    reason="Updated the program summary and opt-in call to action to match the brand\'s registered details.",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**reason:** `str` — Required. Explains why the campaign should be reconsidered and what you changed; address every point in the campaign's `rejectionReasons`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">update_campaign_registration</a>(...) -> Campaign</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asks the US 10DLC registry to update the set of numbers covered by a registered campaign, without deregistering it. Provide `numbers`, `numberKeys`, or both; if both are empty the call returns `400` with `invalid request: numbers or numberKeys is required`. The response is the campaign; the `numbers` list stored on your account is left as it was. Use `POST` and `DELETE /10dlc/campaigns/{id}/numbers` for incremental changes.
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

client.sms.campaigns.update_campaign_registration(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
    numbers=[
        "14155550100",
        "14155550101"
    ],
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CampaignNumbersRequest` 
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">campaign_network_statuses</a>(...) -> typing.List[CampaignNetworkStatus]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the campaign's status at each US carrier network, read live from the US 10DLC registry. Each entry names the network and its `state`, plus the message class, throughput and brand tier when the network reports them. Use it after the campaign reaches `REGISTERED` to see which networks have provisioned it and what throughput they grant.
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

client.sms.campaigns.campaign_network_statuses(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">list_campaign_numbers</a>(...) -> CampaignNumberList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the numbers attached to the campaign at the US 10DLC registry, as `{"numberPreviews": [...]}`. Each entry gives the number, its country and the registry `numberKey`, which you can pass in `numberKeys` on the number endpoints. Use it to confirm which numbers the registry associates with the campaign.
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

client.sms.campaigns.list_campaign_numbers(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">add_campaign_numbers</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Attaches numbers to the campaign at the US 10DLC registry and adds the `numbers` values to the campaign's `numbers` list on your account. Provide `numbers`, `numberKeys`, or both; if both are empty the call returns `400`. Returns `200` with `{"status":"ok"}`. Attach only numbers on your account that you send this program from.
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

client.sms.campaigns.add_campaign_numbers(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
    numbers=[
        "14155550101"
    ],
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CampaignNumbersRequest` 
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">remove_campaign_numbers</a>(...) -> StatusOk</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Detaches numbers from the campaign at the US 10DLC registry and removes the `numbers` values from the campaign's `numbers` list on your account. Send `numbers`, `numberKeys`, or both in the `DELETE` request body; if both are empty the call returns `400`. Returns `200` with `{"status":"ok"}`. Messages from a detached number are no longer covered by this campaign.
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

client.sms.campaigns.remove_campaign_numbers(
    id="4c2a0e8d-6b4f-4d2c-b0a8-9e7c5a3f1d24",
    numbers=[
        "14155550101"
    ],
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

**id:** `str` — Campaign ID (UUID) returned by `POST /10dlc/campaigns` or `POST /10dlc/campaigns/toll-free`. An unknown ID, an ID from another account, or a value that is not a UUID returns `404` with `{"error":"campaign not found"}`.
    
</dd>
</dl>

<dl>
<dd>

**request:** `CampaignNumbersRequest` 
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">upload_document</a>(...) -> Document</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uploads a supporting document or MMS sample file for campaign registration and stores it at the US 10DLC registry. Send `multipart/form-data` with the file in a part named `document` that carries a filename; the file can be up to 10 MB (`413` above that). The response is the document record; reference its `documentId` in a campaign's `supportingDocuments` or `mmsSampleFiles`, and use the same value to download it again.
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

client.sms.campaigns.upload_document(
    document="example_document",
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

**document:** `core.File` — The file to upload, as the `document` part of a `multipart/form-data` body. The part must include a filename; a missing part returns `400` with `multipart field "document" is required`. Maximum 10 MB.
    
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

<details><summary><code>client.sms.campaigns.<a href="src/vobiz/sms/campaigns/client.py">get_document</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Downloads a document you uploaded with `POST /10dlc/documents`. The response body is the file itself, with the file's own `Content-Type` and a `Content-Disposition: attachment` header that carries the original filename. Look the file up by its `documentId`, not by the record `id`.
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

client.sms.campaigns.get_document(
    id="id",
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

**id:** `str` — The `documentId` (UUID) returned by `POST /10dlc/documents`, not the record `id`. A value that is not a UUID, or a document that is not on your account, returns `404` with `{"error":"document not found"}`.
    
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

