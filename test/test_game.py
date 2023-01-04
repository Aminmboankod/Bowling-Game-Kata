from src.game import Game
import pytest

@pytest.mark.noPins
def test_allZeros():
    match = Game("----------")
    assert match.totalScore() == 0

@pytest.mark.strike
def test_strike():
    match = Game("XXXXXXXXXXXX")
    assert match.totalScore() == 300

@pytest.mark.spare
def test_spare():
    match = Game("5/5/5/5/5/5/5/5/5/5/5") 
    assert match.totalScore() == 150

@pytest.mark.pinsAndZeros
def test_noPins():
    match = Game("9-9-9-9-9-9-9-9-9-9-")
    assert match.totalScore() == 90

@pytest.mark.launch_Without_Bouns
def test_Launch():
    match = Game("12345123451234512345")
    assert match.totalScore() == 60

@pytest.mark.completeMatch
def test_completeMatch():

    match = Game("-----4-7-7818/6/8/81")
    assert match.totalScore() == 88

    match = Game("81-92/X637-52X-62/X")
    assert match.totalScore() == 122

    match = Game("9/9-9/9-12X9/9---XX-")
    assert match.totalScore() == 127    

    match = Game("X35357162-/346-X6/7")
    assert match.totalScore() == 113      


