from src.scoreCard import ScoreCard
import pytest

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
    assert match.getTotalScore() == 12