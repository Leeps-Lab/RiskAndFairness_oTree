data = [
    {'Mode': 'independent', 'Income': 100, 'Px': 2, 'Py': 1},
    {'Mode': 'positive'   , 'Income': 100, 'Px': 1, 'Py': 3},
    {'Mode': 'probability'}
]

# !!!!!!!!

'''
!!! DO NOT EDIT VALUES BELOW !!!
'''

# !!!!!!!!

# Static parameters
# Graph parameters
staticValues = {
    'precision': 2,           # number of decimcals
    'scale': {
        'type': 'fixed',    # axis scaling, could be "fixed" or "dynamic"
        'max': 100          # only used in "fixed"
    },
    # only used in probability mode
    'constants': {
        'k': 0.4,          # scaling factor, only used in 'probability' mode
        'maxArea': 100
    },
    'width': 500,            # width of the graph
    'height': 500,            # height of the graph
    'margin': {              # grapg margins
        'top': 20,
        'right': 20,
        'bottom': 50,
        'left': 50
    }
}

defaultValues = {
    'mode': 'negative',
    'label': {
        'x': 'x axis',
        'y': 'y axis'
    },
    # only used in non-probability mode
    'equation': {
        'm': 100,           # income
        'px': 1,            # price of X
        'py': 2,            # price of Y
        'a': {
            'x': 30,        # x value of point A
            'y': 80         # y value of point A
        },
        'b': {
            'x': 65,        # x value of point B
            'y': 45         # y value of point B
        }
    }
}


def numberOfPeriod():
	return len(data)

def getContants():
    return staticValues

def getDefaultValues():
    return defaultValues

def getDynamicValues():
    return data
