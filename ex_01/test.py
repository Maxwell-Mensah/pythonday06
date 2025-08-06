from aweapon import AWeapon
# This should fail because AWeapon is abstract
try:
    a = AWeapon('Laser Gun', 5, 20)
except TypeError as e:
    print(type(e)) # <class 'TypeError'>
# Wrong type
try:
    a = AWeapon('Laser Gun', 'not_a_number', 20)
except Exception as e:
    print(e)