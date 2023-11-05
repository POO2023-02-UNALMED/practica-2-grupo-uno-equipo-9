from abc import ABC, abstractmethod

class Decimales(ABC):
    @staticmethod
    def dos_decimales(valor):
        return round(valor * 100.0) / 100.0

    @abstractmethod
    def redondear(self):
        pass
