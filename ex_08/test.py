from spacearena import SpaceArena
from radscorpion import RadScorpion
from tacticalmarine import TacticalMarine

arena = SpaceArena()
arena.enlistMonsters([RadScorpion(), RadScorpion()])
arena.enlistSpaceMarines([TacticalMarine('Leo')])

arena.fight()