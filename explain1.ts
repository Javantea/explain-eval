/*
 * Minimal StackRabbit Evaluation Explain
 * by Javantea
 * Dec 27, 2024
 *
 * To use:
node_modules/typescript/bin/tsc explain1.ts
node explain1.js
surface is the most important 3.809, built out left is better 1.625, unable to burn is better 0.528
 */

type EvalExplain = {
  surface: number;
  surfaceLeft: number;
  avgHeight: number;
  lineClear: number;
  hole: number;
  holeWeight: number;
  guaranteedBurns: number;
  likelyBurns: number;
  inaccessibleLeft: number;
  inaccessibleRight: number;
  coveredWell: number;
  highCol9: number;
  tetrisReady: number;
  builtOutLeft: number;
  unableToBurn: number;
};

const explain1: EvalExplain = {
  surface: 27.0312,
  surfaceLeft: 0,
  avgHeight: 0,
  lineClear: 0,
  hole: 0,
  holeWeight: 0,
  guaranteedBurns: 0,
  likelyBurns: 0,
  inaccessibleLeft: 0,
  inaccessibleRight: 0,
  coveredWell: 0,
  highCol9: 0,
  tetrisReady: 6,
  builtOutLeft: 1.41176,
  unableToBurn: 0,
};

const explain2: EvalExplain = {
  surface: 23.2222,
  surfaceLeft: 0,
  avgHeight: 0,
  lineClear: 0,
  hole: 0,
  holeWeight: 0,
  guaranteedBurns: 0,
  likelyBurns: 0,
  inaccessibleLeft: 0,
  inaccessibleRight: 0,
  coveredWell: 0,
  highCol9: 0,
  tetrisReady: 6,
  builtOutLeft: -0.213235,
  unableToBurn: -0.52758,
};

const KEYS = ['surface', 'surfaceLeft', 'avgHeight', 'lineClear', 'hole', 'holeWeight', 'guaranteedBurns', 'likelyBurns', 'inaccessibleLeft', 'inaccessibleRight', 'coveredWell', 'highCol9', 'tetrisReady', 'builtOutLeft', 'unableToBurn'];

const KEY_EXPLAIN = ['surface', 'surface left', 'average height', 'line clear', 'hole', 'hole weight', 'guaranteed burns', 'likely burns', 'inaccessible left', 'inaccessible right', 'covered well', 'high col 9', 'tetris ready', 'built out left', 'unable to burn'];


const SMALL = 0.1;

/*
 * Returns a string that explains the evaluation made by StackRabbit.
 */
function compareExplain(a, b) : string
{
    const diff_val: number[] = KEYS.map((key) => a[key] - b[key]);
    const most_important = Math.max(...diff_val);
    var res: string = '';
    for (var i = 0; i < diff_val.length; i++)
    {
        const val = diff_val[i];
        if (Math.abs(val) < SMALL) continue;
        if(val < 0)
        {
            res += `${KEY_EXPLAIN[i]} is worse ${val}, `;
        }
        else
        {
            if (val == most_important)
                res += `${KEY_EXPLAIN[i]} is the most important ${val.toFixed(3)}, `
            else
                res += `${KEY_EXPLAIN[i]} is better ${val.toFixed(3)}, `
        }
    }
    //# strip the final comma space
    return res.substring(0, res.length-2);
}

// Show the user the reason why explain1 is better than explain2.
console.log(compareExplain(explain1, explain2));
