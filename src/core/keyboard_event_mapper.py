from collections import namedtuple


KeyboardEventMapper = namedtuple("KeyboardEventMapper", "initialize, pause, finish")

Response = namedtuple("Response", "method, message")

key_mapper = KeyboardEventMapper(
    initialize="a", pause="q", finish="f"
)

