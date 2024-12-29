#!/usr/bin/env python3
"""
StackRabbit Evaluation Explain
by Javantea
Dec 27-28, 2024

"""
import collections

# Test data to help us determine whether we are
explain1 = {"surface":27.0312, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":1.41176, "unableToBurn":-0}
board1 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000001001110100111111111011111111101111111110111111111011111111101111111110'

explain2 = {"surface":23.2222, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":-0.213235, "unableToBurn":-0.52758}
board2 ='00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011110000001111100000111111011111111101111111110111111111011111111101111111110'

#explain3 = collections.defaultdict(float, {'surface': 29.22, 'unableToBurn': -14.93, 'highCol9': -5.00, 'tetrisReady': 6.00, 'builtOutLeft': 1.26})
explain3 = {"surface":23.3706, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":1.20615, "unableToBurn":-1.96632}
board3 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001110001100111001111011101111101111111110111111111011111111101111111110'

#explain4 = collections.defaultdict(float, {'surface': 28.55, 'unableToBurn': -1.89, 'tetrisReady': 6.00, 'builtOutLeft': 1.59})
explain4 = {"surface":20.0602, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-7.2, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":0.344615, "unableToBurn":-2.35958}
board4 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000100000000010000000011000000001100110001111011101111101111111110111111111011111111101111111110'

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
    if len(value) == 1: return 'is'
    return 'are'

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
    """
    # FIXME: need .. in sys.path. It's done in main and explainer1.py.
    #import tetris_cheat1
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
    for col in range(9):
        if col == WELL_COLUMN: continue
        diff_a = surface_a[col] - surface_a[col+1]
        diff_b = surface_b[col] - surface_b[col+1]
        cost_a.append(abs(diff_a))
        cost_b.append(abs(diff_b))
        if cost_a[-1] < cost_b[-1]:
            better.append(col)
        elif cost_a[-1] > cost_b[-1]:
            worse.append(col)
    print(cost_a, cost_b)
    print(better, worse)

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
    return 'Col {0} {1} better {2}'.format(''.join(map(str, better)), is_are(better), worse_str)

def compare(a, b, board_a=None, board_b=None, short=False):
    """
    Returns a string that explains the evaluation made by StackRabbit.
    """
    diff_val = [a[key] - b[key] for key in KEYS]
    most_important = max(diff_val)
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
    if res2: res = ' ' + res
    return res2 + res[:-2]

def main():
    #import sys
    #sys.path.append('..')
    print(compare(explain1, explain2, board1, board2))
    print(surface_logic(explain3, explain4, board3, board4))
    print(compare(explain3, explain4, board4, board3))

if __name__ == '__main__':
    main()
