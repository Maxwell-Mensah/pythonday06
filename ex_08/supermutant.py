from amonster import AMonster

class SuperMutant(AMonster):
    _num=1
    def __init__(self):
        super().__init__(name=f"SuperMutant {SuperMutant._num}", hp=170, ap=20, damage=60, apcost=20)
        SuperMutant._num+=1
        print(f"{self.name}: Roaarrr !")

    def receiveDamage(self, damage):
        self.hp-=damage
        if self.hp<=0:
            self.dead=True
            print(f"{self.name}: Urgh ! ")

    def recoverAP(self):
        if self.dead:
            return False
        self.ap+=10
        if self.ap>50:
            self.ap=50    