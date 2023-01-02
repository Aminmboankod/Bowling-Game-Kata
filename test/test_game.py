from src.game import Game
import pytest

@pytest.fixture
def score():
    score = Game()
    return score

@pytest.mark.noPins
def test_allZeros(score):
    assert 0 == score.totalScore("----------")
    assert 0 == score.totalScore("-")

@pytest.mark.strike
def test_strike(score):
    assert 300 == score.totalScore("XXXXXXXXXXXX")

@pytest.mark.spare
def test_spare(score):
    assert 150 == score.totalScore("5/5/5/5/5/5/5/5/5/5/5")

@pytest.mark.noPins
def test_noPins(score):
    assert 90 == score.totalScore("9-9-9-9-9-9-9-9-9-9-")

@pytest.mark.launch_Without_Bouns
def test_Launch(score):
    assert 6 == score.totalScore("51")
    score.score = 0
    assert 60 == score.totalScore("12345123451234512345")