"""
Mars Rover Exploration Programming Problem
main.py

Author:        Jan Xu
Telephone:     +1 (510) 926-5428
Email address: jx3915@imperial.ac.uk

Test cases for the Mars Rover Exploration Programming Problem.
"""

from classes import Plateau, Rover

############
# Doctests #
############

def testcase1():
    """Test Case 1: test a few customised input to check if code runs

    >>> plat = Plateau(5, 5)
    >>> rover1 = Rover(1, 2, 'N', plat)
    >>> rover1.explore("LMLMLMLMM")
    >>> rover1
    1 3 N
    >>> rover2 = Rover(3, 3, 'E', plat)
    >>> rover2.explore("MMRMMRMRRM")
    >>> rover2
    5 1 E
    """

def testcase2():
    """Test Case 2: test a few customised input to check if code runs

    >>> plat = Plateau(8, 3)
    >>> rover1 = Rover(0, 0, 'E', plat)
    >>> rover1.explore("MMMLLMMRM")
    >>> rover1
    1 1 N
    >>> rover2 = Rover(3, 0, 'S', plat)
    >>> rover2.explore("RRRMLMMMR")
    >>> rover2
    4 3 E
    >>> rover3 = Rover(8, 3, 'W', plat)
    >>> rover3.explore("MRL")
    >>> rover3
    7 3 W
    """

def testcase3():
    """Test Case 3: try spawning a rover outside the plateau boundaries

    >>> plat = Plateau(3, 4)
    >>> rover = Rover(3, 5, 'N', plat)
    Traceback (most recent call last):
      ...
    AssertionError: The rover cannot be placed outside the plateau.
    >>> rover
    Traceback (most recent call last):
      ...
    NameError: name 'rover' is not defined
    """

def testcase4():
    """Test Case 4: try venturing out of the plateau boundaries (rover will stop
    at the boundary)

    >>> plat = Plateau(3, 4)
    >>> rover = Rover(3, 2, 'N', plat)
    >>> rover.explore("MMM")
    Traceback (most recent call last):
      ...
    AssertionError: The rover cannot move outside the plateau.
    >>> rover
    3 4 N
    """

def testcase5():
    """Test Case 5: try colliding with another rover by a) spawning a rover on
    an occupied grid point by another rover, and by b) steering a rover onto a
    grid point occupied by another rover.

    >>> plat = Plateau(3, 4)
    >>> rover1 = Rover(3, 2, 'N', plat)
    >>> rover2 = Rover(3, 2, 'E', plat)
    Traceback (most recent call last):
      ...
    AssertionError: The rover cannot be placed on a grid point occupied by another rover.
    >>> rover2
    Traceback (most recent call last):
      ...
    NameError: name 'rover2' is not defined
    >>> rover2 = Rover(1, 2, 'N', plat)
    >>> rover2.explore("RMM")
    Traceback (most recent call last):
      ...
    AssertionError: The rover cannot move to a grid point occupied by another rover.
    """

#################
# Running Tests #
#################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
