from abc import ABC, abstractmethod

class IUnit(ABC):
    
    @abstractmethod
    def equip(self, param):
        pass

    @abstractmethod
    def attack(self, param):
        pass

    @abstractmethod
    def receiveDamage(self, param):
        pass

    @abstractmethod
    def moveCloseTo(self, param):
        pass

    @abstractmethod
    def recoverAP(self):
        pass

    