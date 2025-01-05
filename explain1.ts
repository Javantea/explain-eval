/*
 * StackRabbit Evaluation Explain
 * by Javantea
 * Dec 27, 2024 - Jan 1, 2025
 *
 * Ported from Python
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
const board1 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000010000001001110100111111111011111111101111111110111111111011111111101111111110';

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
const board2 = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011110000001111100000111111011111111101111111110111111111011111111101111111110';

// This is needed to deal with the KEYS.map in compareExplain.
type ExplainProperties = 'surface' | 'surfaceLeft' | 'avgHeight' | 'lineClear' | 'hole' | 'holeWeight' | 'guaranteedBurns' | 'likelyBurns' | 'inaccessibleLeft' | 'inaccessibleRight' | 'coveredWell' | 'highCol9' | 'tetrisReady' | 'builtOutLeft' | 'unableToBurn';

const KEYS: ExplainProperties[] = ['surface', 'surfaceLeft', 'avgHeight', 'lineClear', 'hole', 'holeWeight', 'guaranteedBurns', 'likelyBurns', 'inaccessibleLeft', 'inaccessibleRight', 'coveredWell', 'highCol9', 'tetrisReady', 'builtOutLeft', 'unableToBurn'];

const KEY_EXPLAIN = ['surface', 'surface left', 'average height', 'line clear', 'hole', 'hole weight', 'guaranteed burns', 'likely burns', 'inaccessible left', 'inaccessible right', 'covered well', 'high col 9', 'tetris ready', 'built out left', 'unable to burn'];


const translations = {'tetrisReady':"This stack is tetris ready.", 'avgHeight':"The average height is lower, while the other risks topout.", 'surfaceLeft':"Your left is stronger.", 'lineClear':"This move avoided a burn.", 'hole':"This avoids putting holes in the stack that must be uncovered.", 'holeWeight':"This puts less weight on holes.", 'guaranteedBurns':"This placement avoids burns.", 'likelyBurns':"This placement avoids burns that might not be forced.", 'inaccessibleLeft':"Your left is accessible.", 'inaccessibleRight':"Your right is accessible.", 'coveredWell':"This avoids covering your well.", 'highCol9':"Your column 9 is lower.", 'unableToBurn':"This stack makes it possible to burn.", 'builtOutLeft':'This has a better built out left.', 'surface':''};

const negativeTranslations = {'tetrisReady':"This stack is not tetris ready.", 'avgHeight':"Your average height is too high causing this board to be prone to topout.", 'surfaceLeft':"Your left is weaker.", 'lineClear':"This is a burn costing pace.", 'hole':"This puts holes in the stack that must be uncovered.", 'holeWeight':"This puts more weight on holes.", 'guaranteedBurns':"This placement requires burns to get a tetris.", 'likelyBurns':"This placement will likely result in burns.", 'inaccessibleLeft':"Your left is inaccessible.", 'inaccessibleRight':"Your right is inaccessible.", 'coveredWell':"This placement covers your well.", 'highCol9':"Your column 9 is too high.", 'unableToBurn':"This stack makes difficult to burn.", 'builtOutLeft':'Your left is weaker.'}

const SMALL = 0.1;

// from config.hpp. that's our right well. We can swap to any column we want =]
const WELL_COLUMN = 9;

/*
    Similar to getSurfaceArray in utils.hpp.
    TODO: compare.
*/
function get_surface_array(board: string)
{
    let out_surface: number[] = [0,0,0,0,0,0,0,0,0,0];
    for (let col = 0; col < 10; col++) {
        let rout = 20;
        for (let row = 0; row < 20; row++) {
            if (board[row*10+col] == '1') {
                rout = row;
                break;
            }
        }
        out_surface[col] = 20 - rout;
    }
    return out_surface;
}

/*
  Pluralizes the english verb to be in the form is/are based on a list/tuple input.
  is_are([1, 2]) returns 'are'
  is_are([]) returns 'are'
  is_are([3]) returns 'is'
  is_are([0]) returns 'is'
  The reason behind [] returning are is this situation: A and B are correct. "None are correct"
 */
function is_are(value: any[])
{
    if (value.length == 1) return 'is';
    return 'are';
}

/*
 *  Checks for L dependency using the 537 tool. A surface is L dependent when:
 *  there is a drop of 2 and then an increase of 3 or more.
 */
function is_L_dependent(surface: number[]): boolean
{
    // TODO test
    let L_dependent = [];
    for (var col = 0; col < 9; col++) {
        if (col == WELL_COLUMN) continue;
        const diff = surface[col] - surface[col+1];
        if (diff == 2) L_dependent.push(col);
    }
    for (var col of L_dependent) {
        const next_col = col + 1;
        if (next_col >= 9) continue;
        const diff_next = surface[next_col] - surface[next_col+1];
        if (diff_next < -2) {
            return true;
        }
    }
    return false;
}

/*
 * Checks for J dependency using the 735 tool. A surface is J dependent when:
 *  there is a drop of 3 or more.
 *  and
 *  then an increase of 2.
 */
function is_J_dependent(surface: number[]): boolean
{
    // TODO test
    let J_dependent = [];
    for (var col = 0; col < 9; col++) {
        if (col == WELL_COLUMN) continue;
        const diff = surface[col] - surface[col+1];
        if (col == 0) {
            // Left J dependency
            if (diff == -2) return true;
        }
        if (diff == 2) J_dependent.push(col);
    }
    for (var col of J_dependent) {
        const prev_col = col - 1;
        if (prev_col < 0) continue;
        const diff_next = surface[prev_col] - surface[prev_col+1]
        if (diff_next < -2) {
            return true;
        }
    }
    return false;
}

function surface_logic(a: EvalExplain, b: EvalExplain, board_a: string|null=null, board_b: string|null=null, short: boolean=false) : string
{
    if (board_b == null || board_a == null)
        return 'The surface is better';
    const surface_a = get_surface_array(board_a);
    const surface_b = get_surface_array(board_b);

    let cost_a = [];
    let cost_b = [];
    let better = [];
    let worse = [];
    let L_dependent = [];
    for (let col = 0; col < 9; col++) {
        if (col == WELL_COLUMN) continue;
        //# TODO: Double well code from rateSurface
        const diff_a = surface_a[col] - surface_a[col+1];
        const diff_b = surface_b[col] - surface_b[col+1];
        if (diff_b == 2) L_dependent.push(col);
        const cost_a_last = Math.abs(diff_a);
        const cost_b_last = Math.abs(diff_b);
        cost_a.push(cost_a_last);
        cost_b.push(cost_b_last);
        if (cost_a_last < cost_b_last) {
            better.push(col);
        } else if (cost_a_last > cost_b_last) {
            worse.push(col);
        }
    }
    console.log('cost_a ' + cost_a);
    console.log('cost_b ' + cost_b);
    if (cost_b.indexOf(0) == -1) {
        //# There is nowhere to place an O piece (see board11).
        if (cost_a.indexOf(0) != -1) {
            return "Better parity";
        }
    }
    if (Math.max(...cost_b) > Math.max(...cost_a) + 4) {
        //# TODO: Test
        return 'This avoids a spire';
    }
    let L_dependency_actual = [];
    if (L_dependent.length) {
        //#print('L', L_dependent)
        for (var col of L_dependent) {
            const next_col = col + 1;
            if (next_col >= 9) continue;
            const diff_next = surface_b[next_col] - surface_b[next_col+1];
            if (diff_next < -2) {
                L_dependency_actual.push(col);
            }
        }
        if (L_dependency_actual.length) {
            //print('L verified', L_dependency_actual)
            if (!is_L_dependent(surface_a)) {
                //# TODO: test and more nuance (in case the L dependency is not the highest priority).
                return 'This avoids an L dependency';
            }
        }
    }

    if (is_J_dependent(surface_b) && !is_J_dependent(surface_a)) {
        return 'This avoids a J dependency';
    }

    console.log(better);
    console.log(worse);

    let worse_str = '';
    if (better.length == 1) {
        if (worse.length) {
            const worse_cols = worse.join('');
            worse_str = `but Col ${worse_cols} ${is_are(worse)} worse`;
        }
        return `Col ${better.join('')} ${is_are(better)} better ${worse_str}`;
    }
    //# Multiple columns are better.
    if (better.length > 4) {
        return `The stack is much better ${better.join('')}`;
    }
    //# 2-3 columns are better.
    if (worse.length) {
        worse_str = `but Col ${worse.join('')} ${is_are(worse)} worse`;
    }
    if (better.length >= 2) {
        //# Improved parity by putting 2 minos together. (see board12 and board13, 14 and 15)
        let dbetter: number[] = [];
        for (let i = 0; i < better.length - 1; i++) {
            dbetter.push(better[i+1] - better[i]);
        }
        if (dbetter.indexOf(1) != -1) {
            //# handle 16 and 17
            const first_one = dbetter.indexOf(1);
            //print('first one debug', first_one)
            const dcost = cost_b[better[first_one]] - cost_a[better[first_one]];
            if (dcost == 1) {
                return `Better parity in columns ${better[first_one]+1} and ${better[first_one]+2}`;
            }
            return `Better shape in columns ${better[first_one]+1} and ${better[first_one]+2}`;
        } else {
            return `Better parity in columns ${better[0]+1} and ${better[0]+2}`;
        }
    }
    return `Col ${better.join('')} ${is_are(better)} better ${worse_str}`;
}

/*
 * Returns a string that explains the evaluation made by StackRabbit.
 */
function compareExplain(a: EvalExplain, b: EvalExplain, board_a: string|null=null, board_b: string|null=null, short: boolean=false) : string
{
    const diff_val: number[] = KEYS.map((key) => a[key] - b[key]);
    const most_important = Math.max(...diff_val);
    let res = '';
    let res2 = '';
    if (most_important < 0) {
        // It's for sure worse
        res = 'StackRabbit 2 playout is better';
    }
    for (var i = 0; i < diff_val.length; i++)
    {
        const val = diff_val[i];
        if (Math.abs(val) < SMALL) continue;
        if(val < 0)
        {
            res += `${KEY_EXPLAIN[i]} is worse ${val.toFixed(3)}, `;
        }
        else
        {
            if (val == most_important) {
                res += `${KEY_EXPLAIN[i]} is the most important ${val.toFixed(3)}, `
                if (KEYS[i] == 'surface') {
                    res2 = surface_logic(a, b, board_a, board_b);
                } else if (translations[KEYS[i]] !== undefined) {
                    res2 = translations[KEYS[i]];
                }
            } else {
                res += `${KEY_EXPLAIN[i]} is better ${val.toFixed(3)}, `
            }
        }
    }
    if (short && res2) return res2;
    if (res2) return res2 + '\n' + res.substring(0, res.length-2)
    //# strip the final comma space
    return res.substring(0, res.length-2);
}

// Show the user the reason why explain1 is better than explain2.
console.log(compareExplain(explain1, explain2, board1, board2));
// When you get it backwards, it tells you why explain2 is worse than explain1.
console.log(compareExplain(explain2, explain1, board2, board1));
