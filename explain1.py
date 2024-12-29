import collections
explain1 = {"surface":27.0312, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":1.41176, "unableToBurn":-0}

explain2 = {"surface":23.2222, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":-0.213235, "unableToBurn":-0.52758}

explain3 = collections.defaultdict(float, {'surface': 29.22, 'unableToBurn': -14.93, 'highCol9': -5.00, 'tetrisReady': 6.00, 'builtOutLeft': 1.26})

explain4 = collections.defaultdict(float, {'surface': 28.55, 'unableToBurn': -1.89, 'tetrisReady': 6.00, 'builtOutLeft': 1.59})

KEYS = ['surface', 'surfaceLeft', 'avgHeight', 'lineClear', 'hole', 'holeWeight', 'guaranteedBurns', 'likelyBurns', 'inaccessibleLeft', 'inaccessibleRight', 'coveredWell', 'highCol9', 'tetrisReady', 'builtOutLeft', 'unableToBurn']

KEY_EXPLAIN = ['surface', 'surface left', 'average height', 'line clear', 'hole', 'hole weight', 'guaranteed burns', 'likely burns', 'inaccessible left', 'inaccessible right', 'covered well', 'high col 9', 'tetris ready', 'built out left', 'unable to burn']

translations = {'tetrisReady':"This stack is tetris ready.", 'avgHeight':"The average height is lower, while the other risks topout.", 'surfaceLeft':"Your left is stronger.", 'lineClear':"This move scored points.", 'hole':"This avoids putting holes in the stack that must be uncovered.", 'guaranteedBurns':"This placement avoids burns.", 'likelyBurns':"This placement avoids burns that might not be forced.", 'inaccessibleLeft':"Your left is accessible.", 'inaccessibleRight':"Your right is accessible.", 'coveredWell':"This avoids covering your well.", 'highCol9':"Your column 9 is lower.", 'unableToBurn':"This stack makes it possible to burn."}

negativeTranslations = {'tetrisReady':"This stack is not tetris ready.", 'avgHeight':"Your average height is too high causing this board to be prone to topout.", 'surfaceLeft':"Your left is weaker.", 'lineClear':"This move scored fewer points.", 'hole':"This puts holes in the stack that must be uncovered.", 'guaranteedBurns':"This placement requires burns to get a tetris.", 'likelyBurns':"This placement will likely result in burns.", 'inaccessibleLeft':"Your left is inaccessible.", 'inaccessibleRight':"Your right is inaccessible.", 'coveredWell':"This placement covers your well.", 'highCol9':"Your column 9 is too high.", 'unableToBurn':"This stack makes difficult to burn."}

SMALL = 0.1

def surface_logic(a, b):
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
    return 'The surface is better'

def compare(a, b):
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
                    res2 = surface_logic(a, b)
            else:
                res += '{0} is better {1:1.3f}, '.format(KEY_EXPLAIN[i], val)
    # strip the final comma space
    if res2: res = ' ' + res
    return res2 + res[:-2]

def main():
    print(compare(explain1, explain2))
    print(compare(explain4, explain3))

if __name__ == '__main__':
    main()
