#!/usr/bin/env python3
"""
StackRabbit Evaluation Explain
by Javantea
Dec 27-28, 2024

"""
import collections

def to_board(short_board):
    """
    Converts a board line one printed
    """
    board = short_board.split('\n')
    # fill the top with empty rows
    board = ['0'*10] * (20-len(board)) + board
    # Make sure each row is filled out using 0s instead of space
    for row in range(20):
        row_len = len(board[row])
        if ' ' in board[row]: board[row] = board[row].replace(' ', '0')
        if row_len == 10: continue
        board[row] = board[row] + ('0' * (10 - row_len))
    return ''.join(board)

# Test data to help us determine whether we are
explain1 = {"surface":27.0312, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":1.41176, "unableToBurn":-0}
#board1 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000001001110100111111111011111111101111111110111111111011111111101111111110'
board1 = to_board("""
   1
1  111 1
111111111
111111111
111111111
111111111
111111111
111111111""")

explain2 = {"surface":23.2222, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":-0.213235, "unableToBurn":-0.52758}
#board2 ='00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011110000001111100000111111011111111101111111110111111111011111111101111111110'
board2 = to_board("""
   1111
   11111
   111111
111111111
111111111
111111111
111111111
111111111""")

#explain3 = collections.defaultdict(float, {'surface': 29.22, 'unableToBurn': -14.93, 'highCol9': -5.00, 'tetrisReady': 6.00, 'builtOutLeft': 1.26})
explain3 = {"surface":23.3706, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":1.20615, "unableToBurn":-1.96632}
#board3 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001110001100111001111011101111101111111110111111111011111111101111111110'
board3 = to_board("""
111   11
111  1111
111 11111
111111111
111111111
111111111
111111111""")

#explain4 = collections.defaultdict(float, {'surface': 28.55, 'unableToBurn': -1.89, 'tetrisReady': 6.00, 'builtOutLeft': 1.59})
explain4 = {"surface":20.0602, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-7.2, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":0.344615, "unableToBurn":-2.35958}
#board4 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000010000000011000000001100110001111011101111101111111110111111111011111111101111111110'
board4 = to_board("""
       1
       1
      11
      11
11   1111
111 11111
111111111
111111111
111111111
111111111""")

#board5 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001100110000111011111011101111101110111111111011111111101111111110'

board6 = to_board("""
       1
       1
      11
      11
11   1111
111 11111
111111111
111111111
111111111
111111111""")

board5 = to_board("""
      11
11    111
11111 111
11111 111
111111111
111111111
111111111""")

#board6 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000010000000011000000001100110001111011101111101111111110111111111011111111101111111110'

# minimal left l dependency
board7 = to_board("""
  1
1 1
1 1""")

# minimal left j dependency
board8 = to_board("""
 1
 1""")

# minimal j dependency col 2
board9 = to_board("""
1
1 1
1 1""")

# minimal bad parity
board11 = to_board("""
 1 1 1 1
111111111""")

# minimal improved parity comparison
board10 = to_board("""
1 1  1 1
111111111""")

# minimal improved parity comparison to board13
board12 = to_board("""
 11
111111111""")

# minimal worse parity
board13 = to_board("""
 1 1
111111111""")

# minimal improved parity comparison to board15
board14 = to_board("""
 111
111111111""")

# minimal worse parity
board15 = to_board("""
 1 11
111111111""")

# minimal improved parity comparison to board17
board16 = to_board("""
  111
111111111""")

# minimal worse parity
board17 = to_board("""
 11 1
111111111""")

# puzzle 83 solution
board18 = to_board("""
1
11
11  11
1111111
1111111
11111111
111111111
111111111
111111111""")

# puzzle 83 2nd best solution
board19 = to_board("""
1     1
11   11
11  111
1111111
1111111
11111111
11111111
11111111
11111111
111111111""")

KEYS = ['surface', 'surfaceLeft', 'avgHeight', 'lineClear', 'hole', 'holeWeight', 'guaranteedBurns', 'likelyBurns', 'inaccessibleLeft', 'inaccessibleRight', 'coveredWell', 'highCol9', 'tetrisReady', 'builtOutLeft', 'unableToBurn']

KEY_EXPLAIN = ['surface', 'surface left', 'average height', 'line clear', 'hole', 'hole weight', 'guaranteed burns', 'likely burns', 'inaccessible left', 'inaccessible right', 'covered well', 'high col 9', 'tetris ready', 'built out left', 'unable to burn']

translations = {'tetrisReady':"This stack is tetris ready.", 'avgHeight':"The average height is lower, while the other risks topout.", 'surfaceLeft':"Your left is stronger.", 'lineClear':"This move scored points.", 'hole':"This avoids putting holes in the stack that must be uncovered.", 'holeWeight':"This puts less weight on holes.", 'guaranteedBurns':"This placement avoids burns.", 'likelyBurns':"This placement avoids burns that might not be forced.", 'inaccessibleLeft':"Your left is accessible.", 'inaccessibleRight':"Your right is accessible.", 'coveredWell':"This avoids covering your well.", 'highCol9':"Your column 9 is lower.", 'unableToBurn':"This stack makes it possible to burn.", 'builtOutLeft':'This has a better built out left.'}

negativeTranslations = {'tetrisReady':"This stack is not tetris ready.", 'avgHeight':"Your average height is too high causing this board to be prone to topout.", 'surfaceLeft':"Your left is weaker.", 'lineClear':"This move scored fewer points.", 'hole':"This puts holes in the stack that must be uncovered.", 'holeWeight':"This puts more weight on holes.", 'guaranteedBurns':"This placement requires burns to get a tetris.", 'likelyBurns':"This placement will likely result in burns.", 'inaccessibleLeft':"Your left is inaccessible.", 'inaccessibleRight':"Your right is inaccessible.", 'coveredWell':"This placement covers your well.", 'highCol9':"Your column 9 is too high.", 'unableToBurn':"This stack makes difficult to burn.", 'builtOutLeft':'Your left is weaker.'}

for key in KEYS:
    if key == 'surface': continue
    assert key in translations, 'need key in translations: {0}'.format(key)
    assert key in negativeTranslations, 'need key in negativeTranslations: {0}'.format(key)

SMALL = 0.1

def get_col(board, i):
    return board[i*10:(i+1)*10].replace('0', ' ')

def print_boards(boarda, boardb, file=None):
    """
    Print any rows that have information in them.
    Of course we want to avoid skipping empty lines that are below lines with data in them.
    """
    top_of_board = True
    for i in range(20):
        if top_of_board:
            a_empty = boarda[i*10:(i+1)*10] == '0000000000'
            if a_empty:
                b_empty = boardb[i*10:(i+1)*10] == '0000000000'
                if b_empty:
                    continue
            top_of_board = False
        print(get_col(boarda, i), get_col(boardb, i), file=file)

def get_surface_array(board):
    """
    Similar to getSurfaceArray in utils.hpp.
    TODO: compare.
    """
    out_surface = [0] * 10
    for col in range(10):
        rout = 20
        for row in range(20):
            if board[row*10+col] == '1':
                rout = row
                break
        out_surface[col] = 20 - rout
    return out_surface

# from config.hpp. that's our right well. We can swap to any column we want =]
WELL_COLUMN = 9

def is_are(value):
    """
    Pluralizes the english verb to be in the form is/are based on a list/tuple input.
    is_are([1, 2]) returns 'are'
    is_are([]) returns 'are'
    is_are([3]) returns 'is'
    is_are([0]) returns 'is'
    The reason behind [] returning are is this situation: A and B are correct. "None are correct"
    """
    if len(value) == 1: return 'is'
    return 'are'

def is_L_dependent(surface):
    """
    Checks for L dependency using the 537 tool. A surface is L dependent when:
    there is a drop of 2
    and
    then an increase of 3 or more.
    """
    L_dependent = []
    for col in range(9):
        if col == WELL_COLUMN: continue
        diff = surface[col] - surface[col+1]
        if diff == 2: L_dependent.append(col)
    for col in L_dependent:
        next_col = col + 1
        if next_col >= 9: continue
        diff_next = surface[next_col] - surface[next_col+1]
        if diff_next < -2:
            return True
    return False


def is_J_dependent(surface):
    """
    Checks for J dependency using the 735 tool. A surface is J dependent when:
    there is a drop of 2
    and
    then an increase of 3 or more.
    """
    #print('jd', surface)
    J_dependent = []
    for col in range(9):
        if col == WELL_COLUMN: continue
        diff = surface[col] - surface[col+1]
        if col == 0:
            #print('left j', diff)
            # left J dependency
            if diff == -2: return True
        if diff == -2: J_dependent.append(col)
    #print('jdep', J_dependent)
    for col in J_dependent:
        prev_col = col - 1
        if prev_col < 0: continue
        diff_next = surface[prev_col] - surface[prev_col+1]
        #print('diff_next', diff_next)
        if diff_next > 2:
            return True
    return False

#print_boards(board8, board9)
assert(is_J_dependent(get_surface_array(board8)))
assert(is_J_dependent(get_surface_array(board9)))

def surface_logic(a, b, board_a, board_b):
    """
    Surface is an important issue that we can say a lot about.
    Parity..

    Your stack is broken.
    Your stack is wrecked.
    Your stack has minor problems.
    Your parity is destroyed.
    Your parity is bad.
    You have a place for O pieces, but not S.
    You have no place for _ pieces.
    Your board has a high right.
    Your board looks nice, but has dependencies.
    You are J dependent, which is fine if your stack is flat.
    You are L dependent, which is usually bad.
    You have a dependency that needs a dependency after that. (L I, J I, Z I, or S I).
    You created an I dependency.
    You have a spire.
    You have two dependencies.
    You have 3 dependencies. Why not 4?

    Unfortunately we need the input board to know exactly what it didn't like.
    But we can explain each one using the code from StackRabbit, specifically eval.cpp rateSurface.

    It now occurs to me why surface dominates. It's because that's the thing that determines whether you are scoring tetrises vs burns when you aren't digging.
    """
    # We need the resultingBoard from StackRabbit to know what the surface is like.
    if board_b is None or board_a is None:
        return 'The surface is better'
    print('a          b')
    print_boards(board_a, board_b)
    surface_a = get_surface_array(board_a)
    surface_b = get_surface_array(board_b)
    print(surface_a, surface_b)
    cost_a, cost_b = [], []
    better = []
    worse = []
    L_dependent = []
    for col in range(9):
        if col == WELL_COLUMN: continue
        # TODO: Double well code from rateSurface
        diff_a = surface_a[col] - surface_a[col+1]
        diff_b = surface_b[col] - surface_b[col+1]
        if diff_b == 2: L_dependent.append(col)
        cost_a.append(abs(diff_a))
        cost_b.append(abs(diff_b))
        if cost_a[-1] < cost_b[-1]:
            better.append(col)
        elif cost_a[-1] > cost_b[-1]:
            worse.append(col)
    print(cost_a, cost_b)
    print(better, worse)
    if 0 not in cost_b:
        # There is nowhere to place an O piece (see board11).
        if 0 in cost_a:
            return "Better parity"
    if max(cost_b) > max(cost_a) + 4:
        # TODO: Test
        return 'This avoids a spire'
    L_dependency_actual = []
    if L_dependent:
        #print('L', L_dependent)
        for col in L_dependent:
            next_col = col + 1
            if next_col >= 9: continue
            diff_next = surface_b[next_col] - surface_b[next_col+1]
            if diff_next < -2:
                L_dependency_actual.append(col)
        if L_dependency_actual:
            print('L verified', L_dependency_actual)
            if not is_L_dependent(surface_a):
                # TODO: test and more nuance (in case the L dependency is not the highest priority).
                return 'This avoids an L dependency'

    if is_J_dependent(surface_b) and not is_J_dependent(surface_a):
        return 'This avoids a J dependency'

    worse_str = ''
    if len(better) == 1:
        if worse:
            worse_str = 'but Col {0} {1} worse'.format(''.join(map(str, worse)), is_are(worse))
        return 'Col {0} {1} better {2}'.format(''.join(map(str, better)), is_are(better), worse_str)
    # Multiple columns are better.
    if len(better) > 4:
        return 'The stack is much better {0}'.format(''.join(map(str, better)))
    # 2-3 columns are better.
    if worse:
        worse_str = 'but Col {0} {1} worse'.format(''.join(map(str, worse)), is_are(worse))
    if len(better) >= 2:
        # Improved parity by putting 2 minos together. (see board12 and board13, 14 and 15)
        dbetter = [better[i+1] - better[i] for i in range(len(better) - 1)]
        if 1 in dbetter:
            # handle 16 and 17
            first_one = dbetter.index(1)
            print('first one debug', first_one)
            #print('db', dbetter)
            print('cost', cost_a[better[first_one]], cost_b[better[first_one]])
            dcost = cost_b[better[first_one]] - cost_a[better[first_one]]
            if dcost == 1:
                return 'Better parity in columns {0} and {1}'.format(better[first_one]+1, better[first_one]+2)
            return 'Better shape in columns {0} and {1}'.format(better[first_one]+1, better[first_one]+2)
        else:
            return 'Better parity in columns {0} and {1}'.format(better[0]+1, better[0]+2)
    return 'Col {0} {1} better {2}'.format(''.join(map(str, better)), is_are(better), worse_str)

def compare(a, b, board_a=None, board_b=None, short=False):
    """
    Returns a string that explains the evaluation made by StackRabbit.
    """
    # TODO: when the eval is in favor of b, that's stackrabbit 2.0's thing but this code is clearly not it.
    # Also it never really occurs as far as I can tell.
    diff_val = [a[key] - b[key] for key in KEYS]
    most_important = max(diff_val)
    if most_important < 0:
        # it's for sure worse.
        res = 'StackRabbit 2 playout is better'
        res2 = ''
    else:
        # TODO: is it worthwhile to sum and check for SR2?
        res = ''
        res2 = ''
    for i in range(len(diff_val)):
        val = diff_val[i]
        if abs(val) < SMALL: continue
        if val < 0:
            res += '{0} is worse {1:1.3f}, '.format(KEY_EXPLAIN[i], -val)
        else:
            if val == most_important:
                res += '{0} is the most important {1:1.3f}, '.format(KEY_EXPLAIN[i], val)
                if KEYS[i] in translations:
                    res2 = translations[KEYS[i]]
                elif KEYS[i] == 'surface':
                    # surface logic
                    res2 = surface_logic(a, b, board_a, board_b)
            else:
                res += '{0} is better {1:1.3f}, '.format(KEY_EXPLAIN[i], val)
    # strip the final comma space
    if short and res2: return res2
    if short:
        print('FIXME: short for this one', a, b)
    res = res[:-2]
    if res2: return res2 + ' ' + res
    return res

def main():
    print(compare(explain1, explain2, board1, board2))
    print(surface_logic(explain3, explain4, board3, board4))
    print(compare(explain3, explain4, board4, board3))
    print(surface_logic({}, {}, board6, board5))
    # 7 is L dependent, 6 is not.
    print(surface_logic({}, {}, board6, board7))
    # 8 is J dependent, 6 is not.
    print(surface_logic({}, {}, board6, board8))
    # 9 is J dependent, 6 is not.
    print(surface_logic({}, {}, board6, board9))
    # Both have J dependencies.
    print(surface_logic({}, {}, board8, board9))
    # 10 has better parity than 11 otherwise the same.
    print(surface_logic({}, {}, board10, board11))
    # 12 has better parity than 13 otherwise the same.
    print(surface_logic({}, {}, board12, board13))
    # 14 has better parity than 15 otherwise the same.
    print(surface_logic({}, {}, board14, board15))
    # 16 has better parity than 17 otherwise the same.
    print(surface_logic({}, {}, board16, board17))
    # 18 has better stack than 19 otherwise the same.
    print(surface_logic({}, {}, board18, board19))

if __name__ == '__main__':
    main()
