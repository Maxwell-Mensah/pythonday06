from iunit import IUnit
# Cannot instantiate directly:
try:
    unit = IUnit()
except TypeError as e:
    print(type(e)) # <class 'TypeError'>
