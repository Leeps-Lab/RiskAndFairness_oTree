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
        },
        'prob': {
            'a': 0,
            'b': 100
        }
    }
    dynamic_values = config.getDynamicValues()


class Player(BasePlayer):

    mode = models.CharField()
    partner_a = models.FloatField() # Circle is other
    partner_b = models.FloatField()
    me_a = models.FloatField() # Square is me
    me_b = models.FloatField()
    prob_a = models.FloatField()
    prob_b = models.FloatField()
    outcome = models.CharField()
    time_InitialInstructions = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_TaskInstructions =  models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_Graph =  models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    #time_ResultsWaitPage = models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))
    time_Results =  models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))

    def role(self):
        if self.id_in_group == 1:
            return 'Decider'
        else:
            return 'Partner'

class Group(BaseGroup):

    def set_payoffs(self):
        current_round = self.round_number
        print('current_round in set payoffs', current_round)

        # check if current round is the preset payoff round
        if current_round == self.session.vars['paying_round']:
            # pull dictionary of values for current round from config.py
            dynamic_values = config.getDynamicValues()
            round_data = dynamic_values[current_round - 1]

            print('round data in set payoffs', round_data)

            # generate pseudo_random number to compare to probabilities  0 <= rnd <= 1
            # !!!!  this is now run every round so rnd cant be here. !!!!
            rnd = random.random()
            print('random rnd', rnd)

            decider = self.get_player_by_role('Decider')
            partner = self.get_player_by_role('Partner')

            if round_data['mode'] == 'probability':
                decider.payoff = \
                    (rnd < decider.prob_a / 100) * round_data['a_x'] + (rnd >= decider.prob_a / 100) * round_data['b_x']
                decider.outcome = 'A' if rnd < decider.prob_a / 100 else 'B'
                partner.payoff = \
                    (rnd < decider.prob_a / 100) * round_data['a_y'] + (rnd >= decider.prob_a / 100) * round_data['b_y']
                partner.outcome = 'A' if rnd < decider.prob_a / 100 else 'B'
            elif round_data['mode'] == 'single':
                decider.payoff = \
                    (rnd < round_data['prob_a'] / 100) * decider.me_a + (rnd >= round_data['prob_a'] / 100) * decider.me_b
                decider.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
                partner.payoff = \
                    (rnd < round_data['prob_a'] / 100) * partner.partner_a + (rnd >= round_data['prob_a'] / 100) * partner.partner_b
                partner.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
            elif round_data['mode'] in ['positive', 'negative', 'independent']:
                decider.payoff = \
                    (rnd < round_data['prob_a'] / 100) * decider.me_a + (rnd >= round_data['prob_a'] / 100) * decider.me_b
                decider.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
                partner.payoff = \
                    (rnd < round_data['prob_a'] / 100) * decider.partner_a + (rnd >= round_data['prob_a'] / 100) * decider.partner_b
                partner.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            # set a random round to be the payoff round
            self.session.vars['paying_round'] = random.randint(1, Constants.num_rounds)
            print('------PAYING ROUND------', self.session.vars['paying_round'])
        else:
            self.group_like_round(1)


# git add
# cd .. && yes | otree resetdb && otree runserver && cd RiskAndFairness_oTree
# yes | otree resetdb && otree runserver
# git add ______ && git commit -m "_______________" && git push