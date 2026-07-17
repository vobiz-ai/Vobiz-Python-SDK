# Vobiz Python SDK - Usage Sheet

A practical cheat-sheet of the most common operations. For the exhaustive list of
every method and parameter, see [`reference.md`](./reference.md).

All snippets assume:

```python
from vobiz import Vobiz

client = Vobiz(api_key="YOUR_AUTH_ID", auth_token="YOUR_AUTH_TOKEN")
AUTH_ID = "YOUR_AUTH_ID"
```

---

## Calls

```python
# Make an outbound call
client.calls.make_call(
    auth_id=AUTH_ID,
    from_="14155551234",
    to="+919876543210",
    answer_url="https://example.com/answer",
    answer_method="POST",
)

# List live (in-progress) calls
client.live_calls.list_live_calls(auth_id=AUTH_ID)

# Get a single live call
client.live_calls.get_live_call(auth_id=AUTH_ID, call_uuid="CALL_UUID")

# Hang up a live call
client.live_calls.hangup_call(auth_id=AUTH_ID, call_uuid="CALL_UUID")
```

## In-call actions

```python
client.play_audio.call(auth_id=AUTH_ID, call_uuid="CALL_UUID", urls="https://cdn/audio.mp3")
client.speak_text.call(auth_id=AUTH_ID, call_uuid="CALL_UUID", text="Hello from Vobiz")
client.dtmf.send_dtmf(auth_id=AUTH_ID, call_uuid="CALL_UUID", digits="1234")
client.record_calls.start_recording(auth_id=AUTH_ID, call_uuid="CALL_UUID")
client.record_calls.stop_recording(auth_id=AUTH_ID, call_uuid="CALL_UUID")
```

## Call Detail Records (CDRs)

```python
client.cdr.list_cdrs(auth_id=AUTH_ID)
client.cdr.list_recent_cdrs(auth_id=AUTH_ID)
client.cdr.search_cdrs(auth_id=AUTH_ID)
client.cdr.get_cdr(auth_id=AUTH_ID, call_id="CALL_ID")
client.cdr.export_cdrs(auth_id=AUTH_ID)
```

## Recordings

```python
client.recordings.list_recordings(auth_id=AUTH_ID)
client.recordings.get_recording(auth_id=AUTH_ID, recording_id="REC_ID")
client.recordings.delete_recording(auth_id=AUTH_ID, recording_id="REC_ID")
```

## Phone Numbers

```python
client.phone_numbers.list_numbers(auth_id=AUTH_ID)                       # your numbers
client.phone_numbers.list_inventory_numbers(auth_id=AUTH_ID)             # available to buy
client.phone_numbers.purchase_from_inventory(auth_id=AUTH_ID, ...)
client.phone_numbers.assign_number_to_trunk(auth_id=AUTH_ID, ...)
client.phone_numbers.unrent_number(auth_id=AUTH_ID, ...)
```

## Applications

```python
client.applications.list_applications(auth_id=AUTH_ID)
client.applications.create_application(auth_id=AUTH_ID, ...)
client.applications.retrieve_application(auth_id=AUTH_ID, app_id="APP_ID")
client.applications.update_application(auth_id=AUTH_ID, app_id="APP_ID", ...)
client.applications.delete_application(auth_id=AUTH_ID, app_id="APP_ID")
```

## SIP Trunks & Endpoints

```python
client.trunks.list_trunks(auth_id=AUTH_ID)
client.trunks.create_trunk(auth_id=AUTH_ID, ...)
client.endpoints.list_endpoints(auth_id=AUTH_ID)
client.endpoints.create_endpoint(auth_id=AUTH_ID, ...)
client.credentials.list_credentials(auth_id=AUTH_ID)
```

## Conferences

```python
client.conferences.list_conferences(auth_id=AUTH_ID)
client.conferences.get_conference(auth_id=AUTH_ID, conference_name="my-room")
client.conference_members.mute_member(auth_id=AUTH_ID, conference_name="my-room", member_id="MEMBER")
client.conference.kick_member(auth_id=AUTH_ID, conference_name="my-room", member_id="MEMBER")
client.conference_recording.start_conference_recording(auth_id=AUTH_ID, conference_name="my-room")
```

## Account & Balance

```python
client.account.retrieve_account()
client.account.get_concurrency(auth_id=AUTH_ID)
client.balance.get_balance(auth_id=AUTH_ID, currency="INR")
client.balance.list_transactions(auth_id=AUTH_ID)
```

## Sub-accounts & KYC

```python
client.sub_accounts.list_subaccounts(auth_id=AUTH_ID)
client.sub_accounts.create_subaccount(auth_id=AUTH_ID, ...)
client.sub_account_kyc.get_subaccount_kyc_status(sub_auth_id="SUB_AUTH_ID")
client.sub_account_kyc.verify_subaccount_pan(sub_auth_id="SUB_AUTH_ID", ...)
```

---

> Exact required parameters per method are documented in [`reference.md`](./reference.md)
> and at https://docs.vobiz.ai. Most write methods accept the same fields shown in the
> REST API reference.
