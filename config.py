'''
Please use lowercase for dictionary keys in the future // Rachel

# default probability in Security mode is prob_a: 0, prob_b: 100

# positive -> sec_1bl_1ch;
# negative -> sec_2bl_1ch;
# independent -> sec_1bl_2ch;
# single -> sec_ownrisk

'''

import random
import copy
import pandas as pd

# if you want to turn off shuffling, change this to False
shuffle = True

# this will be a list, each element of which is the paying round for a group.
# With the default of 16 participants, there will be 8 groups, so chosen_rounds
# should never have more than 8 elements.
# If chosen rounds is empty, models.py will randomly assign the chosen round for each group.
# indexing starts at 1, not 0
chosen_rounds = [2]

data = [
    [
    #{'mode': 'det_giv', 'm': 20, 'p_x': .2},
    # {'mode': 'det_giv', 'm': 40, 'p_x': 1},
    # {'mode': 'det_giv', 'm': 40, 'p_x': .667},
    # {'mode': 'det_giv', 'm': 40, 'p_x': .5},
    # {'mode': 'det_giv', 'm': 40, 'p_x': .4},
    # {'mode': 'det_giv', 'm': 60, 'p_x': 1.5},
    # {'mode': 'det_giv', 'm': 60, 'p_x': 1},
    # {'mode': 'det_giv', 'm': 60, 'p_x': .75},
    # {'mode': 'det_giv', 'm': 60, 'p_x': .6},
    # {'mode': 'det_giv', 'm': 80, 'p_x': 2},
    # {'mode': 'det_giv', 'm': 80, 'p_x': 1.333},
    # {'mode': 'det_giv', 'm': 80, 'p_x': 1},
    # {'mode': 'det_giv', 'm': 100, 'p_x': 5},
    # {'mode': 'det_giv', 'm': 100, 'p_x': 2.5},
    # {'mode': 'det_giv', 'm': 100, 'p_x': 1.25}
    ],
    [
    #{'mode': 'sec_1bl_1ch', 'm': 20, 'p_x': .5},
    # {'mode': 'sec_1bl_1ch', 'm': 20, 'p_x': .333},
    # {'mode': 'sec_1bl_1ch', 'm': 20, 'p_x': .25},
    # {'mode': 'sec_1bl_1ch', 'm': 20, 'p_x': .2},
    # {'mode': 'sec_1bl_1ch', 'm': 40, 'p_x': 1},
    # {'mode': 'sec_1bl_1ch', 'm': 40, 'p_x': .667},
    # {'mode': 'sec_1bl_1ch', 'm': 40, 'p_x': .5},
    # {'mode': 'sec_1bl_1ch', 'm': 40, 'p_x': .4},
    # {'mode': 'sec_1bl_1ch', 'm': 60, 'p_x': 1.5},
    # {'mode': 'sec_1bl_1ch', 'm': 60, 'p_x': 1},
    # {'mode': 'sec_1bl_1ch', 'm': 60, 'p_x': .75},
    # {'mode': 'sec_1bl_1ch', 'm': 60, 'p_x': .6},
    ],
    [
    #{'mode': 'sec_2bl_1ch'   , 'm': 20, 'p_x': 0.5},
    # {'mode': 'sec_2bl_1ch'   , 'm': 20, 'p_x': .333},
    # {'mode': 'sec_2bl_1ch'   , 'm': 20, 'p_x': 0.25},
    # {'mode': 'sec_2bl_1ch'   , 'm': 20, 'p_x': 0.2},
    # {'mode': 'sec_2bl_1ch'   , 'm': 40, 'p_x': 1},
    # {'mode': 'sec_2bl_1ch'   , 'm': 40, 'p_x': .667},
    # {'mode': 'sec_2bl_1ch'   , 'm': 40, 'p_x': 0.5},
    # {'mode': 'sec_2bl_1ch'   , 'm': 40, 'p_x': 0.4},
    # {'mode': 'sec_2bl_1ch'   , 'm': 60, 'p_x': 1.5},
    # {'mode': 'sec_2bl_1ch'   , 'm': 60, 'p_x': 1},
    # {'mode': 'sec_2bl_1ch'   , 'm': 60, 'p_x': .75},
    # {'mode': 'sec_2bl_1ch'   , 'm': 60, 'p_x': 0.6},
    ],
    [
    {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': 0.5},
    # {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': .333},
    # {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': 0.25},
    # {'mode': 'sec_ownrisk'   , 'm': 20, 'p_x': 0.2},
    # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': 1},
    # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': .667},
    # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': 0.5},
    # {'mode': 'sec_ownrisk'   , 'm': 40, 'p_x': 0.4},
    # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 1.5},
    # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 1},
    # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': .75},
    # {'mode': 'sec_ownrisk'   , 'm': 60, 'p_x': 0.6},
    ],
    [
    {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': 1,       'a': 5, 'b': 5},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .667,    'a': 5, 'b': 5},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .5,      'a': 5, 'b': 5},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .4,      'a': 5, 'b': 5},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': 1,       'a': 23, 'b': 23},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .667,    'a': 23, 'b': 23},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .5,      'a': 23, 'b': 23},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .4,      'a': 23, 'b': 23},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': 1,       'a': 60, 'b': 60},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .667,    'a': 60, 'b': 60},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .5,      'a': 60, 'b': 60},
    # {'mode': 'sec_ownrisk_fixedother', 'm': 40, 'p_x': .4,      'a': 60, 'b': 60},
    ],
    [
    {'mode': 'probability', 'a_x': 90, 'a_y': 10, 'b_x': 10, 'b_y': 90},
    # {'mode': 'probability', 'a_x': 90, 'a_y': 10, 'b_x': 10, 'b_y': 45},
    # {'mode': 'probability', 'a_x': 45, 'a_y': 10, 'b_x': 10, 'b_y': 90},
    # {'mode': 'probability', 'a_x': 70, 'a_y': 10, 'b_x': 40, 'b_y': 40},
    # {'mode': 'probability', 'a_x': 10, 'a_y': 70, 'b_x': 40, 'b_y': 40},
    ]
]

def shuffle(data):
    if shuffle == False:
        return data

    shuffled_data = []
    # shuffle each dict within each block
    for block in data:
        shuffled_data.append(random.sample(block, k=len(block)))

    # shuffle each block
    random.shuffle(shuffled_data)
    return shuffled_data


def flatten(shuffled_data):
    return [period for block in shuffled_data for period in block]

# converts config data into a pandas dataframe, for exporting to the visualization fcn
def export_data(data, session_name):
    cols = ['mode', 'm', 'p_x', 'a', 'b', 'a_x', 'a_y', 'b_x', 'b_y']
    df = pd.DataFrame(columns=cols)
    for period in flatten(data):
        for key in period:
            # convert all dict values to lists to allow creation of dataframe
            period[key] = [period[key]]
        df1 = pd.DataFrame(period)
        df = df.append(df1)

    df.to_csv('visualization/data/config_' + session_name + '.csv')



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


# CHECK WHAT HE WANTS FOR PROBABILITY AND FIXED FOR ALT OWNRISKS
def fill_defaults(data):
    newdata = copy.deepcopy(data)
    for block in newdata:
        for dic in block:
            if dic['mode'] in ['sec_1bl_1ch', 'sec_2bl_1ch', 'sec_1bl_2ch', 'sec_ownrisk']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'label' not in dic:
                    dic['label'] = {'x': 'State A (50%)', 'y': 'State B (50%)'}
            elif dic['mode'] in ['sec_ownrisk_fixedother', 'sec_otherrisk_ownfixed']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'fixed' not in dic and 'a' in dic and 'b' in dic: #check if this is what he wants here
                    dic['fixed'] = {'m': dic['a'] + dic['b'], 'p_x': 1, 'p_y': 1, 'a': dic['a']}
                if 'label' not in dic:
                    dic['label'] = {'x': 'State A (50%)', 'y': 'State B (50%)'}
            elif dic['mode'] == 'probability':
                if 'label' not in dic:
                    dic['label'] = {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}
            elif dic['mode'] in ['det_giv']:
                if 'p_y' not in dic:
                    dic['p_y'] = 1
                if 'prob_a' not in dic:
                    dic['prob_a'] = 50
                if 'label' not in dic:
                    dic['label'] = {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}
    return newdata

def getDynamicValues():
    dynamic_values = fill_defaults(data)
    if checkValidity(flatten(dynamic_values)) == 0:
        return 0
    return dynamic_values

def getChosenRounds():
    if len(chosen_rounds) == 0:
        return None
    else:
        return chosen_rounds


# Syntax for data dictionaries
# {'mode': 'det_giv', 'm': 50, 'p_x': 0.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
# {'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_2bl_1ch'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_ownrisk'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
# {'mode': 'sec_ownrisk_fixedother'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
# {'mode': 'sec_otherrisk_ownfixed'   , 'm': 50, 'p_x': 0.60, 'p_y': 1, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},
# {'mode': 'probability', 'a_x': 70, 'a_y': 10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}}
