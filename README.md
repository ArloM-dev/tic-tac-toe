# Tic tac toe

A text-based customizable tic-tac-toe game with many uses. You can use it to play against a friend or a bot,
let two bots battle it out, or even test your programming skills by developing your own.

<details>
  <summary> Go to ...</summary>
  <ul>
    <li><a href="#using-the-programme">Using the programme</a></li>
    <li><a href="#documentation-for-bots">Documentation for bots</a></li>
    <li><a href="#help">Help</a></li>
  </ul>
</details>

### Quick note

This is just an old project I found from when I had started out programming,
and thought it would be nice to publish to GitHub for people to mess around with. 
It's quite basic, but technically it is my only completed repo as most of my other projects got deleted.

### Description

This project is designed to be edited and experimented with.
The way this works is that when you play, the game uses the bots file to determine the next move.
This means you can either play against other people or build a program/bot to play against you.
By default, the two players are set to user input, meaning it would be two people playing against each other.
But if you would rather play against a bot or make two bots play against each other, just build your function in the bots.py file.
Then, up at the top where it says "insert your bots here," change the text from "user_bot" to your own function.

## Using the programme

### Installing

As this is just a simple Python file, you can download the files from GitHub or clone the repo.
If you want, you can also fork the repo, but as this is designed to be modified,
I likely won't be taking any pull requests or making any future changes.

To clone the repo, make sure you have Git installed and then run the command:
```
git clone https://github.com/ArloM-dev/tic-tac-toe
```
To install git go [here](https://git-scm.com/downloads)

### Executing and using the program

These files fully function in Python 3.12 and have not been tested for future or past versions.
If you do not currently have Python installed, it can be installed [here](https://www.python.org/downloads/).

* If you want to measure two bots against each other, set them as player 1 and 2.
* Follow the instructions on the main.py menu and choose your settings.


## Documentation for bots

### How the grid works

The grid is a basic matrix with the following values
* empty = 0
* X = 1
* O = 4  <br/>

The matrix ranges from 0 to 2 in both dimensions, with [0][0] being the first value and [2][2] being the last.
The reason for O being four is that the game detects a win by adding up the values of a row/column/diagonal and checking the result.
By O being 4, it is impossible for the game to accidentally add up to the correct value with a combination of Xs, Os, and empties.
There are already a few functions to get you started, such as the possible cells function, which will return an array full of grid coordinates (in the form of arrays) that are empty.
Feel free to edit these functions and experiment with ideas, and even modify the main file.

### Building a bot

Building a bot isn't that complicated, but there are a few things you should keep in mind.

* The function returns an array of integers, which just contains the two coordinates.
* The parameters should be the grid matrix first, then the player which is a bool.
* If your function uses less or more, make sure to edit the function at the top's parameters.

## Help

There are a few problems you may run into while developing your bot. These include:

### Cell already ocupied

This is pretty self-explanatory and just means your function is returning already occupied cells. To fix this, try using the possible cells function.

### Invalid row/column

This error occurs when the coordinates submitted were invalid or none were submitted at all.
To fix this, make sure your function returns an array in the form [intx, inty], where the x and y values range between 0 and 2.
If that doesn't work, make sure you spelled your function correctly when assigning it, and that the parameters are in the correct order.
