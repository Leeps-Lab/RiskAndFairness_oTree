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
            elif round_data['mode'] == 'single':
                return ['mode', 'me_a', 'me_b', 'prob_a', 'prob_b']
            else:
                return ['mode', 'partner_a', 'partner_b', 'me_a', 'me_b', 'prob_a', 'prob_b']
        else:
            return ['mode', 'partner_a', 'partner_b', 'me_a', 'me_b', 'prob_a', 'prob_b']

    def vars_for_template(self):
        current_round = self.round_number
        dynamic_values = config.getDynamicValues()
        round_data = dynamic_values[current_round - 1]
        return {'mode': round_data['mode']}

    def before_next_page(self):
        current_round = self.round_number
        dynamic_values = config.getDynamicValues()
        round_data = dynamic_values[current_round - 1]
        if round_data['mode'] == 'single':
            self.group.set_payoffs()
        elif self.player.id_in_group == 1:
            self.group.set_payoffs()

class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        pass

class Results(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):
        # variables:
        mode = Constants.dynamic_values[self.session.vars['paying_round'] - 1]['mode']
        decision = self.group.get_player_by_id(1).me_a if mode != 'probability' else self.group.get_player_by_id(1).prob_a
        decision = str(round(decision, 1)) + '% for A'
        return {'mode': mode.capitalize(), 'decision': decision}


page_sequence = [
    InitialInstructions,
    #TaskInstructions,
    Graph,
    ResultsWaitPage,
    Results
]


# yes | otree resetdb && otree runserver
