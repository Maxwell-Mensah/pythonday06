from tacticalmarine import TacticalMarine
from assaultterminator import AssaultTerminator
marine = TacticalMarine('Mark')
# Output:
#Mark on duty.
terminator = AssaultTerminator('Kevin')
# Output:
#Kevin has teleported from space.
print(marine.getHp()) # 100
print(terminator.getHp()) # 150
