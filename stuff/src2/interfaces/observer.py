from abc import ABC, abstractmethod

class ObserverInterface(ABC):
   @abstractmethod
   def update(self) -> None:
       ...



class ObservableInterface(ABC):
    @abstractmethod
    def subscribe(self, observer: ObserverInterface) -> None:
        ...

    @abstractmethod
    def notify(self) -> None:
        pass
