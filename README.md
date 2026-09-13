## 🏆Quiz game 🏆

### About it:

This program consists in giving you random knowledge questions once at a time. For example, mathematical, history, geographical questions that you may or not know. 


### Features 💪

>  The user can answer each questions by choosing a number that corresponds with the given possible answers


### Requirements 🛄

> Python 3.13 or Python 3.14


### Installation 📦

1. Clone the repository with `git clone` command on the repository.
2. Create a virtual environment for your script with `python3 -m venv` command.
3. Activate the virtual environment with `source .venv/bin/activate` command

### Usage 👤

- Run your program by simply typing `python3 quiz-game.py`.

- Then, this should appear at the start of the program:
  ```
  |========================================================|
  |    ___        _                                        |
  |   / _ \ _   _(_)____   __ _  __ _ _ __ ___   ___       |
  |  | | | | | | | |_  /  / _` |/ _` | '_ ` _ \ / _ \      |
  |  | |_| | |_| | |/ /  | (_| | (_| | | | | | |  __/      |
  |   \__\_\\__,_|_/___|  \__, |\__,_|_| |_| |_|\___|      |
  |                       |___/                            |
  |========================================================|
  
  Hi! You have succesfully entered the quiz game!
  Do you wish to continue [Y or N]: 
  ```

> It asks you if you want to play the game or quit the program.
>
> Type `Y` or ` y `  and press `enter` to play
>
> Type `N` or `n`  and press `enter` to quit



Then there are the instructions for the quiz game and your first random question already shows up, so something like this should appear (for example): 

```
Hi, Welcome to the quiz game 🏆 and here, I am here to test your general knowledge 🧠!
There are 10 random questions in total that you will have to answer. Each one will potentially get harder so be careful! 😉
Good luck!

[10 POINTS] Which country is considered the largest in the world? [difficulty: easy] 1/15
[1] Canada
 
[2] United states
 
[3] Russia
 
[4] Japan

~ ~ ~ ~ ~ ~ ~ ~ ~ ~
|—---—(Enter your number below)
|
|--->
```

#### Examples 👀

Example 1:

- So what you have to do is to pick a number between 1 to 4.
  - Type `1`  and press `enter` for Canada
  - Type `2`  and press `enter` for United states
  - Type `3` and press `enter` for Russia
  - Type `4`  and press `enter` for Japan

Example 2:

```
====================================
[10 POINTS] How many sides does a hexagon polygon have?  [difficulty: easy]  3/15

[1] 5 sides
 
[2] 6 sides
 
[3] 4 sides
 
[4] 7 sides

~ ~ ~ ~ ~ ~ ~ ~ ~ ~
|—---—(Enter your number below)
|
|--->
```

If you want to pick an answer, **you have to choose the number that corresponds to the answer, not the actual amount of sides of the hexagon**

- So here are the choices:
  - Type `1` and press `enter`  for **5 sides** 
  - Type `2` and press `enter`  for **6 sides**
  - Type `3`  and press `enter` for **4 sides**
  - Type `4`  and press `enter` for **7 sides**


### Project structure 🏗️

```
quiz-game/
|── questions/
     |── easy-questions.json
     |── hard-questions.json
     |── medium-questions.json
|──.gitignore
├── README.md
|── other_funcs.py
|── quiz-game.py
|── quiz_game_ode_testing.py
```


### Author ✍️

```
Created by ecalexandre 
```
