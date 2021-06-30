from collections import namedtuple


KeyboardEvent = namedtuple('Response', 'initialize, pause, finish, started')


keyboard_event_mapper = KeyboardEvent(
    initialize='a', pause='q', finish='f', started=None
    )

