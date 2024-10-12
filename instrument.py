# Interfaz
from abc import ABC, abstractmethod

class Instrument(ABC):
    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def tune_up(self):
        pass
