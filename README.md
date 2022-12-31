# Bowling-Game-Kata
------
![](/doc/images/bowling-image.jpg)
## Introduction

The following project is a classic challenge proposed in class that consists of creating a program (in this case in python) that tries to add the points obtained by all the frames of a game of bowling.

Here is a sample score table of a bowling player:

| Frame | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Rolls | 1 &nbsp;&nbsp; 4 | 4 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | 5 &nbsp;&nbsp; / | ✕ | 0 &nbsp;&nbsp; 1 | 7 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | ✕ | 2 &nbsp;&nbsp; / &nbsp;&nbsp; 6 |
|Score| 5 | 14 | 29 | 49 | 60 | 61 | 77 | 97 | 117 | **133** |

## Rules:

The game consists of 10 frames as shown above.  In each frame the player has two opportunities to knock down 10 pins.  The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two tries.  The bonus for that frame is the number of pins knocked down by the next roll.  So in frame 3 above, the score is 10 (the total number knocked down) plus a bonus of 5 (the number of pins knocked down on the next roll.)

A strike is when the player knocks down all 10 pins on his first try.  The bonus for that frame is the value of the next two balls rolled.

In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame.  However no more than three balls can be rolled in tenth frame.


## TDD in Bowling kata:

To develop test-driven is to round in a simple cycle:  
1. [![Generic badge](https://img.shields.io/badge/⎍-Test-red.svg)](https://shields.io/)  

2. [![Generic badge](https://img.shields.io/badge/⎍-Code-brightgreen.svg)](https://shields.io/)  

3. [![Generic badge](https://img.shields.io/badge/⎍-Refactor-blue.svg)](https://shields.io/)