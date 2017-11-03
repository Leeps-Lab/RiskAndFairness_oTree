'''
Please use lowercase for dictionary keys in the future // Rachel

# default probability in Security mode is prob_a: 0, prob_b: 100

# positive -> sec_1bl_1ch;
# negative -> sec_2bl_1ch;
# independent -> sec_1bl_2ch;
# single -> sec_ownrisk

'''

data = [
{'mode': 'det_giv', 'm': 50, 'p_x': 1.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 1.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 2.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 2.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 2.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},

{'mode': 'det_giv', 'm': 50, 'p_x': 0.50, 'p_y': 1, 'prob_a': 50,'label': {'x': 'Your Tokens','y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 0.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},
{'mode': 'det_giv', 'm': 50, 'p_x': 1.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}},

{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},

{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},


{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 2.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},

{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 0.75, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.00, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.25, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},
{'mode': 'sec_1bl_1ch'   , 'm': 50, 'p_x': 1.50, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},


    {'mode': 'sec_ownrisk'   , 'm': 50, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},


    {'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'fixed': {'m': 50, 'p_x': 1, 'p_y': 2, 'a': 10}},

    {'mode': 'sec_otherrisk_ownfixed', 'm': 50, 'p_x': 1, 'p_y': 2, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},

    {'mode': 'probability', 'a_x': 70, 'a_y': 10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'Your Tokens', 'y': 'Partner\'s Tokens'}}
    # {'mode': 'sec_1bl_2ch', 'm': 50, 'p_x': 2, 'p_y': 1, 'prob_a': 50, 'label': {'x': 'State A (50%)','y': 'State B (50%)'}},

]

# patch

print('temp')
def checkValidity():
    for period in data:
        if 'prob_a' in period:
            if period['prob_a'] < 0 or period['prob_a'] > 100:
                print('ERROR: invalid prob_a in round', data.index(period), ': prob_a is: ',
                    period['prob_a'], ' but must be a number between 0 and 100')
                return 0
    return 1

def numberOfPeriod():
    return len(data)

def getDynamicValues():
    if checkValidity() == 0:
        return 0
    return data


# COMMENT ON NEW TASKS
# Logically, m, p_x, and p_y are for your equation, and under "fixed" are for other's equation
{'mode': 'sec_ownrisk_fixedother', 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50, 'fixed': {'m': 50, 'p_x': 1, 'p_y': 2, 'a': 10}},

# Logically, m, p_x, and p_y are for other's equation, and under "fixed" are for your equation
{'mode': 'sec_otherrisk_ownfixed', 'm': 50, 'p_x': 1, 'p_y': 2, 'prob_a': 50, 'fixed': {'m': 100, 'p_x': 2, 'p_y': 3, 'a': 30}},


# old config data
# data = [
#     {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
#     {'mode': 'independent', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 50},
#     {'mode': 'positive'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
#     {'mode': 'negative'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
#     {'mode': 'single'   , 'm': 100, 'p_x': 2, 'p_y': 3, 'prob_a': 50}
# ]


