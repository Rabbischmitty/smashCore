"""
    Project: SmashCore
    Course: UMGC CMSC 495 (7383)
    Term: Spring 2025
    Date: 20250401
    Code Repository: https://github.com/jcooke-dev/smashCore
    Authors: Justin Cooke, Ann Rauscher, Camila Roxo, Justin Smith, Rex Vargas

    Module Description: This is the test harness for the Leaderbaord class.
"""
import pytest
from unittest import mock
from score import Score
from src import Leaderboard, PlayerState, UserInterface


@pytest.fixture
def leaderboard_partial():
    score_list: list[Score] = [Score(50, 1, "ddd"),
                               Score(100, 1, "ccc"),
                               Score(300, 1, "bbb"),
                               Score(500, 1, "aaa")
                               ]
    leaderboard = Leaderboard()
    leaderboard.l_top_scores = score_list
    return leaderboard

@pytest.fixture
def leaderboard_full():
    score_list: list[Score] = [
        Score(50, 1, "iii"),
        Score(100, 1, "ccc"),
        Score(120, 1, "hhh"),
        Score(150, 1, "aaa"),
        Score(250, 1, "fff"),
        Score(300, 1, "bbb"),
        Score(350, 1, "eee"),
        Score(500, 1, "aaa"),
        Score(550, 1, "ddd"),
        Score(560, 1, "ggg")
    ]
    leaderboard = Leaderboard()
    leaderboard.l_top_scores = score_list
    return leaderboard

def test_is_high_score(leaderboard_partial):
    assert leaderboard_partial.is_high_score(1000)


def test_is_high_score_without_full_list(leaderboard_partial):
    assert leaderboard_partial.is_high_score(30)

def test_is_high_score_without_full_list_same_low_score(leaderboard_partial):
    assert leaderboard_partial.is_high_score(50)

def test_is_not_high_score_with_full_list(leaderboard_full):
    assert leaderboard_full.is_high_score(30) is False


def test_is_not_high_score_with_full_list_same_min_score(leaderboard_full):
    assert leaderboard_full.is_high_score(50) is False


def test_is_high_score_with_full_list(leaderboard_full):
    assert leaderboard_full.is_high_score(400)


def test_add_score_to_parial_list(leaderboard_partial):
    ps = PlayerState()
    ps.score = 400
    ps.level = 2
    ps.lives = 0
    ui = mock.Mock()
    ui.tb_initials_text = "abc"
    leaderboard_partial.add_score(ps, ui)

    expected_list: list[Score] = [
                                  Score(50, 1, "ddd"),
                                  Score(100, 1, "ccc"),
                                  Score(300, 1, "bbb"),
                                  Score(400, 2, "abc"),
                                  Score(500, 1, "aaa")]
    assert leaderboard_partial.l_top_scores == expected_list


def test_add_score_to_full_list(leaderboard_full):
    ps = PlayerState()
    ps.score = 400
    ps.level = 2
    ps.lives = 0
    ui = mock.Mock()
    ui.tb_initials_text = "xyz"
    leaderboard_full.add_score(ps, ui)
    expected_list: list[Score] = [
        Score(100, 1, "ccc"),
        Score(120, 1, "hhh"),
        Score(150, 1, "aaa"),
        Score(250, 1, "fff"),
        Score(300, 1, "bbb"),
        Score(350, 1, "eee"),
        Score(400, 2, "xyz"),
        Score(500, 1, "aaa"),
        Score(550, 1, "ddd"),
        Score(560, 1, "ggg")
    ]
    assert leaderboard_full.l_top_scores == expected_list

