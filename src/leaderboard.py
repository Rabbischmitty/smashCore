"""
    Project: SmashCore
    Course: UMGC CMSC 495 (7383)
    Term: Spring 2025
    Date: 20250401
    Code Repository: https://github.com/jcooke-dev/smashCore
    Authors: Justin Cooke, Ann Rauscher, Camila Roxo, Justin Smith, Rex Vargas

    Module Description: Handles the leaderboard scores and naming
"""

import constants
import persistence
from score import Score


class Leaderboard:
    """ This maintains the set of leaderboard game scores """

    def __init__(self):
        self.l_top_scores: list[Score] = []

    @classmethod
    def create_persisted_object(cls):
        """
        Creates a leaderboard file if none exist
        :return:
        """
        lb = cls.load(persistence.LEADERBOARD_FILENAME)
        if lb is None:
            lb = Leaderboard()
        return lb

    @classmethod
    def load(cls, filename: str):
        """
        Loads leaderboard file
        :param filename:
        :return:
        """
        return persistence.read_object(filename)

    def store(self, filename: str):
        """
        Stores leaderboard file
        :param filename:
        :return:
        """
        persistence.store_object(self, filename)

    def is_high_score(self, score: int) -> bool:
        """
        Tests if score is within the top high scores
        :param score:
        :return:
        """
        return (score > min(scr.score for scr in self.l_top_scores)) if len(self.l_top_scores) >= constants.LEADERBOARD_SIZE else True

    def add_score(self, ps, ui):
        """
        Called after it is determined player has achieved a high score.
        Adds player's high score to the leaderboard
        If leaderboard is full, bumps a player off and resorts.
        :param ps: PlayerState
        :param ui: UserInterface
        :return:
        """
        score = Score(ps.score, ps.level, ui.tb_initials_text)

        if len(self.l_top_scores) < constants.LEADERBOARD_SIZE:
            self.l_top_scores.append(score)
        else:
            # full, so remove lowest score
            self.l_top_scores[0] = score

        # reset the ui var holding the entered initials
        ui.tb_initials_text = ""

        # ensure in proper order
        self.l_top_scores.sort()
