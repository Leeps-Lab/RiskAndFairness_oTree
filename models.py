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
    num_rounds = config.numberOfPeriod()

    # I'm offloading the heavy lifting to JavaScript because I'm very bad at Python
    static_values = {
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
        'width': 600,            # width of the graph
        'height': 600,            # height of the graph
        'margin': {              # grapg margins
            'top': 20,
            'right': 20,
            'bottom': 50,
            'left': 50
        }
    }
    default_values = {
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
    dynamic_values = config.getDynamicValues()

class Subsession(BaseSubsession):

    def creating_session(self):

    	# this both breaks players into random groups,
    	# and assigns the two players in each group to random
    	# roles (d vs nd, decision maker vs non-decision maker)
    	self.group_randomly()


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    mode = models.CharField()
    circle_x = models.FloatField()
    circle_y = models.FloatField()
    square_x = models.FloatField()
    square_y = models.FloatField()
    prob_a = models.FloatField()
    prob_b = models.FloatField()

    def role(self):
        if self.id_in_group == 1:
            return 'decision_maker'
        else:
            return 'non-decision_maker'
