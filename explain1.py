explain1 = {"surface":27.0312, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":1.41176, "unableToBurn":-0}

explain2 = {"surface":23.2222, "surfaceLeft":0, "avgHeight":-0, "lineClear":-0, "hole":-0, "holeWeight":0, "guaranteedBurns":-0, "likelyBurns":-0, "inaccessibleLeft":-0, "inaccessibleRight":-0, "coveredWell":-0, "highCol9":-0, "tetrisReady":6, "builtOutLeft":-0.213235, "unableToBurn":-0.52758}

KEYS = ['surface', 'surfaceLeft', 'avgHeight', 'lineClear', 'hole', 'holeWeight', 'guaranteedBurns', 'likelyBurns', 'inaccessibleLeft', 'inaccessibleRight', 'coveredWell', 'highCol9', 'tetrisReady', 'builtOutLeft', 'unableToBurn']

KEY_EXPLAIN = ['surface', 'surface left', 'average height', 'line clear', 'hole', 'hole weight', 'guaranteed burns', 'likely burns', 'inaccessible left', 'inaccessible right', 'covered well', 'high col 9', 'tetris ready', 'built out left', 'unable to burn']


SMALL = 0.1

def compare(a, b):
    diff_val = [a[key] - b[key] for key in KEYS]
    most_important = max(diff_val)
    res = ''
    for i in range(len(diff_val)):
        val = diff_val[i]
        if abs(val) < SMALL: continue
        if val < 0:
            res += '{0} is worse {1:1.3f}, '.format(KEY_EXPLAIN[i], -val)
        else:
            if val == most_important:
                res += '{0} is the most important {1:1.3f}, '.format(KEY_EXPLAIN[i], val)
            else:
                res += '{0} is better {1:1.3f}, '.format(KEY_EXPLAIN[i], val)
    # strip the final comma space
    return res[:-2]

def main():
    print(compare(explain1, explain2))

if __name__ == '__main__':
    main()
