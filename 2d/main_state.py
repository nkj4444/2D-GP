from pico2d import *
import pico2d
import game_framework
import title_state
import random
import ai_boy_IQ10

running = True


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



def enter():
    global boy, grass, selectedboy, team
    boy = Boy()
    grass = Grass()

    team = [Boy() for i in range(20)]
    selectedboy = team[1]

    while running:
        handle_events()

        for boy in team:
            boy.update()

        clear_canvas()
        grass.draw()
        for boy in team:
            boy.draw()
        update_canvas()

        delay(0.05)


def exit():
    global boy, grass
    del(boy)
    del(grass)

class Boy:
   image = None

   LEFT_RUN, RIGHT_RUN = 0, 1

   def __init__(self):
      self.x, self.y = random.randint(100, 700),90
      self.frame = random.randint(0, 7)
      self.dir = 1
      self.state = ai_boy_IQ10.RIGHT_RUN
      if Boy.image == None:
        Boy.image = load_image('animation_sheet.png')
   def update(self):
       if self.state == ai_boy_IQ10.RIGHT_RUN:

           ai_boy_IQ10.handle_right_run(self)

       elif self.state == self.LEFT_RUN:
           self.frame = (self.frame + 1) % 8
           self.x += (self.dir * 5)
       if self.x >= 800:
           self.dir = -1
           self.x = 800
           self.state = self.LEFT_RUN
       elif self.x < 0:
           self.dir = 1
           self.x = 0
           self.state = self.RIGHT_RUN
   def draw(self):
      self.image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)


class Grass:
   def __init__(self):
      self.image = load_image('grass.png')
   def draw(self):
      self.image.draw(400, 30)






def update():
    boy.update()



def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()



    delay(0.05)