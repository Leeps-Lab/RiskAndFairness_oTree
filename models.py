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
    static_values = config.getContants()
    default_values = config.getDefaultValues()
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

	def role(self):
		if self.id_in_group == 1:
			return 'decision_maker'
		else:
			return 'non-decision_maker'
