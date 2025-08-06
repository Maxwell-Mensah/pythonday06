from aspacemarine import ASpaceMarine
from powerfist import PowerFist

class AssaultTerminator(ASpaceMarine):
    def __init__(self):
        super().__init__(self, name, hp=150, ap=30, weapon=PowerFist)
        print(f"{self.name} has teleported form space")

    def receiveDamage(self, damage):
        damage-=3
        if damage<1:
            damage=1
        self.hp-=damage
        if self.hp<=0:
            self.dead=True
            print(f"BOUUUMMM ! {self.name} has exploded")