assignments = []

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [a + b for a in A for b in B]

rows = 'ABCDEFGHI'
cols = '123456789'
boxes = cross(rows, cols)
row_units = [cross(row, cols) for row in rows]
col_units = [cross(rows, col) for col in cols]
square_units = [cross(row, col) for row in ['ABC', 'DEF', 'GHI'] for col in ['123', '456', '789']]
diag_units = [[a + b for a, b in zip(A, cols)] for A in [rows, reversed(rows)]] # Two diagonal units
units = row_units + col_units + square_units + diag_units # List of all units
peers = {box: set(sum([unit for unit in units if box in unit], [])) - {box} for box in boxes} # Dictionary of box to its peers

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    return {box: value if value != '.' else '123456789' for box, value in zip(cross(rows, cols), grid)}

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = max(len(values[box]) for box in boxes) + 1
    for row in rows:
        print(''.join(values[row + col].center(width) + ('|' if col in '36' else '') for col in cols))
        if row in 'CF':
            print('+'.join(['-'*(width*3)]*3))

def eliminate(values):
    """
    If a box is filled in eliminate its value from its peers.
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        values(dict): The sudoku with filled in values removed from peers
    """
    for box, value in values.items():
        if len(value) == 1: # Pick the filled in boxes
            for peer in peers[box]: # Find its peers
                values = assign_value(values, peer, values[peer].replace(value, "")) # Remove corresponding value from peers
    return values

def only_choice(values):
    """
    If a value is only possible in one box across a unit fill that box with the value
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        values(dict): The sudoku with values with only one place to go set
    """
    for unit in units:
        for value in '123456789':
            choices = [box for box in unit if value in values[box]] # Possible boxes for a value in one unit
            if len(choices) == 1: # One choice means the value has only one place to go
                values = assign_value(values, choices[0], value) # Set the only-choice box to the value
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    for unit in units:
        twins = {a for a in unit for b in unit if values[a] == values[b] and a is not b and len(values[a]) == 2} # All boxes that are twins in a unit
        for box in set(unit) - twins: # Exclude the twins from boxes that need to be updated
            for value in values[box]:
                if value in ''.join(values[twin] for twin in twins): # If a value belongs to one of the twins, eliminate it
                    values = assign_value(values, box, values[box].replace(value, ''))
    return values

def reduce_puzzle(values):
    """
    Narrow search space using three strategies: eliminate, only_choice and naked_twins
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        values(dict): The sudoku dictionary after exhausting all possible elimination using the three strategies
        False(bool): If the sudoku is in an illegal state
    """
    while True:
        solved_before = len([box for box in boxes if len(values[box]) == 1]) # Number of filled in boxes before reduction
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_after = len([box for box in boxes if len(values[box]) == 1]) # Number of filled in boxes after reduction
        if solved_before == solved_after: # Break when there is no more elimination possible
            break
    return False if any(len(values[box]) == 0 for box in boxes) else values # Detect constraint violation 


def search(values):
    """
    Find a solution for the sudoku, use trial and error if no further elimination is possible
    Args:
        values(dict): The sudoku in dictionary form
    Returns:
        values(dict): The solved sudoku
        False(bool): If the sudoku is not solvable
    """
    values = reduce_puzzle(values) # Exhaust all elimination to minimize potential searching
    if not values: # Fail early if the search path reaches a contradiction
        return False
    if all(len(values[box]) == 1 for box in boxes): # Detect if sudoku is already solved
        return values
    _, node = min((len(values[box]), box) for box in boxes if len(values[box]) > 1) # Select box with minimal number of values to try out
    for value in values[node]:
        branch = values.copy()
        branch = assign_value(branch, node, value) # Set the node to the hypothetical value
        branch = search(branch) # Reapply the process to this branch of possible states
        if branch: # Return the solution if found
            return branch
    return False # No legal state possible for this sudoku


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    grid = grid_values(grid)
    grid = search(grid)
    return grid

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))


    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
