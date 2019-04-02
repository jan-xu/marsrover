"""
ThoughtWorks Recruitment Assessment
Mars Rover Programming Problem
main.py

Author:        Jan Xu
Telephone:     +1 (510) 926-5428
Email address: jx3915@imperial.ac.uk

Main program of the Mars Rover Programming Problem, as given by ThoughtWorks.
Class definitions are imported here, which along with user-defined functions are
used to prompt the user for plateau and rover configurations, such as:

* dimensions of plateau
* number of rovers deployed
* initial position of each rover
* navigation commands for each rover

This code can be used to test the input given in the assignment brief:

    Specify dimensions for plateau (xdim ydim): 5 5
    Number of rovers to be deployed: 2
    Specify position for rover 1 (x y heading): 1 2 N
    Navigation string for rover 1 to explore plateau: LMLMLMLMM
    Specify position for rover 2 (x y heading): 3 3 E
    Navigation string for rover 2 to explore plateau: MMRMMRMRRM

The corresponding output should be displayed in the Python interpreter at the
end of the program:

    Final position of rover 1: (1, 3, N)
    Final position of rover 2: (5, 1, E)

"""

from classes import Plateau, Rover

#############
# Functions #
#############

def create_plateau():
    """Create a plateau for rover exploration."""

    xdim, ydim = map(int, input("Specify dimensions for plateau (xdim ydim): ").split())
    plat = Plateau(xdim, ydim)
    return plat

def spawn_rover(id, plat):
    """Spawn a rover on the plateau according to inputted position."""

    pos = input("Specify position for rover {0} (x y heading): ".format(id)).split()
    x, y, head = int(pos[0]), int(pos[1]), pos[2]
    rover = Rover(x, y, head, plat, id)
    print(str(rover))
    return rover

def move_rover(rover):
    """Move rover according to inputted navigation string."""

    navstring = input("Navigation string for rover {0} to explore plateau: ".format(rover.id))
    rover.explore(navstring)

################
# Main Program #
################

def run():
    """Main code that runs the Mars Rover program."""

    plat = create_plateau()
    print("Initial configuration of plateau: \n")
    print(plat)

    n = int(input("Number of rovers to be deployed: "))

    for id in range(1, n+1):
        rover = spawn_rover(id, plat)
        print("Spawned a rover! Initial", str(rover))
        print('\n', plat)

        print("Ready for navigation!")
        move_rover(rover)
        print('\n', plat)

    for rover in plat.rovers:
        print("Final", str(rover))

# Call the main program
if __name__ == "__main__":
    run()
