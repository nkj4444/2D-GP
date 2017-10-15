from pico2d import *
import pico2d
import game_framework
import title_state
import random
import ai_boy_IQ10
import numbers
import json




def handle_events():
    global running
    global selectedboy
    global team
    global selectboyindex, selectindex


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

            elif event.key == SDLK_1:
                selectedboy = team[1-1]
                selectindex = 0
            elif event.key == SDLK_2:
                selectedboy = team[2-1]
                selectindex = 1
            elif event.key == SDLK_3:
                selectedboy = team[3-1]
                selectindex = 2

            elif event.key == SDLK_4:
                selectedboy = team[4-1]
                selectindex = 3
            elif event.key == SDLK_5:
                selectedboy = team[5-1]
                selectindex = 4
                """
            elif event.key == SDLK_6:
                selectedboy = team[6]
                selectindex = 5
            elif event.key == SDLK_7:
                selectedboy = team[7]
                selectindex = 6
            elif event.key == SDLK_8:
                selectedboy = team[8]
                selectindex = 7
            elif event.key == SDLK_9:
                selectedboy = team[9]
                selectindex = 8
            elif event.key == SDLK_0:
                selectedboy = team[0]
                selectindex = -1
             """
                # json의 플레이어 수가 5이기에 나머지 키 잠금
            elif event.key == SDLK_RIGHT:
                selectedboy.state = 1
                if event.key == SDLK_LEFT:
                    selectedboy.state = 0
            elif event.key == SDLK_LEFT:
                selectedboy.state = 0
                if event.key == SDLK_RIGHT:
                    selectedboy.state = 1

# 키보드 위아래 눌러서 숫자 변화시키기

            elif event.key == SDLK_UP:
                if selectindex == 4:
                    selectindex = 0
                else:
                    selectindex += 1
                selectedboy = team[selectindex]
            elif event.key == SDLK_DOWN:
                if selectindex == 0:
                    selectindex = 4
                else:
                    selectindex -= 1
                selectedboy = team[selectindex]




# 키보드에서 손 떼었을때
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                selectedboy.state = 3
                if event.key == SDLK_LEFT:
                    selectedboy.state = 2

            elif event.key == SDLK_LEFT:
                selectedboy.state = 2
                if event.key == SDLK_RIGHT:
                    selectedboy.state = 3





def main():
    global boy, grass, selectedboy, team, running




    open_canvas()
    boy = Boy()
    grass = Grass()



def create_team():


    player_state_table = {
        "LEFT_RUN" : Boy.LEFT_RUN,
        "RIGHT_RUN": Boy.RIGHT_RUN,
        "LEFT_STAND": Boy.LEFT_STAND,
        "RIGHT_STAND": Boy.RIGHT_STAND

    }


    team_data_file = open('team_data.json', 'r')
    team_data = json.load(team_data_file)
    team_data_file.close()

    team = []
    for name in team_data:
        player = Boy()
        player.name = name
        player.x = team_data[name]['x']
        player.y = team_data[name]['y']
        player.state = player_state_table[team_data[name]['StartState']]
        team.append(player)
    return team




def enter():
    global boy, grass, selectedboy, team, selectboyindex, selectindex
    boy = Boy()
    grass = Grass()
    maxboy = 10
    selectindex = 0
    selectboyindex = 1
    #team = [Boy() for i in range(maxboy)]
    #maxboy 수 만큼 보이들을 생성

    team = create_team()



    selectedboy = team[0]
    running = True
    while running:
        handle_events()
        for boy in team:
            boy.update()

        clear_canvas()
        grass.draw()
        numbers.draw(selectindex + 1, 740, 540)

        for boy in team:
            boy.draw()
        for i in range(5):
            numbers.draw(i+1, team[i].x, team[i].y + 45, 0.3)


# 보이들 각자에 그려질 숫자들은 0~ maxboy 까지 였으나 json을 위해 임의로 수정(maxboy->5)


        update_canvas()

        delay(0.05)
    close_canvas()






def exit():
    global boy, grass
    del(boy)
    del(grass)



if __name__ == '__main__':
    main()

class Boy:
   image = None


   LEFT_RUN, RIGHT_RUN = 0, 1
   LEFT_STAND, RIGHT_STAND = 2, 3

   def __init__(self):
      self.x, self.y = random.randint(100, 700),90
      self.frame = random.randint(0, 7)
      self.dir = 1
      self.state = self.RIGHT_RUN
      self.run_frames = 0
      self.stand_frames = 0
      if Boy.image == None:
        Boy.image = load_image('animation_sheet.png')

   def update(self):
       if self.state == self.RIGHT_RUN:
           self.frame = (self.frame + 1) % 8
           ai_boy_IQ10.handle_right_run(self)

       elif self.state == self.LEFT_RUN:
           self.frame = (self.frame + 1) % 8
           ai_boy_IQ10.handle_left_run(self)
       elif self.state == self.LEFT_STAND:
           self.frame = (self.frame + 1) % 8
           ai_boy_IQ10.handle_left_stand(self)
       elif self.state == self.RIGHT_STAND:
           self.frame = (self.frame + 1) % 8
           ai_boy_IQ10.handle_right_stand(self)


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
    global selectindex
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()



    delay(0.05)