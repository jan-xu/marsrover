"""
ThoughtWorks Recruitment Assessment
Mars Rover Programming Problem
classes.py

Author:        Jan Xu
Telephone:     +1 (510) 926-5428
Email address: jx3915@imperial.ac.uk

Class definitions of Plateau objects and Rover objects. Plateau objects are
represented as a grid that spans between 0 <= x <= xdim and 0 <= y <= ydim.
Rover objects are represented by their position (x, y, heading). The rovers can
move around the plateau, but not collide with each other or venture outside the
plateau boundaries.

These class definitions will serve as foundations for the main program, as
specified in main.py. Doctests are also presented in tests.py and can be run to
ensure stability of the program.
"""

roversymbols = {'N': '▲', 'E': '▶', 'S': '▼', 'W': '◀'}
trailsymbols = {'N': '|', 'E': '–', 'S': '|', 'W': '–'}

#####################
# Class Definitions #
#####################

class Plateau(object):
    """Defines a plateau class on which the rovers navigates."""

    def __init__(self, xdim, ydim):
        """Instantiates a Plateau object with dimensions (xdim, ydim)."""

        assert isinstance(xdim, int) and isinstance(ydim, int), \
            "The plateau dimensions must be integer inputs."
        assert xdim >= 0 and ydim >= 0, \
            "The plateau dimensions must be positive."

        self.xdim = xdim
        self.ydim = ydim
        self.rovers = [] # contains all Rover objects on the plateau
        self.build_grid()

    def build_grid(self):
        """Initialises a representation of Plateau object as a grid."""

        self.grid = []

        # Add rows along y_dim with row labels
        for y in range(self.ydim + 1):
            self.grid.append([('%i' % (self.ydim - y))] + ['▢'] * (self.xdim + 1))

        # Add column labels
        self.grid.append([' '] + list(map(str, list(range(self.xdim + 1)))))

    def add_rover(self, rover):
        """Adds rover to the grid point, if no other rover is occupying it."""

        for r in self.rovers:
            assert (rover.x, rover.y) != (r.x, r.y), \
                "The rover cannot be placed on a grid point occupied by another rover."

        self.rovers.append(rover)

    def __repr__(self):
        return ''.join([' '.join(row) + '\n' for row in self.grid])


class Rover(object):
    """Defines a rover class to occupy a grid point and navigate across a
    plateau."""

    orient_dct = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
    orient_lst = list(orient_dct) # list of keys in orientation dictionary

    def __init__(self, x, y, head, plat, id=""):
        """Instantiates a Rover object at position (x, y, head) associated with
        a plateau object."""

        assert isinstance(x, int) and isinstance(y, int), \
            "The rover coordinates must be integer inputs."
        assert 0 <= x <= plat.xdim and 0 <= y <= plat.ydim, \
            "The rover cannot be placed outside the plateau."
        assert head.upper() in Rover.orient_lst, \
            "The rover heading input is invalid. Possible inputs: 'N', 'E', 'S', 'W'."
        assert isinstance(plat, Plateau), \
            "The plateau input is not a Plateau object."

        self.x = x
        self.y = y
        self.head = head.upper()
        self.id = id
        self.plat = plat
        plat.add_rover(self)

        # Visualise rover in grid representation
        self.x_idx, self.y_idx = self.coords_idx()
        self.plat.grid[self.y_idx][self.x_idx] = roversymbols[self.head]

    def move_forward(self):
        """Moves the rover forward one step in the direction of its heading."""

        move_instructs = Rover.orient_dct[self.head] # movement instructions

        assert 0 <= self.x + move_instructs[0] <= self.plat.xdim \
           and 0 <= self.y + move_instructs[1] <= self.plat.ydim, \
            "The rover cannot move outside the plateau."
        for r in self.plat.rovers:
            assert (self.x + move_instructs[0], self.y + move_instructs[1]) != (r.x, r.y), \
                "The rover cannot move to a grid point occupied by another rover."

        self.x += move_instructs[0]
        self.y += move_instructs[1]

        # Visualise rover in grid representation
        x_new_idx, y_new_idx = self.coords_idx()
        self.plat.grid[y_new_idx][x_new_idx] = roversymbols[self.head]
        self.plat.grid[self.y_idx][self.x_idx] = trailsymbols[self.head]
        self.x_idx, self.y_idx = x_new_idx, y_new_idx # update new coordinate indices

    def rotate(self, direction):
        """Rotates the rover 90 degrees to the left (L) or right (R)."""

        head_idx = Rover.orient_lst.index(self.head)
        if direction.upper() == 'L':
            self.head = Rover.orient_lst[(head_idx - 1) % 4]
        elif direction.upper() == 'R':
            self.head = Rover.orient_lst[(head_idx + 1) % 4]

        # Visualise rover in grid representation
        self.plat.grid[self.y_idx][self.x_idx] = roversymbols[self.head]

    def explore(self, navstring):
        """Implements navigation commands to the rover as a string consisting of
        letters 'L', 'R' and 'M'."""

        assert set(navstring.upper()).issubset({'L', 'R', 'M'}), \
            "Invalid navigation string. Possible inputs: 'L', 'R', 'M'."

        def action(self, navstring):
            """Implements first navigation command in the navigation string."""
            if navstring:
                if navstring[0] != 'M':
                    self.rotate(navstring[0])
                else:
                    self.move_forward()
                action(self, navstring[1:])

        return action(self, navstring)

    def __repr__(self):
        return "{0} {1} {2}".format(self.x, self.y, self.head)

    def __str__(self):
        return "position of rover {0}: ({1}, {2}, {3})".format(self.id, self.x, self.y, self.head)

    def coords_idx(self):
        """Finds the indices of the grid representation of the plateau that
        corresponds with the rover position."""

        x_idx = self.x + 1 # x-index is just one more than x-coordinate

        # y-index is inverted and is therefore parsed in the grid attribute of the Plateau object
        for row in self.plat.grid:
            if str(self.y) == row[0]:
                y_idx = self.plat.grid.index(row)
                break

        return x_idx, y_idx
