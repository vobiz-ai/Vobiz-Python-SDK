"""vobizxml - build VobizXML call-control documents in Python.

Mirrors Plivo's ``plivoxml`` API so migrating code only changes the import and the
``GetDigits``/``GetInput`` -> ``Gather`` rename (aliases are provided so even that
keeps working).

    from vobiz import vobizxml

    r = vobizxml.ResponseElement()
    r.add_speak("Hello, world!")
    print(r.to_string())
    # <?xml version="1.0" encoding="UTF-8"?>
    # <Response>
    #     <Speak>Hello, world!</Speak>
    # </Response>
"""

from .base import VobizXMLElement
from .elements import (
    ResponseElement,
    SpeakElement,
    PlayElement,
    WaitElement,
    GatherElement,
    DialElement,
    NumberElement,
    UserElement,
    RecordElement,
    ConferenceElement,
    DtmfElement,
    RedirectElement,
    HangupElement,
    PreAnswerElement,
    StreamElement,
)

__version__ = "0.1.0"

__all__ = [
    "VobizXMLElement",
    "ResponseElement",
    "SpeakElement",
    "PlayElement",
    "WaitElement",
    "GatherElement",
    "DialElement",
    "NumberElement",
    "UserElement",
    "RecordElement",
    "ConferenceElement",
    "DtmfElement",
    "RedirectElement",
    "HangupElement",
    "PreAnswerElement",
    "StreamElement",
]
