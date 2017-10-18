from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from . import config
from . import models

"""
Principal maintainer: Rachel Chen <me@rachelchen.me>
Contributors:
    Kristian Lopez Vargas <kristianlvargas@gmail.com>
    Eli Pandolfo
"""

class InitialInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class TaskInstructions(Page):
    def is_displayed(self):
        return self.round_number == 1


class Graph(Page):

    form_model = models.Player

    def get_form_fields(self):
        current_round = self.round_number
        dynamic_values = config.getDynamicValues()
        round_data = dynamic_values[current_round - 1]
        if round_data is not None and round_data['mode'] is not None:
            if round_data['mode'] == 'probability':
                return ['mode', 'prob_a', 'prob_b']
            else:
                return ['mode', 'other_a', 'other_b', 'me_a', 'me_b', 'prob_a', 'prob_b']
        else:
            return ['mode', 'other_a', 'other_b', 'me_a', 'me_b', 'prob_a', 'prob_b']


class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        pass

class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds


page_sequence = [
    InitialInstructions,
    TaskInstructions,
    Graph,
    ResultsWaitPage,
    Results
]


# yes | otree resetdb && otree runserver
