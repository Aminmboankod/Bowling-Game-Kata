# Bowling-Game-Kata
------

![Bowling](/doc/images/bowling-image.jpg)


# Index

+   [Introduction](#introduction)
+   [DDD Information](#ddd-information)
+   [Rules](#rules)
+   [Manual](#manual)
    +   [Requierements](#requierements)
    +   [Instalation](#instalation)
+   [DDD Model](#ddd-model)
+   [UML Diagram](#uml-diagram)
+   [TDD](#tdd-in-bowling-kata)



# Introduction



The following project is a classic challenge proposed in class that consists of creating a program (in this case in python) that tries to add the points obtained by all the frames of a game of bowling.

Here is a sample score table of a bowling player:

| Frame | 1st | 2nd | 3rd | 4th | 5th | 6th | 7th | 8th | 9th | 10th |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Rolls | 1 &nbsp;&nbsp; 4 | 4 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | 5 &nbsp;&nbsp; / | ✕ | 0 &nbsp;&nbsp; 1 | 7 &nbsp;&nbsp; / | 6 &nbsp;&nbsp; / | ✕ | 2 &nbsp;&nbsp; / &nbsp;&nbsp; 6 |
|Score| 5 | 14 | 29 | 49 | 60 | 61 | 77 | 97 | 117 | **133** |


# DDD Information

Create a program, which, given a valid sequence of rolls for one line of American Ten-Pin Bowling,
produces the total score for the game. This is a summary of the rules of the game:
- Each game, or “line” of bowling, includes ten turns, or “frames” for the bowler.
- In each frame, the bowler gets up to two tries to knock down all the pins.

- If in two tries, he fails to knock them all down, his score for that frame is the total number of pins
knocked down in his two tries.
- If in two tries he knocks them all down, this is called a “spare” and his score for the frame is ten
plus the number of pins knocked down on his next throw (in his next turn).
- If on his first try in the frame he knocks down all the pins, this is called a “strike”. His turn is over,
and his score for the frame is ten plus the simple total of the pins knocked down in his next two
rolls.
- If he gets a spare or strike in the last (tenth) frame, the bowler gets to throw one or two more
bonus balls, respectively. - These bonus throws are taken as part of the same turn. If the bonus
throws knock down all the pins, the process does not repeat: the bonus throws are only used to
calculate the score of the final frame.
- The game score is the total of all frame scores.

## Rules:

The game consists of 10 frames as shown above.  In each frame the player has two opportunities to knock down 10 pins.  The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares.

A spare is when the player knocks down all 10 pins in two tries.  The bonus for that frame is the number of pins knocked down by the next roll.  So in frame 3 above, the score is 10 (the total number knocked down) plus a bonus of 5 (the number of pins knocked down on the next roll.)

A strike is when the player knocks down all 10 pins on his first try.  The bonus for that frame is the value of the next two balls rolled.

In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame.  However no more than three balls can be rolled in tenth frame.

# Manual

## Requierements
| Paquete | Versión |
|:----:|:----:|
|attrs | 22.2.0
| exceptiongroup | 1.1.0 
| iniconfig | 1.1.1 |
| packaging | 22.0 | 
| pluggy | 1.0.0 |
| pytest | 7.2.0 |
| tomli | 2.0.1

## Instalation

Crea el directorio donde vas a clonar el repositorio  y clonalo usando el siguiente comando:
```
$ mkdir ./Bowling-Game-kata
$ cd Bowling-Game-kata
$ git clone https://github.com/Aminmboankod/Bowling-Game-Kata.git
```
Ejecuta el archivo de configuración:
```
$ ./setup.sh
```


## DDD Model
---
![Modelo DDD](/doc/images/BowlingGame-DDD.drawio.png)


## UML Diagram
---
![Diagrama UML](/doc/images/BowlingGame-UML.drawio.png)



## TDD in Bowling kata:

To develop test-driven is to round in a simple cycle:  
1. [![Generic badge](https://img.shields.io/badge/⎍-Test-red.svg)](https://shields.io/)  

2. [![Generic badge](https://img.shields.io/badge/⎍-Code-brightgreen.svg)](https://shields.io/)  

3. [![Generic badge](https://img.shields.io/badge/⎍-Refactor-blue.svg)](https://shields.io/)