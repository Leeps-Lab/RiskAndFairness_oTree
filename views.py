from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from . import config
from . import models

"""
Principle maintainer: Rachel Chen <me@rachelchen.me>
Contributors:
    <add your name here>
"""

class Graph(Page):

    form_model = models.Player
    def get_form_fields(self):
        current_round = self.round_number
        dynamic_values = config.getDynamicValues()
        round_data = dynamic_values[current_round - 1]
        if round_data is not None and round_data['Mode'] is not None:
            if round_data['Mode'] == 'probability':
                return ['mode', 'prob_a', 'prob_b']
            else:
                return ['mode', 'circle_x', 'circle_y', 'square_x', 'square_y']
        else:
            return ['mode', 'circle_x', 'circle_y', 'square_x', 'square_y', 'prob_a', 'prob_b']


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Graph,
    ResultsWaitPage,
    Results
]
