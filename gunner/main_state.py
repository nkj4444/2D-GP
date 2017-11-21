from pico2d import *
import pico2d
import game_framework
import numbers

import random


open_canvas(1400,1000)
running = True
move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2 = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
move = False
mouse_cursor_change = False

player_move1_trigger,player_move2_trigger,player_attack_trriger,player_rest_trriger,player_hit_trigger = False,False,False,False,False
enemy_move1_trigger,enemy_move2_trigger,enemy_attack_trigger,enemy_rest_trigger,enemy_hit_trigger = False,False,False,False,False

gunnerX = 60
gunnerY = 490
turn = 1
cursor_x = 300
cursor_y = 300
player_hp = 10
player_ep = 10

w = 20
h = 15
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
P_y = 4

events = get_events()




def handle_events():
    global running
    global x
    global y
    global move
    global move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2
    global rect1
    global cursor_x, cursor_y,mouse_cursor_change
    global player_move1_trigger

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



            if event.x > 300 and event.x <600 and event.y > 900 and event.y < 1000:
                move = True
                mouse_cursor_change = True

            elif event.x > 300 and event.x < 600 and event.y > 800 and event.y < 900:
                turn_change()
            elif event.y < 300 or event.y > 700 and move == True:
                print('overrange!')
                move = False

        elif event.type == SDL_MOUSEBUTTONUP and turn ==1 and move == True:

            if event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move6_1 = True
                player_move1_trigger = True
                move8_1, move4_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False,False,False,False,False,False,False
                mouse_cursor_change = False
            elif event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move8_1 = True
                player_move1_trigger = True
                move6_1, move4_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_y < 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][0].y+100:
                move2_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_y >= 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move2_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move4_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move4_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move9_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move3_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move9_1, move1_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move7_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move7_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move1_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move9_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move1_1 = True
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move9_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
        elif event.type == SDL_MOUSEMOTION:
            if move == True and event.y < 700 and event.y > 300:
                cursor_x = event.x
                cursor_y = 1000 - event.y




# 마우스 버튼이 눌릴 좌표를 확인해서 이벤트에 if로 넣어 버리면 부분 클릭 가능
# 마우스 이벤트의 Y 좌표는 화면 꼭대기에서 시작하므로 gunnerY에다가 220을 더해야 쓸 수 있음






def turn_change():
    global turn
    global move


    if turn == 1:
        turn = 2
    elif turn == 2:
        turn = 3

    elif turn == 3:
        turn = 1

        print(P_x, P_y - 3)  # 바뀐위치


#턴은 3 까지 해서 1 = 플레이어, 2 = 적ai, 3 = 움직임 이렇게 해야 할듯

class UserInterface:


    def __init__(self):
        self.image = load_image('button_test.png')
        self.hit_image = load_image('hit.png')

    def draw(self):
        self.image.clip_draw(0, 0, 100, 40, 100, 350, 100, 30)
        self.image.clip_draw(0, 40, 100, 40, 100, 400, 100, 30)
        self.image.clip_draw(0, 80, 100, 40, 100, 450, 100, 30)
        ##(x가시작되는위치,y가시작되는위치,표시할넓이,표시할높이,x좌표,y좌표,x축스케일,y축스케일)





class Point_bar:
    def __init__(self):
        self.image = load_image('point_bar.png')
    def draw_HP(self):
        self.image.clip_draw(0, 50, 300, 50, 1015+(35/2)*player_hp, 195, 35*player_hp, 100)
        numbers.draw(player_hp, 1200, 245, 0.7)
    def draw_EP(self):
        self.image.clip_draw(0, 0, 300, 50, 1015+(35/2)*player_ep, 95, 35*player_ep, 100)
        numbers.draw(player_ep, 1200, 145, 0.7)


class Mousecursor:
    global cursor_x
    global cursor_y


    def __init__(self):
        self.image = load_image('cursor.png')


    def attack_cursor(self):
        self.image.clip_draw(100, 0, 100, 100, cursor_x, cursor_y, 100, 100)


    def move_cursor(self):
        self.image.clip_draw(0, 0, 100, 100, cursor_x, cursor_y, 100, 100)


class Gunner:

   def __init__(self):
       self.image = load_image('gunner.png')

   def draw(self):
       self.image.draw(gunnerX, gunnerY)


class Enemy:

    global turn
    global enemy_attack_trigger,enemy_hit_trigger,enemy_move1_trigger,enemy_move2_trigger,enemy_rest_trigger

    x = 1060
    y = 490
    p_x=9
    p_y=4

    hp = 10
    ep = 10
    damage = 2
    speed = 1
    ATTACK = 1
    SEARCH = 2
    REROADING = 3
    REST = 4

    move = True
    attack = False
    rest = False
    reroading = False

    run_stack = [None for i in range(5)]




    state = SEARCH

    def enemy_move1(self):
        global enemy_move1_trigger

        if self.move == True and turn == 3:
            if self.p_x > P_x and (self.p_x - P_x) != 1 and (self.p_x - P_x) != -1: # x만 해놓음
                self.p_x -= 1
                self.x -= 100
            elif self.p_x < P_x:
                self.p_x += 1
                self.x += 100

        self.move == False
        enemy_move1_trigger = False


    def enemy_attack(self):
        global enemy_attack_trigger
        if self.state == self.ATTACK:
            global player_hp
            global player_hit_trigger


            #self.image.clip_draw(100, 0, 100, 100, cursor_x, cursor_y, 100, 100)
            self.testimage=load_image('cursor.png')
            if self.attack == True:
                #self.image.clip_draw(100, 0, 100, 100,maprect[P_x + random.randint(-1, 1)][P_x + random.randint(-1, 1)].x,maprect[P_x + random.randint(-1, 1)][P_x + random.randint(-1, 1)].y, 100, 100)

                if random.randint(0, 1) == 0:  #반반확률로 맞음 그림 추가필요
                    player_hp -= 1
                    player_hit_trigger = True

            self.attack == False
            self.state = self.SEARCH
            enemy_attack_trigger = False



    def enemy_ai(self):
        global enemy_attack_trigger, enemy_hit_trigger, enemy_move1_trigger, enemy_move2_trigger, enemy_rest_trigger
        lessposition = min(self.p_x,P_x)
        biggerposition = max(self.p_x,P_x)
        interval = biggerposition-lessposition   #플레이어와 적 사이의 거리(칸수)를 interval로 설정
        if interval >= 3:
            self.statae = self.SEARCH
            enemy_move1_trigger = True
        elif interval < 3:
            self.state = self.ATTACK
            self.attack = True
            enemy_attack_trigger = True
        if self.ep == 0:
            self.state = self.REST
            enemy_rest_trigger = True

    print(x , y)


    def __init__(self):
        self.image = load_image('enemy.png')

    def draw(self):
        self.image.draw(self.x-10, self.y)


class Ground:


   def __init__(self):
       self.image = load_image('ground_test.png')

   def draw(self):
       self.image.draw(400, 150)




       ##(x가시작되는위치,y가시작되는위치,표시할넓이,표시할높이,x좌표,y좌표,x축스케일,y축스케일)


class Map:


   def __init__(self):
       self.image = load_image('map_test.png')

   def draw(self):
       self.image.draw(700, 500)


def player_move():
    global move,move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2
    global gunnerX,gunnerY,P_x,P_y,player_move1_trigger

    if turn == 3 and move == True:
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
        elif move7_1 == True:
            gunnerX = gunnerX - 100
            gunnerY = gunnerY + 100
            P_y = P_y + 1
            P_x = P_x - 1
            move7_1 = False
            move = False
        elif move9_1 == True:
            gunnerX = gunnerX + 100
            gunnerY = gunnerY + 100
            P_x = P_x + 1
            P_y = P_y + 1
            move9_1 = False
            move = False
        elif move3_1 == True:
            gunnerX = gunnerX + 100
            gunnerY = gunnerY - 100
            P_x = P_x + 1
            P_y = P_y - 1
            move3_1 = False
            move = False
        elif move1_1 == True:
            gunnerY = gunnerY - 100
            gunnerX = gunnerX - 100
            P_y = P_y - 1
            P_y = P_y - 1
            move1_1 = False
            move = False
    player_move1_trigger = False






gunner = Gunner()
UI = UserInterface()
ground = Ground()
map = Map()
enemy = Enemy()
m_cursor = Mousecursor()
p_bar = Point_bar()

object_num = 8

hit_frame = 0
action_list = list(range(4 * object_num)) #8명분 4*명/5로 수정해야함

def action():
    global action_list

    for i in range(object_num*4):
        if action_list[i] != None:
            action_list[i]







def actionlisting():
    global action_list
    for i in range(object_num*4):
        action_list[i] = None

    if player_move1_trigger == True:
        action_list[0] = player_move()
    else:
        action_list[0] = None
    if enemy_move1_trigger == True:
        action_list[1] = enemy.enemy_move1()
    else:
        action_list[1] = None



    if enemy_attack_trigger == True:
        action_list[3] = enemy.enemy_attack()
    else:
        action_list[3] = None


while running == True:


# 움직임 테스트용 move가 True인 상태에서 턴이 2(행동턴인 3으로 바꿔야함)가 되면



# 플레이어의 위치를 이동시키고 move를 False로 변경
    if turn == 1:
        handle_events()
    elif turn ==2:
        delay(1)
        enemy.enemy_ai()

        turn_change()
    elif turn == 3:
        delay(0.5)
        actionlisting()
        action()

        turn_change()

    #ground.draw()
    map.draw()
    p_bar.draw_HP()
    p_bar.draw_EP()




    gunner.draw()
    enemy.draw()

    if player_hit_trigger == True and hit_frame < 120:
        load_image('hit.png').draw(gunnerX,gunnerY)    # hitframe으로 그릴 시간조정, hit_trigger활성시 발동. 맞는 이펙트 그리기
        hit_frame += 1
    else:
        hit_frame = 0
        player_hit_trigger = False



    #UI.draw()
    numbers.draw(turn, 450, 250, 1)  # 턴 나타내는 숫자. 테스트용

    if mouse_cursor_change == True:
        m_cursor.move_cursor()

    update_canvas()
    clear_canvas()

close_canvas()