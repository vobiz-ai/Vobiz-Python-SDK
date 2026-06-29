"""Base element + serialization for the Vobiz call-control XML builder.

Modeled on Plivo's ``plivoxml`` (``ResponseElement`` + ``add_*`` builder methods +
``to_string()``), but emits VobizXML verbs and attributes. Python kwargs are
snake_case and are converted to the camelCase attribute names VobizXML uses
(e.g. ``input_type`` -> ``inputType``, ``execution_timeout`` -> ``executionTimeout``).
"""

XML_DECLARATION = '<?xml version="1.0" encoding="UTF-8"?>'
_INDENT = "    "  # 4 spaces, matching the xml/*.mdx reference style


def to_camel(key):
    """snake_case kwarg -> camelCase XML attribute. A single trailing underscore is
    stripped so Python keywords can be passed as ``async_`` -> ``async``."""
    if key.endswith("_"):
        key = key[:-1]
    head, *rest = key.split("_")
    return head + "".join(p[:1].upper() + p[1:] for p in rest)


def attr_value(value):
    """Render an attribute value: bools -> 'true'/'false', everything else -> str."""
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def escape(text):
    """Escape XML text content."""
    return (
        str(text)
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def escape_attr(value):
    """Escape an attribute value (text rules plus double quotes)."""
    return escape(value).replace('"', "&quot;")


class VobizXMLElement:
    """A single VobizXML element. Holds an ordered attribute map, optional text
    content, and child elements. Subclasses set ``name`` and expose ``add_*`` helpers.
    """

    name = "Element"

    def __init__(self, content=None, raw=False, **attrs):
        self.content = content
        self.raw = raw  # if True, content is inserted without escaping (e.g. SSML)
        self.children = []
        self.attributes = {}
        for key, value in attrs.items():
            if value is None:
                continue
            self.attributes[to_camel(key)] = attr_value(value)

    def add(self, element):
        """Append a child element and return it (so callers can keep nesting)."""
        self.children.append(element)
        return element

    def set(self, **attrs):
        """Set/override attributes after construction; returns self for chaining."""
        for key, value in attrs.items():
            if value is None:
                continue
            self.attributes[to_camel(key)] = attr_value(value)
        return self

    def _open_tag(self):
        parts = [self.name]
        for key, value in self.attributes.items():
            parts.append('{}="{}"'.format(key, escape_attr(value)))
        return " ".join(parts)

    def _render(self, level, pretty):
        pad = _INDENT * level if pretty else ""
        open_tag = self._open_tag()

        # Empty element -> self-closing
        if not self.children and self.content is None:
            return "{}<{}/>".format(pad, open_tag)

        # Text-content element -> single line
        if not self.children:
            body = self.content if self.raw else escape(self.content)
            return "{}<{}>{}</{}>".format(pad, open_tag, body, self.name)

        # Container element -> children indented (content, if any, is ignored)
        if pretty:
            inner = "\n".join(c._render(level + 1, pretty) for c in self.children)
            return "{0}<{1}>\n{2}\n{0}</{3}>".format(pad, open_tag, inner, self.name)
        inner = "".join(c._render(level + 1, pretty) for c in self.children)
        return "<{0}>{1}</{2}>".format(open_tag, inner, self.name)

    def to_string(self, pretty=True):
        """Serialize to a VobizXML document string (with the XML declaration)."""
        body = self._render(0, pretty)
        return XML_DECLARATION + ("\n" if pretty else "") + body

    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return "<{} attrs={} children={}>".format(
            type(self).__name__, self.attributes, len(self.children)
        )
