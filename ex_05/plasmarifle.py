from aweapon import AWeapon

class Plasmarifle(AWeapon):
    def __init__(self):
        super().__init__(name="Plasma Rifle", apcost=5, damage=21, melee=False)
    
    def attack(self):
        print("PIOU")
