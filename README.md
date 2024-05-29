# Tic tac toe

A text based customizable tic tac toe game with many uses. You can use it to just play a friend or bot, let two bots battle it out or even
test your programming skills by developing you own.

### Quick note
This is just an old project I found from when I had starting out programming,
and thought it would be nice to publish to github for people too mess around with.
Its quite basic, but technically it is my only completed repo as most of my other projects got deleted.

## Description

This projects is designed to be edited and experimented with.
The way this works is that when you play, the game uses the bots file to determine the next move.
This means you can either play other people, or build a program/bot to play against you.
By default the two players are set to user input, meaning it would be two people playing against each other
but if you would rather play a bot or make two bots play against each other just build your function in the bots.py file,
and then up at the top where it says "insert your bots here" and change the text from user_bot to your own function.

## Using the program

### Installing

As this is just a simple python file, you can just download the files from github or clone the repo.
If you want you can also fork the repo, but as this is designed to be modified, I likely wont be taking any pull requests or making any future changes.

To clone the repo, make sure you have git installed and then run the command
```
git clone https://github.com/ArloM-dev/tic-tac-toe
```
To install git go [here](https://git-scm.com/downloads)

### Executing and using the program

These files fully function in python 3.12, and have not been tested for future or past versions
if you do not currently have python it can be installed [here](https://www.python.org/downloads/)
* if you want to measure two bots against each other, set them as player 1 and 2
* follow the instructions on the main.py menu and choose your settings

## Documentation for bots

### How the grid works

The grid is a basic matrix with the following values
* empty = 0
* X = 1
* O = 4  <br/>

The matrix just ranges from 0 to 2 both ways, with [0[0]] being the first value and [2[2]] being the last.

The reason for O being four is that the way the game detects a win is by adding up the values of a row/column/diagonal and checking the result.
By O being 4, it is impossible for the game to accidentaly add up to the correct value with a combination of Xs, Os and emptys.
There are already a few functions to get you started such as the possible cells function, which will return an array full of grid coordinates
(in the form of arrays) that are empty. Feel free to edit these functions and mess around with ideas, and even mess with the main file.

### Building a bot

Building a bot isn't that complicated, but there are a few things you should keep in mind.
* The function returns an array of intigers, which just contain the two coordinates
* The parameters should be the grid matrix first, then the player which is a bool
* If your function uses less or more, make sure to edit the function at the tops parameters

## Help
There are a few problems you may run into while developing your bot. These include:

### Cell already ocupied

This is pretty self explanitory, and just means your function is returning allready ocupied cells. To fix this, try using the possible cells function.

### Invalid row/column

This error occurs when the coordinates submitted were invalid or none were submitted at all. To fix this, make sure
your function returned an array in the form [intx, inty], where the x and y values range between 0 and 2. If that doesnt work, make sure
you spelled your function correctly when assigning it, and that the parameters are the correct way round.
