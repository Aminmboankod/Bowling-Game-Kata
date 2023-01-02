from src.game import Game
import pytest


pytest.mark.strike
def strike():
    assert 10 == Game.strike("X")

pytest.mark.spare
def spare():
    next_roll = 1
    assert 10+(next_roll)== Game.spare("/", next_roll)

pytest.mark.noPins
def noPins():
    assert 0 == Game.noPins("-")

pytest.mark.launch_Without_Bouns
def normaLaunch():
    assert 6 == Game.normaLaunch("51")