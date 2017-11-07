'''
Please use lowercase for dictionary keys in the future // Rachel

# default probability in Security mode is prob_a: 0, prob_b: 100

# positive -> sec_1bl_1ch;
# negative -> sec_2bl_1ch;
# independent -> sec_1bl_2ch;
# single -> sec_ownrisk

'''

import random

data = [
    [
    {'mode': 'det_giv', 'm': 95, 'p_x': 2.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    {'mode': 'det_giv', 'm': 95, 'p_x': 2.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}}
    ],
    [
    {'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    {'mode': 'sec_1bl_1ch'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}}
    ],
    [
    {'mode': 'sec_2bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    {'mode': 'sec_2bl_1ch'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}}
    ],
    [
    {'mode': 'sec_ownrisk'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    {'mode': 'sec_ownrisk'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}}
    ],
    [
    {'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'fixed': {'m': 50, 'p_x': 1, 'p_y': 2, 'a': 10}},
    {'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'fixed': {'m': 50, 'p_x': 1, 'p_y': 2, 'a': 10}}
    ],
    [
    {'mode': 'probability', 'a_x': 70, 'a_y': 10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}}
    ]
]

def shuffle(data):
    shuffled_data = []
    # shuffle each dict within each block
    for block in data:
        shuffled_data.append(random.sample(block, k=len(block)))

    # shuffle each block
    random.shuffle(shuffled_data)
    return shuffled_data


def flatten(shuffled_data):
    return [period for block in shuffled_data for period in block]

def checkValidity(flattened_data):
    for period in flattened_data:
        if 'prob_a' in period:
            if period['prob_a'] < 0 or period['prob_a'] > 100:
                print('ERROR: invalid prob_a in round', flattened_data.index(period), ': prob_a is: ',
                    period['prob_a'], ' but must be a number between 0 and 100')
                return 0
    return 1

def numberOfPeriod():
    return len(flatten(data))

def getDynamicValues():
    dynamic_values = data
    if checkValidity(flatten(dynamic_values)) == 0:
        return 0
    return dynamic_values


# Syntax for data dictionaries

# {'mode': 'det_giv', 'm': 50, 'p_x': 0.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
# {'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_2bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_ownrisk'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_ownrisk_fixedother'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
# {'mode': 'sec_otherrisk_ownfixed'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
# {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
