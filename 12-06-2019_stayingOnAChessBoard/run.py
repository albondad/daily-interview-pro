#NOTES
# - a knight always has 8 possible moves
# - total possible leaves / total possible moves
# - total possible moves != k^8, because once the knight leaves the board it can't move
# - need to figure out each possible position for each move

# - step01: figure out all positions, store in array
# - step01: search array, figure out all valid positions (check when position is in board)
# - step02: search array, figure out all invalid positions (check when position is off board, disregard moves after off board)
# - step02: total positions = valid positions + invalid positions
# - step03: invalid positions / total positions = probability knight can't move


#VARIABLES
valid_positions = 0
invalid_positions = 0

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
    if ( x > 0 or x > 8 or y < 0 or y > 8):
        result = True
        valid_positions += 1
    else:
        result = False
        invalid_positions += 1
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

#given parameters of array of positions and number moves, returns array of all possible valid positions
def get_all_positions(array, k):
    current_positions = array[:]
    new_positions = []
    all_positions = []

    for i in range(k):
        for j in current_positions:
            new_positions += get_possible_positions(j.x, j.y)[:]
            all_positions += get_possible_positions(j.x, j.y)[:]
        current_positions = new_positions[:]
        new_positions = []

    return all_positions




#DEBUGGING
get_all_positions(get_possible_positions(0, 0), 1)
#print invalid_positions
#print valid_positions
print 'Probability:', valid_positions, '/', valid_positions + invalid_positions
