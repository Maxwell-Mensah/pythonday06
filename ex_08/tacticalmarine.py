from aspacemarine import ASpaceMarine
from plasmarifle import Plasmarifle

class TacticalMarine(ASpaceMarine):
    def __init__(self):
        super().__init__(self, name, hp=100, ap=20, weapon=Plasmarifle)
        print(f"{self.name} on duty")

    def receiveDamage(self, damage):
        self.hp-=damage
        if self.hp<=0:
            self.dead=True
            print(f"{self.name} the tactical Marine has fallen")

    def recoverAP(self):
        if self.dead:
            return False
        self.ap+=12
        if self.ap>50:
            self.ap=50    