from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
from . import config
import random

"""
Principal maintainer: Rachel Chen <me@rachelchen.me>
Contributors:
    Kristian Lopez Vargas <kristianlvargas@gmail.com>
    Eli Pandolfo
"""


class Constants(BaseConstants):
    name_in_url = 'RiskAndFairness_oTree'
    players_per_group = 2
    num_rounds = config.numberOfPeriod()

    # I'm offloading the heavy lifting to JavaScript because I'm very bad at Python
    static_values = {
        'precision': 1,         # number of decimals
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
        'height': 600,           # height of the graph
        'margin': {              # graph margins
            'top': 20,
            'right': 20,
            'bottom': 50,
            'left': 50
        }
    }
    default_values = {
        'mode': 'negative',
        'label': {
            'x': 'State A',
            'y': 'State B'
        },
        # only used in security mode (aka non-probability mode)
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
            return 'Decider'
        else:
            return 'Partner'

class Group(BaseGroup):

    def set_payoffs(self):
        rnd = random()
        current_round = self.round_number
        dynamic_values = config.getDynamicValues()
        round_data = dynamic_values[current_round - 1]
        for p in self.get_players():
            if round_data['Mode'] == 'probability':
                if p.role() == 'Decider':
                    p.payoff = (rnd < p.prob_a/100)*round_data['a_x'] + (rnd >= p.prob_a/100)*round_data['b_x']
                if p.role() == 'Partner':
                    p.payoff = (rnd < p.prob_a / 100) * round_data['a_y'] + (rnd >= p.prob_a / 100) * round_data['b_y']
            if round_data['Mode'] != 'probability': # this needs to change later
                if p.role() == 'Decider':
                    p.payoff = (rnd < p.prob_a/100)*round_data['a_x'] + (rnd >= p.prob_a/100)*round_data['b_x']
                if p.role() == 'Partner':
                    p.payoff = (rnd < p.prob_a / 100) * round_data['a_y'] + (rnd >= p.prob_a / 100) * round_data['b_y']



class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
        else:
            self.group_like_round(1)


# yes | otree resetdb && otree runserver
