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
    {'mode': 'det_giv', 'm': 50, 'p_x': 0.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    #{'mode': 'det_giv', 'm': 55, 'p_x': 0.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 60, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 65, 'p_x': 1.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 70, 'p_x': 1.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 75, 'p_x': 1.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 80, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 85, 'p_x': 2.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 90, 'p_x': 2.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
    # {'mode': 'det_giv', 'm': 95, 'p_x': 2.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}}
    ],
    [
    {'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    #{'mode': 'sec_1bl_1ch'   , 'm': 52, 'p_x': 0.80, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 54, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 56, 'p_x': 1.20, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 58, 'p_x': 1.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 60, 'p_x': 1.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 62, 'p_x': 1.80, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 64, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 66, 'p_x': 2.20, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_1ch'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}}
    ],
    [
    {'mode': 'sec_2bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    #{'mode': 'sec_2bl_1ch'   , 'm': 52, 'p_x': 0.80, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 54, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 56, 'p_x': 1.20, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 58, 'p_x': 1.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 60, 'p_x': 1.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 62, 'p_x': 1.80, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 64, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 66, 'p_x': 2.20, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_2bl_1ch'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}}
    ],
    [
    {'mode': 'sec_ownrisk'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    #{'mode': 'sec_ownrisk'   , 'm': 52, 'p_x': 0.80, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 54, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 56, 'p_x': 1.20, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 58, 'p_x': 1.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 1.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 62, 'p_x': 1.80, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 64, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 66, 'p_x': 2.20, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_ownrisk'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}}
    ],
    [
    {'mode': 'sec_ownrisk_fixedother'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 52, 'p_x': 0.80, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 54, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 56, 'p_x': 1.20, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 58, 'p_x': 1.40, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 60, 'p_x': 1.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 62, 'p_x': 1.80, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 64, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 66, 'p_x': 2.20, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}}
    ],
    [
    {'mode': 'sec_otherrisk_ownfixed'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 52, 'p_x': 0.80, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 54, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 56, 'p_x': 1.20, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 58, 'p_x': 1.40, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 60, 'p_x': 1.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 62, 'p_x': 1.80, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 64, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 66, 'p_x': 2.20, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
    # {'mode': 'sec_ownrisk_fixedother'   , 'm': 68, 'p_x': 2.40, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}}
    ],
    [
    {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
    ],
    [
    {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    # {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    ],
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






# COMMENT ON NEW TASKS
# Logically, m, p_x, and p_y are for your equation, and under "fixed" are for other's equation
# {'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'fixed': {'m': 50, 'p_x': 1, 'p_y': 2, 'a': 10}},

# Logically, m, p_x, and p_y are for other's equation, and under "fixed" are for your equation
# {'mode': 'sec_otherrisk_ownfixed', 'm': 50, 'p_x': 1, 'p_y': 2, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},


# old config data
# data = [
#     {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
#     {'mode': 'independent', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 50},
#     {'mode': 'positive'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
#     {'mode': 'negative'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
#     {'mode': 'single'   , 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50}
# ]


# syntax for other tasks
# {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# [   {'mode': 'sec_otherrisk_ownfixed', 'm': 50, 'p_x': 1, 'p_y': 2, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}} ],
