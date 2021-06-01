#EVENTO -(TRANSFORMA)-> ESTADO

from collections import namedtuple


KeyboardEventResponseEntity = namedtuple('Response', 'initialize, pause, finish, started')


response = KeyboardEventResponseEntity(
    initialize='a', pause='q', finish='f', started=None
    )

