# Mars Rover Exploration Programming Problem

This README pertains to the Mars Rover Exploration Programming Problem.

The following .py-files are included:

```classes.py``` Class definitions of Plateau and Rover objects.

```main.py``` Main program which prompts for user inputs in the terminal.

```tests.py``` Contains test cases for debugging, using the ```doctest``` module.

All code is written in **Python 3**.

## Problem Description

The problem concerns a squad of rovers exploring a rectangular plateau on Mars. The plateau is divided up into a Euclidean grid, with coordinates *(0,0)* at the lower-left corner and *(xdim,ydim)* at the upper-right corner (*xdim* and *ydim* are user-specified).

Rovers are deployed at an empty grid point, specified by its initial *(x,y)* position, as well as its heading ('N', 'E', 'S' or 'W'). Then, it is sent a navigation string, a string of letters, which controls its exploration path across the plateau. The navigation string can consist of either of the following letters:

- *L* - rotates rover 90 degrees to the left
- *R* - rotates rover 90 degrees to the right
- *M* - moves rover one grid point forward in the direction of its heading

The program is set up such that each string of letters is executed completely, before another rover is deployed and controlled.

### Assumptions

The following assumptions are made and tested for in this program:

- All grid point coordinates of the plateau and thus the rover positions must be positive integer values.
- A rover cannot be deployed on a grid point occupied by another rover.
- A rover will not move if the navigation string contains illegal command characters.
- A rover cannot leave the boundaries of the plateau. Attempting to do so will apply the rover's internal safety protocol: ignoring the rest of the commands in its navigation string (which is deemed unreliable).
- A rover cannot collide with into another rover. Attempting to do so will also apply the rover's internal safety protocol.

## Dependencies

This program has no external dependencies, and only employs the Python standard library module ```doctest``` for running tests in ```tests.py```.

## Usage of scripts

### ```classes.py```

**Class definitions of Plateau and Rover objects.**

**Recommended usage:** ```$ python3 -i classes.py```

To instantiate a Plateau object, call ```Plateau(xdim, ydim)```. Plateau objects are represented as a grid that spans between ```0 <= x <= xdim``` and ```0 <= y <= ydim```. A newly instantiated Plateau object

```
>>> plat = Plateau(5, 5)
```

will be represented as

```
>>> plat
5 ▢ ▢ ▢ ▢ ▢ ▢
4 ▢ ▢ ▢ ▢ ▢ ▢
3 ▢ ▢ ▢ ▢ ▢ ▢
2 ▢ ▢ ▢ ▢ ▢ ▢
1 ▢ ▢ ▢ ▢ ▢ ▢
0 ▢ ▢ ▢ ▢ ▢ ▢
  0 1 2 3 4 5

```

To instantiate a Rover object, call ```Rover(x, y, heading, plateau_obj[, id])```. This will spawn a rover at grid point *(x, y)*. Example:

```
>>> r2 = Rover(2, 3, 'N', plat, 'R2D2')
```

The rover will be represented by its coordinates and heading, so by calling the object we can read its position and orientation:

```
>>> r2
2 3 N
>>> print(r2)
position of rover R2D2: (2, 3, N)
```

In the associated Plateau object ```plateau_obj``` is represented by a triangle pointing towards its ```heading``` in the Plateau object.

```
>>> plat
5 ▢ ▢ ▢ ▢ ▢ ▢
4 ▢ ▢ ▢ ▢ ▢ ▢
3 ▢ ▢ ▲ ▢ ▢ ▢
2 ▢ ▢ ▢ ▢ ▢ ▢
1 ▢ ▢ ▢ ▢ ▢ ▢
0 ▢ ▢ ▢ ▢ ▢ ▢
  0 1 2 3 4 5
```

We can call the ```explore``` method of a rover to send navigation commands to it. For instance, if we want the rover to advance one step, turn right, advance two steps, turn left, advance one step, turn left again and finally advance three steps, we call

```
>>> r2.explore("MRMMLMLMMM")
```

Now, the rover should have coordinates *(1,5)* and be facing west. We can check this:

```
>>> r2
1 5 W
```

Calling the Plateau object, we can see the trail that the rover has made along its journey, as well as its final position:

```
>>> plat
5 ▢ ◀ – – – ▢
4 ▢ ▢ – – | ▢
3 ▢ ▢ | ▢ ▢ ▢
2 ▢ ▢ ▢ ▢ ▢ ▢
1 ▢ ▢ ▢ ▢ ▢ ▢
0 ▢ ▢ ▢ ▢ ▢ ▢
  0 1 2 3 4 5

>>>
```

### ```main.py```

**Main program which prompts for user inputs in the terminal.**

**Recommended usage:** ```$ python3 main.py```

Interactive program of the Mars Rover Exploration Programming Problem. Class definitions are imported here, which along with user-defined functions are used to prompt the user for plateau and rover configurations, such as:

- dimensions of plateau
- number of rovers deployed
- initial position of each rover
- navigation commands for each rover

This code can be used to test the input given in the assignment brief (note that other outputs may appear in between each input prompt/output statement):

```Specify dimensions for plateau (xdim ydim): 5 5```

```Number of rovers to be deployed: 2```

```Specify position for rover 1 (x y heading): 1 2 N```

```Navigation string for rover 1 to explore plateau: LMLMLMLMM```

```Specify position for rover 2 (x y heading): 3 3 E```

```Navigation string for rover 2 to explore plateau: MMRMMRMRRM```

The corresponding output should be displayed in the Python interpreter at the end of the program:

```
Final position of rover 1: (1, 3, N)
Final position of rover 2: (5, 1, E)
```

### ```tests.py```

**Contains test cases for debugging, using the ```doctest``` module.**

**Recommended usage:** ```$ python3 tests.py -v```

This script contains five test cases, which test whether the program runs and whether the assumptions for the rovers' movements hold. The test cases are as following:

- Test Case 1: test the given input in the assignment brief (same as in ```main.py```)
- Test Case 2: test a few customised input to check if code runs
- Test Case 3: try spawning a rover outside the plateau boundaries
- Test Case 4: try venturing out of the plateau boundaries (rover will stop at the boundary)
- Test Case 5: try colliding with another rover by a) spawning a rover on an occupied grid point by another rover, and by b) steering a rover onto a grid point occupied by another rover.

Test Cases 1 and 2 should run and output the correct final positions of the rovers, whereas Test Cases 3, 4 and 5 should all indicate some sort of AssertionErrors.

## Author
[Jan Xu](mailto:jx3915@imperial.ac.uk)

Telephone: +1 (510) 926-5428
