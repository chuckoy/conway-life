# conway-life
Implementation of Conway's game of life.

Running from command line:
  `python life.py -size <size> -seed <seed>`
    
* `size` determines the size of the board (as of now the app supports just square boards)
* `seed` determines the seed used when generating randoms.

Developed on Python 3 in an Ubuntu 12.04 instance running on Windows 10.

# Reflections

 I used the `seed` parameter to manually test the behaviour of the board. In retrospect, I should've used unit tests for this.
 
 One main bug that I recall when developing this was that the program was saving the changes to the cells when stepping forward. When it reaches a cell that needed to access previous data, it instead took the new data, causing it to deviate from what was supposed to happen. I did a workaround for it by defining a new board for every step, but I wonder if there is a more space-efficient method of solving this problem.
 
 As opposed to my [Monopoly](https://github.com/chuckoy/monopoly-cash-tracker) project. I was actually able to write a test for this app. Granted, it only tests the blinker case but at least I managed to take a step forward. I hope I'll be able to improve the tests for this app in the future.
