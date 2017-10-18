'''
Please use lowercase for dictionary keys in the future // Rachel
'''

data = [
    {'mode': 'probability', 'a_x': 80, 'a_y':0, 'b_x': 0, 'b_y': 80, 'label': {
        'x': 'Something 1',
        'y': 'Something 2'
    }}, # example usage for label
    {'mode': 'independent', 'm': 100, 'p_x': 2, 'p_y': 1, 'prob_a': 0.5},
    {'mode': 'positive'   , 'm': 100, 'p_x': 1, 'p_y': 3}
]


def numberOfPeriod():
    return len(data)

def getDynamicValues():
    return data
