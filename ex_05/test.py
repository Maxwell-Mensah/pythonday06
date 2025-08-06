from aspacemarine import ASpaceMarine
from plasmarifle import PlasmaRifle

# Abstract class, should not be instantiated
try:
    s = ASpaceMarine('Bob')
except TypeError:
    print('OK')
# equip: must refuse anything that is not a weapon
marine = ASpaceMarine('John') # suppose a concrete class
try:
    marine.equip("NotAWeapon")
except Exception as e:
    print(e)
# Output:
# Error in ASpaceMarine. Parameter is not an AWeapon.
marine.equip(PlasmaRifle())
# Output:
# John has been equipped with a Plasma Rifle.
