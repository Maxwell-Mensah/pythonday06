from amonster import AMonster

class RadScorpion(AMonster):
    _num=1
    def __init__(self):
        super().__init__(name=f"RadScorpion #{RadScorpion._num}", hp=80, ap=50, damage=25, apcost=8)
        RadScorpion._num+=1
        print(f"{self.name}: Crrr !")

    def receiveDamage(self, damage):
        self.hp-=damage
        if self.hp<=0:
            self.dead=True
            print(f"{self.name}: SPROTCH !")
        
    def attack(self, param):
        if type(param).__name__=="ASpaceMarine" or type(param).__name__=="AssaultTerminator":
            if self.ap>=self.apcost:
                print(f"{self.name} attacks {param.name}")
                param.receiveDamage(self.damage * 2)
                self.ap-=self.apcost
        
        else:
            super().attack(param)