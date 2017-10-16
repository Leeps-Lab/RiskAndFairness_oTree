from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants
from . import config
from . import models

class Graph(Page):

    form_model = models.Player

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
