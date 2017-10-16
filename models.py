from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config

author = 'Rachel Chen <me@rachelchen.me>'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'RiskAndFairness_oTree'
    players_per_group = 2
    num_rounds = config.numberOfPeriod();

    # Graph parameters
    mode = 'negative'    # valid options: 'single', 'independent', 'positive', 'negative', or 'probability'
    precision = 2           # number of decimcals
    scale = {
        'type': 'fixed',    # axis scaling, could be "fixed" or "dynamic"
        'max': 100          # only used in "fixed"
    }

    # labels
    label = {
        'x': 'x axis',
        'y': 'y axis'
    }

    # only used in probability mode
    constants = {
        'k': 0.4,          # scaling factor, only used in 'probability' mode
        'maxArea': 100
    }
    # only used in non-probability mode
    equation = {
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

    width = 500             # width of the graph
    height = 500            # height of the graph
    margin = {              # grapg margins
        'top': 20,
        'right': 20,
        'bottom': 50,
        'left': 50
    }


class Subsession(BaseSubsession):
    
    def creating_session(self):
    
    	# this both breaks players into random groups,
    	# and assigns the two players in each group to random 
    	# roles (d vs nd, decision maker vs non-decision maker)
    	self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):
	
	def role(self):
		if self.id_in_group == 1:
			return 'decision_maker'
		else:
			return 'non-decision_maker'

	x = models.FloatField()
	y = models.FloatField()
	#could do this in group also and have it be getplayer1 x and y and getplayer1 x2 and y2 if they choose both?
	

