from src.game import Game
import pytest

@pytest.fixture
def score():
    score = Game()
    return score

@pytest.mark.noPins
def test_allZeros(score):
    assert 0 == score.totalScore("----------")

@pytest.mark.strike
def test_strike(score):
    assert 300 == score.totalScore("XXXXXXXXXXXX")

@pytest.mark.spare
def test_spare(score):
    assert 150 == score.totalScore("5/5/5/5/5/5/5/5/5/5/")

@pytest.mark.pinsAndZeros
def test_noPins(score):
    assert 90 == score.totalScore("9-9-9-9-9-9-9-9-9-9-")

@pytest.mark.launch_Without_Bouns
def test_Launch(score):
    assert 6 == score.totalScore("51")
    score.score = 0
    assert 60 == score.totalScore("12345123451234512345")

@pytest.mark.completeMatch
def test_completeMatch(score):
    assert 122 == score.totalScore("81-92/X637-52X-62/X")
    assert 127 == score.totalScore("9/9-9/9-12X9/9---XX-")
    assert 113 == score.totalScore("X35357162-/346-X6/7")
    assert 88 == score.totalScore("-----4-7-7818/6/8/81")
    assert 67 == score.totalScore("9-13315-817--38-9-18")
    assert 95 == score.totalScore("-814179/5/-/1--/7/5-")



'''
    index = -1
    lastRoll = 0
    lastFrame = card[-1]
    if card[-2] == "/":
        if card[-2].isdigit():
            self.score -= int(lastFrame)
        else:
            self.score -= self.scoreFrame(lastFrame)
    for roll in card:
        index += 1
        if roll == "X":
            if index == 9:
                self.score
            else:
                self.score += self.scoreFrame(roll) + self.bonus((card[index+1:index+3]))
        if roll == "/":
            self.score += self.scoreFrame(roll) + self.bonus((card[index+1]))-lastRoll
        if roll == "-":
            continue
        if roll.isdigit():
            self.score += int(roll)
            lastRoll = int(roll)
                    
    return self.score'''