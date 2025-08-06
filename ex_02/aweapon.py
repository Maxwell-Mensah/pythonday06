from abc import ABC, abstractmethod

class AWeapon(ABC):
    def __init__(self, name, apcost, damage, melee=False):
        if type(name).__name__!="str" or type(apcost).__name__!="int" or type(damage).__name__!="int" or type(melee).__name__!="bool":
            print("Error in AWeapon constructor, Bad parameters")
            return None
        self.name=name
        self.apcost=apcost
        self.damage=damage
        self.melee=melee

    def getName(self):
        return self.name

    def getApcost(self):
        return self.apcost
    
    def getDamage(self):
        return self.damage
    
    def isMelee(self):
        return self.melee

    @abstractmethod
    def attack(self):
        pass