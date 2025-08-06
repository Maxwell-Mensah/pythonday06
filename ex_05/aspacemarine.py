from iunit import IUnit
from aweapon import AWeapon

class ASpaceMarine(IUnit):
    def __init__(self, name, hp=0, ap=0, weapon=None):
       self.name=name
       self.hp=hp
       self.ap=ap
       self.weapon=weapon
       self.dead=False

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAp(self):
        return self.ap

    def getWeapon(self):
        return self.weapon

    def equip(self, param):
        if self.dead:
            return False
        if isinstance(param, AWeapon):
            print(f"{self.name} has been equiped with a {param.name}")
        else:
            print("Error in ASpaceMarine. Parameter is not an AWeapon")

    def attack(self, param):
        if self.dead:
            return False
        if not isinstance(param, IUnit):
            print("Error in ASpaceMarine. Parameter is not an IUnit")
            return False
        if self.weapon==None:
            print(f"{self.name}: Hey, this is crazy. I'm not going to fight this empty handed")
        elif self.ap>=(self.weapon).apcost:
            print(f"{self.name} attacks {param.name} with a {self.weapon.name}")
            (self.weapon).attack()
            param.receiveDamage((self.weapon).damage)
            self.ap-=self.apcost

        

    def receiveDamage(self, damage):
        self.hp-=damage
        if self.hp<=0:
            self.dead=True
    
    def moveCloseTo(self, param):
        if self.dead:
            return False
        if not isinstance(param, IUnit):
            print("Error in ASpaceMarine. Parameter is not an IUnit")
            return None
        else:
            print(f"{self.name} is moving closer to {param.name}")

    
    def recoverAP(self):
        if self.dead:
            return False
        self.ap+=9
        if self.ap>50:
            self.ap=50