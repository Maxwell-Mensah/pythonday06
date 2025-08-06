from amonster import AMonster
# Abstract class creation, should fail
try:
    m = AMonster('Krug', 100)
except TypeError as e:
    print(type(e))