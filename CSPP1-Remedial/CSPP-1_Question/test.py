from collections import defaultdict
assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [r+c for r in A for c in B]

boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
diagonal_units = [[rows[i]+cols[i] for i in range(len(rows))],
                  [rows[len(rows)-1-i]+cols[i] for i in range(len(rows))]]
unitlist = row_units + column_units + square_units + diagonal_units
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Naked twins also works by units
    # Iterate over all units, if naked twins exists, 
    # then apply it to remove possibilities of the peers
    for u in unitlist:
        
        # Colllect all twins in a dictionary: {possible numbers: [locations]}
        # Notice that a twin just mean this box has 2 possible numbers
        nt = defaultdict(list)
        for box in u:
            if len(values[box]) == 2:
                nt[values[box]].append(box)
        
        # Iterate through the twins, find the naked twins, and
        # eliminate among their shared peers
        for numbers, locations in nt.items():
            if len(locations) == 2: # this is a naked twins
                a, b = locations
                num1, num2 = numbers 
                shared_peers = set(peers[a]).intersection(set(peers[b]))
                for peer in shared_peers:
                    values[peer] = values[peer].replace(num1, "")
                    values[peer] = values[peer].replace(num2, "")
    
    return values
    
def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Input: A grid in string form.
    Output: A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(boxes, chars))

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        #print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
         #             for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    
    # If couldn't find a valid board, return false
    if values == False:
        return False
    
    # If find a valid board, see if it's a solution
    choices_per_box = [(len(values[box]), box) for box in boxes]
    solved = all([choice_box[0] == 1 for choice_box in choices_per_box])
    if solved:
        return values
    
    # Now it's a valid board but not a solution yet
    # Use recursion to solve each one of the resulting sudokus,
    
    # Choose one of the unfilled squares with the fewest possibilities
    min_choice, min_choice_box = min([choice_box for choice_box in choices_per_box
                                      if choice_box[0] > 1])
    
    # For all choices, fill one at a time,
    # then recursively search on the updated board:
    for num in values[min_choice_box]:
        new_values = values.copy()
        new_values[min_choice_box] = num
        attempt = search(new_values)
        if attempt:
            return attempt
    
def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    #display(values)
    attempt = search(values)
    
    if attempt:
        return attempt
        print("Given sudoku is solved")
    else:
        display(grid_values(grid))
        print()
        raise Exception("Can't solve this Soduku!")

if __name__ == '__main__':
    diag_sudoku_grid = input()
    #'2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')