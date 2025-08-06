from plasmarifle import PlasmaRifle
from powerfist import PowerFist
pr = PlasmaRifle()
pf = PowerFist()
print(pr.getName()) # Plasma Rifle
print(pr.getDamage()) # 21
print(pr.getApcost()) # 5
pr.attack() # PIOU
print(pf.isMelee()) # True
pf.attack() # SBAM