from aweapon import AWeapon

class PowerFist(AWeapon):
    def __init__(self):
        super().__init__(name="Power fist", apcost=8, damage=50, melee=True)
    
    def attack(self):
        print("SBAM")
