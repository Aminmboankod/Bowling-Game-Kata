from src.bowlingGame import Game
import pytest


@pytest.mark.noPins
def test_noPins():
    pins = "----------"
    match = Game()
    for i in range(len(pins)):
        roll = pins[i]
        match.roll(roll)
    assert match.getTotal() == 0



@pytest.mark.launch_Without_Bouns
def test_notBonus():
    pins = "12345123451234512345"
    match = Game()
    for i in range(len(pins)):
        roll = pins[i]
        match.roll(roll)
    assert match.getTotal() == 60


@pytest.mark.pinsAndZeros
def test_noPins():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    match = Game()
    for i in range(len(pins)):
        roll = pins[i]
        match.roll(roll)
    assert match.getTotal() == 90

