from pico2d import *
import pico2d
import game_framework
import main_state
import get_frame_time_rate

running = True

current_time = get_time()


def handle_events():
    global running
    global boy

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:


            running = False
        elif event.type == SDL_KEYDOWN:
           if event.key == SDLK_RIGHT:
              b_g.state = b_g.RIGHT_GO
              boy.state = 1
           elif event.key == SDLK_LEFT:
              b_g.state = b_g.LEFT_GO
              boy.state = 0
           elif event.key == SDLK_ESCAPE:
               running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                b_g.state = b_g.STOP
                boy.state = 3
            elif event.key == SDLK_LEFT:
                b_g.state = b_g.STOP
                boy.state = 2


class Background:
   x = 0
   y = 136

   LEFT_GO =2
   RIGHT_GO=1
   STOP=0

   PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
   RUN_SPEED_KMPH = 20.0
   RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
   RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
   RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)



   def __init__(self):
      self.image = load_image('background.png')
      self.state = self.STOP
   def draw(self):
      self.image.draw(self.x, self.y)
      self.image.draw(self.x+960, self.y)
   def update(self,frame_time):
      if self.x >= 480:
         self.x = -480
      elif self.x <= -480:
          self.x = 480

      distance = self.RUN_SPEED_PPS * frame_time
      if self.state == self.STOP:
          self.x = self.x
      elif self.state == self.RIGHT_GO:
          self.x += -distance
      elif self.state == self.LEFT_GO:
          self.x += distance
      #self.x = self.x + 4

class Boy:



   TIME_PER_ACTION = 0.5
   ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
   FRAMES_PER_ACTION = 8
   total_frames = 0

   image = None


   LEFT_RUN, RIGHT_RUN = 0, 1
   LEFT_STAND, RIGHT_STAND = 2, 3

   def __init__(self):
      self.x, self.y =200,50
      self.frame = 0
      self.dir = 1
      self.state = self.RIGHT_STAND
      self.run_frames = 0
      self.stand_frames = 0
      if Boy.image == None:
        Boy.image = load_image('animation_sheet.png')

   def update(self):

      self.frame = (self.frame + 1) % 8



   def draw(self):
      self.image.clip_draw(self.frame*100, self.state * 100, 100, 100, self.x, self.y)


open_canvas(400,272,sync=True)
b_g=Background()
boy = Boy()

while running == True:

   frame_time = get_time() - current_time
   handle_events()
   #frame_time = get_frame_time_rate.FPS()
   b_g.update(frame_time)
   boy.update()
   clear_canvas()

   b_g.draw()
   boy.draw()
   update_canvas()


   frame_rate = 1.0 / frame_time
   print("Frame Rate : %f fps, Frame Time : %f sec" % (frame_rate, frame_time))

   current_time += frame_time

   delay(0.05)


close_canvas()