from amonster import AMonster
from aspacemarine import ASpaceMarine

class SpaceArena():

    def __init__(self):
        self.monster_list=[]
        self.space_list=[]
    def enlistMonsters(self, monsters : list):
        for monst in monsters:
            if isinstance(monst, AMonster):
                if monst not in (self.monster_list):
                    (self.monster_list).append(monst)
            else:
                print("Stop trying to cheat !")

    

    def enlistSpaceMarines(self, space_marines : list):
        for marine in space_marines:
            if isinstance(marine, ASpaceMarine):
                if marine not in self.space_list:
                    (self.space_list).append(marine)
            else:
                print("Stop trying to cheat !")
    
    def fight(self):
        if len(self.monster_list)==0:
            print("No monster available to fight")
            return
        elif len(self.space_list)==0:
            print("Those cowards ran away")
            return
        else:
            while self.monster_list and self.space_list:
               f_mar=self.space_list[0]
               print(f"{f_mar.name} has enter the arena")
               f_mon=self.monster_list[0]
               print(f"{f_mon.name} has enter the arena")
               while f_mar.hp>0 and f_mon.hp>0:
                    if f_mar.ap>=(f_mar.weapon).apcost:
                        f_mar.attack(f_mon)
                    else:
                        f_mar.recoverAP()
                    if f_mon.dead:
                        (self.monster_list).pop(0) #enlève le monstre à la position 0 dans la liste
                        f_mar.recoverAP()
                        break
                    else:
                        if f_mon.ap>=f_mon.apcost:
                            f_mon.attack(f_mar)
                        else:
                            f_mon.recoverAP()
                        if f_mar.dead:
                            (self.space_list).pop(0) #enlève le space marine à la position 0 dans la liste
                            f_mon.recoverAP
                            break
            if self.monster_list:
                print("The monsters are victorious")
            else:
                print("The Space Marines are victorious")


        