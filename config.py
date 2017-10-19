'''
Please use lowercase for dictionary keys in the future // Rachel
'''

data = [
    {'mode': 'probability', 'a_x': 80, 'a_y':0, 'b_x': 0, 'b_y': 80, 'label': {
        'x': 'Something 1',
        'y': 'Something 2'
    }}, # example usage for label
   # {'mode': 'independent', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 50},
    # default probability in Security mode is prob_a: 0, prob_b: 100
    #{'mode': 'positive'   , 'm': 100, 'p_x': 1, 'p_y': 3}
]

def checkValidity():
    for period in data:
        if 'prob_a' in period:
            if period['prob_a'] < 0 or period['prob_a'] > 100:
                print('ERROR: invalid prob_a in round', data.index(period), ': prob_a is: ', \
                    period['prob_a'], ' but must be a number between 0 and 100')
                return 0
    return 1

def numberOfPeriod():
    return len(data)

def getDynamicValues():
    if checkValidity() == 0:
        return 0
    return data