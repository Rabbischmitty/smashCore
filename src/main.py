"""
    Project: SmashCore
    Course: UMGC CMSC 495 (7383)
    Term: Spring 2025
    Date: 20250401
    Code Repository: https://github.com/jcooke-dev/smashCore
    Authors: Justin Cooke, Ann Rauscher, Camila Roxo, Justin Smith, Rex Vargas

    Module Description: This is the entry point for SmashCore, a breakout style game.
"""

import pygame

import assets
from gamesettings import GameSettings
from leaderboard import Leaderboard
from gamestate import GameState
from playerstate import PlayerState
from userinterface import UserInterface
from gameworld import GameWorld
from gameengine import GameEngine

def main() -> None:
    """
    Initializes pygame, loads the assets, initializes all dependencies, and loads/creates the leaderboard
    :return:
    """
    # mixer configuration settings
    pygame.mixer.pre_init(44100, -16, 2, 128)
    pygame.init()

    # setup various game objects
    assets.load_assets()
    ui = UserInterface()
    gset = GameSettings.create_persisted_object()
    gs = GameState()
    gw = GameWorld()
    ps = PlayerState()
    lb = Leaderboard.create_persisted_object()

    ge = GameEngine(lb, ps, gw, gs, gset, ui)

    # run the main game loop -- this returns when done
    ge.run_loop()

if __name__ == "__main__":
    main()
