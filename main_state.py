from pico2d import *
import pico2d
import game_framework
import title_state
import random


running = True



def enter():
    global boy, grass, selectedboy, team
    boy = Boy()
    grass = Grass()

    team = [Boy() for i in range(11)]
    selectedboy = team[1]

def exit():
    global boy, grass
    del(boy)
    del(grass)

class Boy:
   def __init__(self):
      self.x, self.y = random.randint(100, 700),90
      self.frame = random.randint(0, 7)
      self.image = load_image('run_animation.png')
   def update(self):
      self.frame = (self.frame + 1) % 8
      self.x += 5
      if (self.x >= 800):
        self.x = 0
   def draw(self):
      self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


class Grass:
   def __init__(self):
      self.image = load_image('grass.png')
   def draw(self):
      self.image.draw(400, 30)



def handle_events():
    global running
    global selectedboy
    global team
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(title_state)
        elif event.type == SDL_MOUSEMOTION:
            selectedboy.x = event.x
            selectedboy.y = 600 - event.y
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_9:
                selectedboy = team[9]
            elif event.key == SDLK_1:
                selectedboy = team[1]
            elif event.key == SDLK_2:
                selectedboy = team[2]
            elif event.key == SDLK_3:
                selectedboy = team[3]
            elif event.key == SDLK_3:
                selectedboy = team[3]
            elif event.key == SDLK_4:
                selectedboy = team[4]
            elif event.key == SDLK_5:
                selectedboy = team[5]
            elif event.key == SDLK_6:
                selectedboy = team[6]
            elif event.key == SDLK_7:
                selectedboy = team[7]
            elif event.key == SDLK_8:
                selectedboy = team[8]





def update():
    boy.update()



def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()



    delay(0.05)
