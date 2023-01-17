from src.bowlingGame import Game
from src.scoreCard import ScoreCard
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


@pytest.mark.strike
def test_strike():
    pins = "XXXXXXXXXXXX"
    match = ScoreCard(pins)
    match.calculateScore()
    assert match.getTotalScore() == 300


@pytest.mark.spare
def test_spare():
    pins = "5/5/5/5/5/5/5/5/5/5/5"
    match = ScoreCard(pins)
    match.calculateScore()
    assert match.getTotalScore() == 150

@pytest.mark.pinsAndZeros
def test_noPins():
    pins = "9-9-9-9-9-9-9-9-9-9-"
    match = Game()
    for i in range(len(pins)):
        roll = pins[i]
        match.roll(roll)
    assert match.getTotal() == 90

@pytest.mark.completeMatch
def test_completeMatch():

    pins = "X35357162-/346-X6/7"
    match = ScoreCard(pins)
    match.calculateScore()
    assert match.getTotalScore() == 113


    pins = "-----4-7-7818/6/8/81"
    match = ScoreCard(pins)
    match.calculateScore()
    assert match.getTotalScore() == 88


    pins = "81-92/X637-52X-62/X"
    match = ScoreCard(pins)
    match.calculateScore()
    assert match.getTotalScore() == 122


    pins = "9/9-9/9-12X9/9---XX-"
    match = ScoreCard(pins)
    match.calculateScore()
    assert match.getTotalScore() == 127
