"""VobizXML element classes (mirrors plivoxml's element set, Vobiz verbs).

All ``add_*`` helpers return the created child so you can keep nesting, e.g.::

    from vobiz import vobizxml

    r = vobizxml.ResponseElement()
    g = r.add_gather(action="https://app/menu", input_type="dtmf",
                     num_digits=1, execution_timeout=10)
    g.add_speak("Press 1 for sales, 2 for support.")
    r.add_speak("We didn't receive your input. Goodbye.")
    r.add_hangup()
    print(r.to_string())

Attribute kwargs are snake_case and map to VobizXML's camelCase
(``input_type`` -> ``inputType``, ``execution_timeout`` -> ``executionTimeout``).
For ``<DTMF async="...">`` pass ``async_`` (Python keyword).
"""

from .base import VobizXMLElement


# --- Leaf / content elements -------------------------------------------------

class SpeakElement(VobizXMLElement):
    """<Speak> text-to-speech. Pass ``ssml=...`` to inject raw SSML unescaped."""

    name = "Speak"

    def __init__(self, content=None, ssml=None, **attrs):
        if ssml is not None:
            super().__init__(content=ssml, raw=True, **attrs)
        else:
            super().__init__(content=content, **attrs)


class PlayElement(VobizXMLElement):
    """<Play> a remote MP3/WAV URL (text content)."""

    name = "Play"

    def __init__(self, url=None, **attrs):
        super().__init__(content=url, **attrs)


class WaitElement(VobizXMLElement):
    """<Wait/> silent pause (self-closing)."""

    name = "Wait"


class NumberElement(VobizXMLElement):
    """<Number> a PSTN number to dial (nested in <Dial>)."""

    name = "Number"

    def __init__(self, number=None, **attrs):
        super().__init__(content=number, **attrs)


class UserElement(VobizXMLElement):
    """<User> a SIP endpoint to dial (nested in <Dial>)."""

    name = "User"

    def __init__(self, sip_uri=None, **attrs):
        super().__init__(content=sip_uri, **attrs)


class RecordElement(VobizXMLElement):
    """<Record/> record the call/leg (self-closing; ``action`` required)."""

    name = "Record"


class ConferenceElement(VobizXMLElement):
    """<Conference> join a room (room name is the text content)."""

    name = "Conference"

    def __init__(self, room=None, **attrs):
        super().__init__(content=room, **attrs)


class DtmfElement(VobizXMLElement):
    """<DTMF> send digits on a live call (digits are the text content)."""

    name = "DTMF"

    def __init__(self, digits=None, **attrs):
        super().__init__(content=digits, **attrs)


class RedirectElement(VobizXMLElement):
    """<Redirect> transfer flow control to a URL (text content)."""

    name = "Redirect"

    def __init__(self, url=None, **attrs):
        super().__init__(content=url, **attrs)


class HangupElement(VobizXMLElement):
    """<Hangup/> end/reject the call (self-closing)."""

    name = "Hangup"


class StreamElement(VobizXMLElement):
    """<Stream> fork audio to a WebSocket (wss URL is the text content)."""

    name = "Stream"

    def __init__(self, url=None, **attrs):
        super().__init__(content=url, **attrs)


# --- Mixins for the four containers that hold prompts/children ---------------

class _SpeakPlayMixin:
    def add_speak(self, content=None, ssml=None, **attrs):
        return self.add(SpeakElement(content, ssml=ssml, **attrs))

    def add_play(self, url=None, **attrs):
        return self.add(PlayElement(url, **attrs))


# --- Container elements ------------------------------------------------------

class GatherElement(_SpeakPlayMixin, VobizXMLElement):
    """<Gather> collect DTMF/speech input. Nest Speak/Play prompts inside."""

    name = "Gather"


class PreAnswerElement(_SpeakPlayMixin, VobizXMLElement):
    """<PreAnswer> early-media block. Nest Speak/Play/Wait inside."""

    name = "PreAnswer"

    def add_wait(self, **attrs):
        return self.add(WaitElement(**attrs))


class DialElement(VobizXMLElement):
    """<Dial> bridge the caller to Number/User endpoints; may nest Record."""

    name = "Dial"

    def __init__(self, number=None, **attrs):
        # plain number as shorthand text content is allowed but Number/User preferred
        super().__init__(content=number, **attrs)

    def add_number(self, number=None, **attrs):
        return self.add(NumberElement(number, **attrs))

    def add_user(self, sip_uri=None, **attrs):
        return self.add(UserElement(sip_uri, **attrs))

    def add_record(self, **attrs):
        return self.add(RecordElement(**attrs))


class ResponseElement(VobizXMLElement):
    """<Response> root container. Use the ``add_*`` helpers to build the document."""

    name = "Response"

    def add_speak(self, content=None, ssml=None, **attrs):
        return self.add(SpeakElement(content, ssml=ssml, **attrs))

    def add_play(self, url=None, **attrs):
        return self.add(PlayElement(url, **attrs))

    def add_wait(self, **attrs):
        return self.add(WaitElement(**attrs))

    def add_gather(self, **attrs):
        return self.add(GatherElement(**attrs))

    # Plivo-parity aliases: GetDigits/GetInput both map to <Gather>.
    def add_get_digits(self, **attrs):
        return self.add_gather(**attrs)

    def add_get_input(self, **attrs):
        return self.add_gather(**attrs)

    def add_dial(self, number=None, **attrs):
        return self.add(DialElement(number, **attrs))

    def add_record(self, **attrs):
        return self.add(RecordElement(**attrs))

    def add_conference(self, room=None, **attrs):
        return self.add(ConferenceElement(room, **attrs))

    def add_dtmf(self, digits=None, **attrs):
        return self.add(DtmfElement(digits, **attrs))

    def add_redirect(self, url=None, **attrs):
        return self.add(RedirectElement(url, **attrs))

    def add_hangup(self, **attrs):
        return self.add(HangupElement(**attrs))

    def add_preanswer(self):
        return self.add(PreAnswerElement())

    def add_stream(self, url=None, **attrs):
        return self.add(StreamElement(url, **attrs))
