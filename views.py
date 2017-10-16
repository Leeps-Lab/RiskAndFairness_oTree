from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from . import config
from . import models

class Graph(Page):

    form_model = models.Player
    
'''
class Probability(Page):
	def is_displayed(self):
		if config.data[self.round_number-1]['Mode'] == 'Probability':
			print("PROBABILITY (************)")
			return True
		else:
			return False



class Positive(Page):
	def is_displayed(self):
		if config.data[self.round_number-1]['Mode'] == 'Positive':
			print("POSITIVE (************)")
			return True
		else:
			return False

class Independent(Page):
	def is_displayed(self):
		if config.data[self.round_number-1]['Mode'] == 'Independent':
			print("INDEPENT (************)")
			return True
		else:
			return False
'''


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
