#import modules
import pygame
import math
import sys
from config import *
from button import Button
from freeplay import Freeplay
from mode import Mode
from level import Level
from settings import Settings


class MainMenu:
    def __init__(self, game, screen, display_surface, engine, settings):
        self.game = game
        self.screen = screen
        self.display_surface = display_surface
        self.engine = engine
        self.settings = settings

        folders = os.listdir(BUTTONS_FOLDER)
        for folder in folders:
            BUTTONS[folder] = (pygame.image.load(path.join(BUTTONS_FOLDER, folder, "primary.png")).convert_alpha(
            ), pygame.image.load(path.join(BUTTONS_FOLDER, folder, "secondary.png")).convert_alpha())

        self.buttons = []
        self.buttons.append(Button(760, 250, BUTTONS["Title"]))
        self.buttons.append(
            Button(885, 400, BUTTONS["Freeplay"], self.start_freeplay))
        self.buttons.append(Button(885, 550, BUTTONS["Levels"], self.start_level))
        self.buttons.append(Button(885, 700, BUTTONS["Settings_Main"], self.start_settings))

    def input_handler(self, event):
        return

    def standard(self):
        self.update()
        self.draw()

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons:
            button.update(mouse_pos)

    def draw(self):
        self.screen.fill(WHITE)
        for button in self.buttons:
            self.screen.blit(
                button.current_image, (button.rect.x, button.rect.y))
        pygame.display.flip()

    def start_freeplay(self):
        self.game.current_mode = Freeplay(
            self.game, self.engine, -1, self.screen, self.display_surface, self.settings)

    def start_level(self):
        self.game.current_mode = Level(self.game, self.engine, 1, self.screen, self.display_surface, self.settings)


    def start_settings(self):
        self.game.current_mode = self.settings