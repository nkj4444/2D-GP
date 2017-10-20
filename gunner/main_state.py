from pico2d import *
import pico2d
import game_framework
import numbers


open_canvas()
running = True
move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2 = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
move = False

gunnerX = 60
gunnerY = 190
turn = 1

w = 20
h = 12
#왜인진 모르겠으나 범위를 넓게 잡지 않으면 리스트를 벗어난다는 오류가 뜬다
maprect = [[to_sdl_rect(0,0,100,100) for col in range(w)] for row in range(h)]


for i in range(h):
    for j in range(w):
        maprect[i][j] = to_sdl_rect(i * 100, j * 100, 100, 100)


"""
player_position_matrix = [[0 for col in range(w)] for row in range(h)]
player_position = player_position_matrix[0][1]
"""
P_x = 0
P_y = 1

events = get_events()

def handle_events():
    global running
    global x
    global y
    global move
    global move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2
    global rect1

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and turn == 1:
            turn_change()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT and turn == 1:
            turn_change()




        elif event.type == SDL_MOUSEBUTTONDOWN and turn == 1:
            print(P_x,P_y)


            if event.x > 50 and event.x <150 and event.y > 235 and event.y < 265:
                move = True
            elif event.x > 50 and event.x < 150 and event.y > 135 and event.y < 165:
                turn_change()
        elif event.type == SDL_MOUSEBUTTONUP and turn ==1 and move == True:
            if event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move6_1 = True
            elif event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move8_1 = True
            elif P_y < 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][0].y+100:
                move2_1 = True
            elif P_y >= 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move2_1 = True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move4_1 = True
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move4_1 = True





# 마우스 버튼이 눌릴 좌표를 확인해서 이벤트에 if로 넣어 버리면 부분 클릭 가능
# 마우스 이벤트의 Y 좌표는 화면 꼭대기에서 시작하므로 gunnerY에다가 220을 더해야 쓸 수 있음






def turn_change():
    global turn
    global move

    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 1

#턴은 3 까지 해서 1 = 플레이어, 2 = 적ai, 3 = 움직임 이렇게 해야 할듯

class UserInterface:


    def __init__(self):
        self.image = load_image('button_test.png')

    def draw(self):
        self.image.clip_draw(0, 0, 100, 40, 100, 350, 100, 30)
        self.image.clip_draw(0, 40, 100, 40, 100, 400, 100, 30)
        self.image.clip_draw(0, 80, 100, 40, 100, 450, 100, 30)
        ##(x가시작되는위치,y가시작되는위치,표시할넓이,표시할높이,x좌표,y좌표,x축스케일,y축스케일)

class Gunner:

   def __init__(self):
       self.image = load_image('gunner.png')

   def draw(self):
       self.image.draw(gunnerX, gunnerY)


class Ground:


   def __init__(self):
       self.image = load_image('ground_test.png')

   def draw(self):
       self.image.draw(400, 150)



gunner = Gunner()
UI = UserInterface()
ground = Ground()

while running == True:




    if turn == 2 and move == True:

        if move6_1 == True:
            gunnerX = gunnerX + 100
            P_x = P_x + 1
            move6_1 = False
            move = False
        elif move8_1 == True:
            gunnerY = gunnerY + 100
            P_y = P_y + 1
            move8_1 = False
            move = False
        elif move4_1 == True:
            gunnerX = gunnerX - 100

            P_x = P_x - 1
            move4_1 = False
            move = False
        elif move2_1 == True:
            gunnerY = gunnerY - 100
            P_y = P_y - 1
            move2_1 = False
            move = False





# 움직임 테스트용 move가 True인 상태에서 턴이 2(행동턴인 3으로 바꿔야함)가 되면



# 플레이어의 위치를 이동시키고 move를 False로 변경
    if turn == 1:
        handle_events()
    elif turn ==2:
        delay(2)
        turn_change()
    numbers.draw(turn, 400, 550, 1) # 턴 나타내는 숫자. 테스트용
    ground.draw()
    gunner.draw()
    UI.draw()


    update_canvas()
    clear_canvas()

close_canvas()