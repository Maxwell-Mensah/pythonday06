from iunit import IUnit

class AMonster(IUnit):
    def __init__(self, name, hp=0, ap=0, damage=0, apcost=0, dead=False):
        self.name=name
        self.hp=hp
        self.ap=ap
        self.damage=damage
        self.apcost=apcost
        self.dead=False

    def getName(self):
        return self.name

    def getHp(self):
        return self.hp

    def getAp(self):
        return self.ap
    
    def getDamage(self):
        return self.damage

    def getApcost(self):
        return self.apcost

    def equip(self, param):
        print("Monsters are proud and fight with their own bodies.")

    def attack(self, param):
        if self.dead:
            return False

        if not isinstance(param, IUnit):
            print("Error in AMonster. Parameter is not an IUnit")
        
        else:
            if self.ap>=self.apcost:
                print(f"{self.name} attacks {param.name}")
                param.receiveDamage(self.damage)
                self.ap-=self.apcost
            else:
                print(f"{self.name}: I'm weak i can't attack")


    def receiveDamage(self, damage):
        self.hp-=damage
        if self.hp<=0:
            self.dead=True
    
    def moveCloseTo(self, param):
        if self.dead:
            return False
        if not isinstance(param, IUnit):
            print("Error in AMonster. Parameter is not an IUnit")
            return None
        else:
            print(f"{self.name} is moving closer to {param.name}")

    
    def recoverAP(self):
        if self.dead:
            return False
        self.ap+=7
        if self.ap>50:
            self.ap=50