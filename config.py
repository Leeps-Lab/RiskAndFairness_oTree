data = [
    {'Mode': 'probability'},
    {'Mode': 'independent', 'Income': 100, 'Px': 2, 'Py': 1},
    {'Mode': 'positive'   , 'Income': 100, 'Px': 1, 'Py': 3}
]


def numberOfPeriod():
	return len(data)

def getDynamicValues():
    return data
