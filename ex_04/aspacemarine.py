from iunit import IUnit

class ASpaceMarine(IUnit):
    def __init__(self, name, hp=0, ap=0):
       self.name=name
       self.hp=0
       self.ap=0


    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAp(self):
        return self.ap

    def equip(self, param):
        pass

    def attack(self, param):
        pass

    def receiveDamage(self, damage):
        pass

    def moveCloseTo(self, param):
        pass
    
    def recoverAP(self):
        pass