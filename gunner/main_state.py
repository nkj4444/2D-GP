from pico2d import *
import pico2d
import game_framework

open_canvas()
running = True

move = False
x = 200
y = 150

turn = 1

events = get_events()

def handle_events():
    global running
    global x
    global y
    global move

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_KP_ENTER:
            turn_change()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            turn_change()
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x > 200:
                move = True








def turn_change():
    global turn
    global move

    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1


class Gunner:
   global x
   global y
   def __init__(self):
       self.image = load_image('gunner.png')

   def draw(self):
       self.image.draw(x, y)

gunner = Gunner()

rect = draw_rectangle(200,200,200,200)

while running == True:

    if x > 500:
        x = 200


    if turn == 2 and move == True:
        x = x + 100
        move = False


    handle_events()

    gunner.draw()
    update_canvas()
    clear_canvas()

close_canvas()