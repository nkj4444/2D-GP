from pico2d import *
import pico2d
import game_framework
import numbers
import random
import main_state

M = main_state

class Enemy:
    x = 0
    y = 0
    p_x=6
    p_y=4

    hp = 10
    ep = 10
    damage = 2
    speed = 1
    ATTACK = 1
    SEARCH = 2

    move = False

    run_stack = [None for i in range(5)]




    state = SEARCH

    def enemy_ai(self):

        if self.state == self.SEARCH:
            if self.move == True and M.turn == 3:




    def __init__(self):
        self.image = load_image('gunner.png')

    def draw(self):
        self.image.draw(self.x, self.y)