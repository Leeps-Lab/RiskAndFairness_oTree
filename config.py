'''
Please use lowercase for dictionary keys in the future // Rachel

# default probability in Security mode is prob_a: 0, prob_b: 100

'''

data = [
    {'mode': 'probability', 'a_x': 70, 'a_y':10, 'b_x': 10, 'b_y': 80, 'label': {'x': 'lbl x','y': 'lbl y'}},
    {'mode': 'independent', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 50},
    {'mode': 'positive'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50},
    {'mode': 'negative'   , 'm': 100, 'p_x': 1, 'p_y': 3, 'prob_a': 50}
]

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