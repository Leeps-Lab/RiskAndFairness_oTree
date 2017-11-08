from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from . import config

"""
Principal maintainer: Rachel Chen <me@rachelchen.me>
Contributors:
    Kristian Lopez Vargas <kristianlvargas@gmail.com>
    Eli Pandolfo
"""

class InitialInstructions(Page):
    form_model = models.Player
    form_fields = ['time_InitialInstructions']

    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        numberOfPeriod = config.numberOfPeriod()
        return {'participation_fee': self.session.config['participation_fee']}


class TaskInstructions(Page):
    form_model = models.Player
    form_fields = ['time_TaskInstructions']

    def is_displayed(self):
        # print('GROUP PAYING ROUND', self.group.paying_round)
        # print('GROUP PAYING DICT', self.group.pr_dict)
        #print('PLAYER', self.player.id_in_group, 'PAYING ROUND', self.player.dynamic_values.index(self.group.pr_dict) + 1)
        # print('PLAYER', self.player.id_in_group, 'DYNAMIC VALUES', self.player.dynamic_values)
        mode = self.player.participant.vars['dynamic_values'][self.round_number - 1]['mode']
        if self.round_number > 1:
            prevmode = self.player.participant.vars['dynamic_values'][self.round_number - 2]['mode']
        return self.round_number == 1 or mode != prevmode

    def vars_for_template(self):
        mode = self.player.participant.vars['dynamic_values'][self.round_number - 1]['mode']
        # this will be used in the conditional display of instructions
        return {'mode': mode,
                'sec0': '' if mode in ['probability', 'det_giv'] else mode.split('_')[0],
                'sec1': '' if mode in ['probability', 'det_giv'] else mode.split('_')[1],
                'sec2': '' if mode in ['probability', 'det_giv', 'sec_ownrisk'] else mode.split('_')[2]
                }

class Graph(Page):
    form_model = models.Player

    def get_form_fields(self):
        dynamic_values = self.player.participant.vars['dynamic_values']
        round_data = dynamic_values[self.round_number - 1]
        if round_data is not None and round_data['mode'] is not None:
            if round_data['mode'] == 'det_giv':
                return ['mode', 'me_a', 'me_b', 'time_Graph']
            elif round_data['mode'] == 'probability':
                return ['mode', 'prob_a', 'prob_b', 'time_Graph']
            elif round_data['mode'] == 'sec_ownrisk':
                return ['mode', 'me_a', 'me_b', 'prob_a', 'prob_b', 'time_Graph']
            else:
                return ['mode', 'partner_a', 'partner_b', 'me_a', 'me_b', 'prob_a', 'prob_b', 'time_Graph']
        else:
            return ['mode', 'partner_a', 'partner_b', 'me_a', 'me_b', 'prob_a', 'prob_b', 'time_Graph']

    def vars_for_template(self):
        dynamic_values = self.player.participant.vars['dynamic_values']
        mode = self.player.participant.vars['dynamic_values'][self.round_number - 1]['mode']
        print('MODE MODE MODE', mode)
        if self.round_number > 1:
            counter = 1
            prevmode = self.player.participant.vars['dynamic_values'][self.round_number - 2]['mode']
            while mode == prevmode:
                counter += 1;
                if counter == self.round_number:
                    break
                prevmode = self.player.participant.vars['dynamic_values'][self.round_number - (counter + 1)]['mode']
        else:
            counter = 1
        return {'dynamic_values': dynamic_values,
                'mode': mode,
                'counter': counter,
                'sec1': '' if mode in ['probability', 'det_giv'] else mode.split('_')[1],
                'sec2': '' if mode in ['probability', 'det_giv', 'sec_ownrisk'] else mode.split('_')[2]
                }

    def before_next_page(self):
        if self.group.get_player_by_id(1).participant.vars['pr_dict']['mode'] == 'sec_ownrisk' and self.round_number == self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1:
            self.player.set_payoffs()
        elif self.player.id_in_group == 1 and self.round_number == self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1:
            self.group.set_payoffs()

class ResultsWaitPage(WaitPage):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def after_all_players_arrive(self):
        pass

class Results(Page):

    form_model = models.Player
    form_fields = ['time_Results']

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        modeMap = {
        'probability': 'PR',
        'sec_1bl_1ch': 'S-1B-1C',
        'sec_1bl_2ch': 'S-1B-2C',
        'sec_2bl_1ch': 'S-2B-1C',
        'sec_ownrisk': 'S-OwnRisk',
        'det_giv': 'DG',
        'sec_ownrisk_fixedother': 'S-OwnRisk-FixedOther',
        'sec_otherrisk_ownfixed': 'S-OtherRisk-OwnFixed'}

        # variables:
        mode = self.group.get_player_by_id(1).participant.vars['pr_dict']['mode']

        decider = self.group.get_player_by_id(1)
        nondecider = self.group.get_player_by_id(2)

        pr = decider.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1
        pr2 = nondecider.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1

        if mode == 'probability':
            dec_a = round(decider.in_round(pr).prob_a, 1)
            dec_b = round(decider.in_round(pr).prob_b, 1)
        elif mode == 'det_giv':
            if self.player.id_in_group == 1:
                dec_a = round(decider.in_round(pr).me_a, 1) 
                dec_b = None
            else:
                dec_a = round(decider.in_round(pr).me_b, 1)
                dec_b = None
        else:
            if self.player.id_in_group == 1:
                dec_a = round(decider.in_round(pr).me_a, 1)
                dec_b = round(decider.in_round(pr).me_b, 1)
            elif mode != 'sec_ownrisk':
                dec_a = round(decider.in_round(pr).partner_a, 1)
                dec_b = round(decider.in_round(pr).partner_b, 1)
            # single mode
            else:
                dec_a = round(nondecider.in_round(pr2).me_a, 1)
                dec_b = round(nondecider.in_round(pr2).me_b, 1)

        outcome = self.player.in_round(self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1).outcome
        #payoff = self.player.in_round(Constants.num_rounds).payoff

        payoff = self.player.in_round(self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1).payoff
        
        role = self.player.role()

        if self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) > 0:
            counter = 1
            prevmode = self.player.participant.vars['dynamic_values'][self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) - 1]['mode']
            while mode == prevmode:
                counter += 1;
                if counter == self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) + 1:
                    break
                prevmode = self.player.participant.vars['dynamic_values'][self.player.participant.vars['dynamic_values'].index(self.group.get_player_by_id(1).participant.vars['pr_dict']) - counter]['mode']
        else:
            counter = 1
        return {'mode': modeMap[mode], 'dec_a': dec_a, 'dec_b': dec_b, 'role': role, 'counter': counter, 'outcome': outcome, 'payoff': payoff}


page_sequence = [
    InitialInstructions,
    TaskInstructions,
    Graph,
    ResultsWaitPage,
    Results
]


# yes | otree resetdb && otree runserver
