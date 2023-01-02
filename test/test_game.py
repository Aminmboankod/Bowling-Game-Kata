from src.game import Game
import pytest


pytest.mark.strike
def test_strike():
    assert 10 == Game.strike("X")

pytest.mark.spare
def test_spare():
    next_roll = 1
    assert 10+(next_roll)== Game.spare("/", next_roll)

pytest.mark.noPins
def test_noPins():
    assert 0 == Game.noPins("-")

pytest.mark.launch_Without_Bouns
def test_Launch():
    assert 6 == Game.Launch("51")