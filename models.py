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
            'a_x': 30,        # x value of point A
            'a_y': 80,         # y value of point A
            'b_x': 65,        # x value of point B
            'b_y': 45         # y value of point B
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
        current_round = self.round_number
        # check if current round is the preset payoff round
        if current_round == self.session.vars['paying_round']:
            # pull dictionary of values for current round from config.py
            dynamic_values = config.getDynamicValues()
            round_data = dynamic_values[current_round - 1]

            # generate pseudo_random number to compare to probabilities
            # 0 <= rnd <= 1
            rnd = random.random()

            for p in self.get_players():
                # probability mode: if rnd < player x's (the Decider's) chosen prob. of state A, they get the preset
                # state A_x payoff, otherwise they get paid preset state b_x payoff. If rnd < player y's prob for state A
                # (also chosen by player x), player y gets the preset state a_y payoff, else the preset state b_y payoff.
                if round_data['mode'] == 'probability':
                    if p.role() == 'Decider':
                        p.payoff = (rnd < p.prob_a/100)*round_data['a_x'] + (rnd >= p.prob_a/100)*round_data['b_x']
                    elif p.role() == 'Partner':
                        p.payoff = (rnd < p.prob_a / 100) * round_data['a_y'] + (rnd >= p.prob_a / 100) * round_data['b_y']
                # single mode: each player only sees a square, so they each get the value of their square
                elif round_data['mode'] == 'single':
                    p.payoff = (rnd < round_data['prob_a']) * p.square_x + (rnd >= round_data['prob_a']) * p.square_y
                # for all other modes: if rnd < probability of state A (meaning state A was chosen), player x gets
                # the square's x coordinate, and player y gets the circle's x coordinate. If state B was chosen, player
                # x gets the squares y coordinate and player y gets the circles y coordinate.
                elif round_data['mode'] in ['positive', 'negative', 'independent']:
                    if p.role() == 'Decider':
                        p.payoff = (rnd < round_data['prob_a']) * p.square_x + (rnd >= round_data['prob_a']) * p.square_y
                elif p.role() == 'Partner':
                    p.payoff = (rnd < round_data['prob_a']) * p.circle_x + (rnd >= round_data['prob_a']) * p.circle_y

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            # set a random round to be the payoff round
            self.session.vars['paying_round'] = random.randint(1, Constants.num_rounds)
        else:
            self.group_like_round(1)


# yes | otree resetdb && otree runserver
