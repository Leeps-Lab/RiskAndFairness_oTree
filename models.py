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
    participation_fee = c(5)

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
        'mode': 'sec_2bl_1ch',
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
    
    # not flattened
    dynamic_values = config.getDynamicValues()
    pr_dict = None

    # number of different task types
    number_types_of_tasks = len(set([d['mode'] for d in config.flatten(dynamic_values)]))


    # INSTRUCTIONS PATHS
    # list instruction templates
    instructions_probability = 'RiskAndFairness_oTree/Probability.html'
    instructions_sec = 'RiskAndFairness_oTree/sec.html'
    instructions_det_giv = 'RiskAndFairness_oTree/det_giv.html'


class Player(BasePlayer):

    # each player has its own shuffled data, and its own paying round number (starting at 1)
    # (the paying round is the same for all players, but the index of that round is unique for each shuffled dataset)

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
    time_Results =  models.TextField(widget=widgets.HiddenInput(attrs={'id': 'arrive_time'}))


    def role(self):
        if self.id_in_group == 1:
            return 'Decider'
        else:
            return 'Non-Decider'
    
    def set_payoffs(self):
        round_data = self.participant.vars['dynamic_values'][self.round_number - 1]
        print('round data in set payoffs', round_data)

        rnd = random.random()
        print('random rnd', rnd)

        self.payoff = (rnd < round_data['prob_a'] / 100) * self.me_a + (rnd >= round_data['prob_a'] / 100) * self.me_b
        self.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
            
class Group(BaseGroup):


    def set_dv(self):
        self.get_player_by_id(1).participant.vars['paying_round'] = random.randint(1, Constants.num_rounds)
        print('GROUP PAYING ROUND', self.get_player_by_id(1).participant.vars['paying_round'])
        self.get_player_by_id(1).participant.vars['pr_dict'] = config.flatten(Constants.dynamic_values)[self.get_player_by_id(1).participant.vars['paying_round'] - 1]
        print('\nPR DICT', self.get_player_by_id(1).participant.vars['pr_dict'])
        self.get_player_by_id(1).participant.vars['dynamic_values'] = config.flatten(config.shuffle(Constants.dynamic_values))
        print('\nPLAYER 1 PAYING ROUND', self.get_player_by_id(1).participant.vars['dynamic_values'].index(self.get_player_by_id(1).participant.vars['pr_dict']) + 1)
        print('\nPLAYER 1 DV', self.get_player_by_id(1).participant.vars['dynamic_values'])
        self.get_player_by_id(2).participant.vars['dynamic_values'] = config.flatten(config.shuffle(Constants.dynamic_values))
        print('\nPLAYER 2 PAYING ROUND', self.get_player_by_id(2).participant.vars['dynamic_values'].index(self.get_player_by_id(1).participant.vars['pr_dict']) + 1)
        print('\nPLAYER 2 DV', self.get_player_by_id(2).participant.vars['dynamic_values'])

    def set_payoffs(self):

        modeMap = {
        'probability': 'probability',
        'sec_1bl_1ch': 'positive',
        'sec_2bl_1ch': 'negative',
        'sec_1bl_2ch': 'independent',
        'sec_ownrisk': 'single',
        'sec_ownrisk_fixedother': 'single_fixedcircle',
        'sec_otherrisk_ownfixed': 'single_fixedsquare',
        'det_giv': 'single_given'}
        
        # generate pseudo_random number to compare to probabilities  0 <= rnd <= 1
        # !!!!  this is now run every round so rnd cant be here. !!!!
        rnd = random.random()
        print('random rnd', rnd)

        pr = self.get_player_by_id(1).participant.vars['dynamic_values'].index(self.get_player_by_id(1).participant.vars['pr_dict']) + 1
        pr2 = self.get_player_by_id(2).participant.vars['dynamic_values'].index(self.get_player_by_id(1).participant.vars['pr_dict']) + 1

        decider = self.get_player_by_role('Decider').in_round(pr)
        nondecider = self.get_player_by_role('Non-Decider').in_round(pr2)

        # pull dictionary of values for current round from decider
        round_data = decider.participant.vars['dynamic_values'][self.round_number - 1]
        print('round data in set payoffs', round_data)

        if modeMap[round_data['mode']] == 'probability':
            decider.payoff = \
                (rnd < decider.prob_a / 100) * round_data['a_x'] + (rnd >= decider.prob_a / 100) * round_data['b_x']
            decider.outcome = 'A' if rnd < decider.prob_a / 100 else 'B'
            nondecider.payoff = \
                (rnd < decider.prob_a / 100) * round_data['a_y'] + (rnd >= decider.prob_a / 100) * round_data['b_y']
            nondecider.outcome = decider.outcome
        elif modeMap[round_data['mode']] in ['positive', 'negative', 'independent']:
            decider.payoff = \
                (rnd < round_data['prob_a'] / 100) * decider.me_a + (rnd >= round_data['prob_a'] / 100) * decider.me_b
            decider.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
            nondecider.payoff = \
                (rnd < round_data['prob_a'] / 100) * decider.partner_a + (rnd >= round_data['prob_a'] / 100) * decider.partner_b
            nondecider.outcome = decider.outcome
        elif modeMap[round_data['mode']] == 'single_fixedsquare':
            decider.payoff = \
                (rnd < round_data['prob_a'] / 100) * decider.me_a + (rnd >= round_data['prob_a'] / 100) * decider.me_b
            decider.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
            nondecider.payoff = \
                (rnd < round_data['prob_a'] / 100) * decider.partner_a + (rnd >= round_data['prob_a'] / 100) * decider.partner_b
            nondecider.outcome = decider.outcome
        elif modeMap[round_data['mode']] == 'single_fixedcircle':
            decider.payoff = \
                (rnd < round_data['prob_a'] / 100) * decider.me_a + (rnd >= round_data['prob_a'] / 100) * decider.me_b
            decider.outcome = 'A' if rnd < round_data['prob_a'] / 100 else 'B'
            nondecider.payoff = \
                (rnd < round_data['prob_a'] / 100) * decider.partner_a + (rnd >= round_data['prob_a'] / 100) * decider.partner_b
            nondecider.outcome = decider.outcome
        elif modeMap[round_data['mode']] == 'single_given':
            decider.payoff = decider.me_a
            nondecider.payoff = decider.me_b # this is really partner_a, but the javascript automatically exports this so its a hacky but easy and clean way to do it

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            self.group_randomly()
            for group in self.get_groups():
                group.set_dv()

        else:
            self.group_like_round(1)


# git add
# cd .. && yes | otree resetdb && otree runserver && cd RiskAndFairness_oTree
# yes | otree resetdb && otree runserver
# git add ______ && git commit -m "_______________" && git push
