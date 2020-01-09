#NOTES
# - a knight always has 8 possible moves


#VARIABLES
valid_positions = 0
invalid_positions = 0
total_positions = 0;


#CLASSES
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


#FUNCTIONS
#given parameter of x position and y position, returns True is position in in 8x8 grid, returns False otherwise
def return_valid_position(x, y):
    result = False
    global valid_positions
    global invalid_positions
    global total_positions

    if ( x > 0 or x > 8 or y < 0 or y > 8):
        result = True
        valid_positions += 1
    else:
        result = False
        invalid_positions += 1

    total_positions += 1

    return result

#given parameter of x position and y position, returns array of all possible valid positions
def get_possible_positions(x, y):
    positions = [];
    if (return_valid_position(x - 2, y + 3)):
        positions.append(Position(x - 2, y + 3))

    if (return_valid_position(x + 2, y + 3)):
        positions.append(Position(x + 2, y + 3))

    if (return_valid_position(x + 3, y + 2)):
        positions.append(Position(x + 3, y + 2))

    if (return_valid_position(x + 3, y - 2)):
        positions.append(Position(x + 3, y - 2))

    if (return_valid_position(x + 2, y - 3)):
        positions.append(Position(x + 2, y - 3))

    if (return_valid_position(x - 2, y - 3)):
        positions.append(Position(x - 2, y - 3))

    if (return_valid_position(x - 3, y - 2)):
        positions.append(Position(x - 3, y - 2))

    if (return_valid_position(x - 3, y + 2)):
        positions.append(Position(x - 3, y + 2))

    return positions


#STARTER CODE SOLUTION
def is_knight_on_board(x, y, k, cache={}):
    current_positions = [Position(x, y)]
    new_positions = []

    for i in range(k):
        for j in current_positions:
            new_positions += get_possible_positions(j.x, j.y)[:]
        current_positions = new_positions[:]
        new_positions = []

    return float(invalid_positions) / float(valid_positions + invalid_positions)

print is_knight_on_board(0, 0, 1)
