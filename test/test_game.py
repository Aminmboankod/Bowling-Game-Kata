from src.game import Game
import pytest


pytest.mark.strike
def strike():
    assert 10 == Game.strike("X")

pytest.mark.spare
def spare():
    next_frame = 1
    assert 10+(next_frame)== Game.spare("/")

pytest.mark.noPins
def noPins():
    assert 0 == Game.noPins("-")

pytest.mark.launch_Without_Bouns
def normaLaunch():
    assert 6 == Game.normaLaunch("51")