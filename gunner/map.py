from pico2d import *
import pico2d
import game_framework



def make(w,h):

    maprect = [[to_sdl_rect() for col in range(w)] for row in range(h)]

    for i in range(w):
        maprect[0][i] = to_sdl_rect(i * 100, 0, 100, 100)
    for i in range(h):
        maprect[i][0] = to_sdl_rect(0, i * 100, 100, 100)


#matrix = [[0 for col in range(Width)] for row in range(Height)] 이차원배열생성
