from pico2d import *
import pico2d
import game_framework
import numbers

import random


open_canvas(1400,1000)
running = True
move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2 = False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False
move,attack = False,False
mouse_cursor_change = False
attack_point_pop,move_point_pop = False,False
end = False
player_shot_sound = None
enemy_shot_sound = None


player_move1_trigger,player_move2_trigger,player_attack_trigger,player_rest_trigger,player_hit_trigger = False,False,False,False,False
enemy_move1_trigger,enemy_move2_trigger,enemy_attack_trigger,enemy_rest_trigger,enemy_hit_trigger,enemy_fallback_trigger = False,False,False,False,False,False

gunnerX = 260
gunnerY = 490
turn = 1
cursor_x = 300
cursor_y = 300
player_hp = 10
player_ep = 10
move_point_x = -100
move_point_y = -100
attack_point_x = -100
attack_point_y = -100
w = 20
h = 15

p_hit_frame = 0
e_hit_frame = 0
#왜인진 모르겠으나 범위를 넓게 잡지 않으면 리스트를 벗어난다는 오류가 뜬다
maprect = [[to_sdl_rect(0,0,100,100) for col in range(w)] for row in range(h)]


for i in range(h):
    for j in range(w):
        maprect[i][j] = to_sdl_rect(i * 100, j * 100, 100, 100)


"""
player_position_matrix = [[0 for col in range(w)] for row in range(h)]
player_position = player_position_matrix[0][1]
"""
P_x = 2
P_y = 4

events = get_events()




def handle_events():
    global running
    global x
    global y
    global move,attack
    global move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2
    global rect1
    global cursor_x, cursor_y,mouse_cursor_change,move_point_x,move_point_y,move_point_pop,attack_point_x,attack_point_y,attack_point_pop
    global player_move1_trigger,player_attack_trigger,player_rest_trigger,end

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

            if end == True:
                running = False
            elif event.x > 300 and event.x <600 and event.y > 900 and event.y < 1000:
                move = True
                attack = False
                cursor_x = 300
                cursor_y = 300
                mouse_cursor_change = True
            elif event.x > 0 and event.x < 300 and event.y > 800 and event.y < 900:
                attack = True
                move = False
                cursor_x = 300
                cursor_y = 300
                mouse_cursor_change = True
            elif event.x > 0 and event.x <300 and event.y > 900 and event.y < 1000:
                player_attack_trigger,player_move1_trigger = False,False
                move,attack = False,False
                mouse_cursor_change = False
                attack_point_pop = False
                move_point_pop = False
                player_rest_trigger = True

            elif event.x > 300 and event.x < 600 and event.y > 800 and event.y < 900:
                turn_change()
            elif event.y < 300 or event.y > 700 and move == True:
                print('overrange!')
                move = False
                attack = False
            elif event.y < 300 or event.y > 700 and attack == True:
                print('overrange!')
                attack = False
                move = False


        elif event.type == SDL_MOUSEBUTTONUP and turn ==1 and move == True:

            if event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move6_1 = True
                player_move1_trigger = True
                move8_1, move4_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False,False,False,False,False,False,False
                mouse_cursor_change = False
                attack_point_pop = False
                move_point_x =  maprect[P_x+1][P_y].x+50
                move_point_y = 1000-maprect[P_x][P_y-1].y+50
                move_point_pop = True
            elif event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move8_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move4_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x][P_y].x + 50
                move_point_y = 1000-maprect[P_x][P_y].y + 50
                move_point_pop = True
            elif P_y < 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and  maprect[P_x+1][P_y].x+100:
                move2_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y - 1].y - 50
                move_point_pop = True
            elif P_y >= 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move2_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x][P_y].x+50
                move_point_y = 1000-maprect[P_x][P_y-1].y-50
                move_point_pop = True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move4_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x - 1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y].y - 50
                move_point_pop = True
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
                move4_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move2_1, move7_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x-1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y].y- 50
                move_point_pop = True
            elif event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move9_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x+1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y+1].y - 50
                move_point_pop = True
            elif event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move3_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move9_1, move1_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x+1][P_y].x + 50
                move_point_y = 1000 -  maprect[P_x][P_y-1].y - 50
                move_point_pop = True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move7_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x - 1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y + 1].y - 50
                move_point_pop = True

            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
                move7_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move9_1, move1_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x-1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y+1].y - 50
                move_point_pop = True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move1_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move9_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x - 1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y - 1].y - 50
                move_point_pop = True


            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                move1_1 = True
                attack_point_pop = False
                player_move1_trigger = True
                move6_1, move8_1, move4_1, move2_1, move7_1, move9_1, move3_1 = False, False, False, False, False, False, False
                mouse_cursor_change = False
                move_point_x = maprect[P_x-1][P_y].x + 50
                move_point_y = 1000 - maprect[P_x][P_y - 1].y - 50
                move_point_pop = True



        elif event.type == SDL_MOUSEBUTTONUP and turn == 1 and attack == True and event.y < 700 and event.y > 300:

            if event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
               # move6_1
                move_point_pop = False
                mouse_cursor_change = False
                player_attack_trigger = True

                attack_point_x =  maprect[P_x+1][P_y].x+50
                attack_point_y = 1000-maprect[P_x][P_y-1].y+50
                attack_point_pop = True
            elif event.x > maprect[P_x+2][P_y].x and event.x < maprect[P_x+3][P_y].x and event.y > maprect[P_x+1][P_y].y and event.y < maprect[P_x+1][P_y-1].y:
               # move6_2
                move_point_pop = False
                mouse_cursor_change = False
                player_attack_trigger = True

                attack_point_x =  maprect[P_x+2][P_y].x+50
                attack_point_y = 1000-maprect[P_x+1][P_y-1].y+50
                attack_point_pop = True
            elif event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
               # move8_1
                move_point_pop = False
                mouse_cursor_change = False
                player_attack_trigger = True

                attack_point_x = maprect[P_x][P_y].x + 50
                attack_point_y = 1000-maprect[P_x][P_y].y + 50
                attack_point_pop = True
            elif event.x > maprect[P_x][P_y+1].x and event.x < maprect[P_x+1][P_y+1].x and event.y > maprect[P_x][P_y+2].y and event.y < maprect[P_x][P_y+1].y:
               # move8_2
                move_point_pop = False
                mouse_cursor_change = False
                player_attack_trigger = True

                attack_point_x = maprect[P_x][P_y+1].x + 50
                attack_point_y = 1000-maprect[P_x][P_y+1].y + 50
                attack_point_pop = True
            elif P_y < 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and  maprect[P_x+1][P_y].x+100:
                # move2_1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y - 1].y - 50
                attack_point_pop = True
            elif P_y < 2 and event.x > maprect[P_x][P_y-1].x and event.x < maprect[P_x+1][P_y-1].x and event.y > maprect[P_x][P_y-2].y and  maprect[P_x+1][P_y-1].x+100:
                # move2_2
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x][P_y-1].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y - 2].y - 50
                attack_point_pop = True
            elif P_y >= 2 and event.x > maprect[P_x][P_y].x and event.x < maprect[P_x+1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
               # move2_1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x][P_y].x+50
                attack_point_y = 1000-maprect[P_x][P_y-1].y-50
                attack_point_pop= True
            elif P_y >= 2 and event.x > maprect[P_x][P_y-1].x and event.x < maprect[P_x+1][P_y-1].x and event.y > maprect[P_x][P_y-2].y and event.y < maprect[P_x][P_y-3].y:
               # move2_2
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x][P_y-1].x+50
                attack_point_y = 1000-maprect[P_x][P_y-2].y-50
                attack_point_pop= True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
               # move4_1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x - 1][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y].y - 50
                attack_point_pop = True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x-1][P_y].y and event.y < maprect[P_x-1][P_y-1].y:
               # move4_2
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x - 2][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x-1][P_y].y - 50
                attack_point_pop = True
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y].y and event.y < maprect[P_x][P_y-1].y:
               # move4_1
                move_point_pop = False
                mouse_cursor_change = False
                player_attack_trigger = True
                attack_point_x= maprect[P_x-1][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y].y- 50
                attack_point_pop = True
            elif P_x >= 2 and event.x > maprect[P_x-2][P_y].x and event.x < maprect[P_x-1][P_y].x and event.y > maprect[P_x-1][P_y].y and event.y < maprect[P_x-1][P_y-1].y:
               # move4_2
                move_point_pop = False
                mouse_cursor_change = False
                player_attack_trigger = True
                attack_point_x= maprect[P_x-2][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x-1][P_y].y- 50
                attack_point_pop = True
            elif event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
               # move9_1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+1][P_y].x + 50
                attack_point_y= 1000 - maprect[P_x][P_y+1].y - 50
                attack_point_pop = True
            elif event.x > maprect[P_x+2][P_y+1].x and event.x < maprect[P_x+3][P_y+1].x and event.y > maprect[P_x+1][P_y+2].y and event.y < maprect[P_x+1][P_y+1].y:
               # move9_2
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+2][P_y+1].x + 50
                attack_point_y= 1000 - maprect[P_x+1][P_y+2].y - 50
                attack_point_pop = True
            elif event.x > maprect[P_x + 1][P_y+1].x and event.x < maprect[P_x + 2][P_y+1].x and event.y > maprect[P_x][P_y + 2].y and event.y < maprect[P_x][P_y+1].y:
                # move9_1+y1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x + 1][P_y+1].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y + 2].y - 50
                attack_point_pop = True
            elif event.x > maprect[P_x+2][P_y].x and event.x < maprect[P_x+3][P_y].x and event.y > maprect[P_x+1][P_y+1].y and event.y < maprect[P_x+1][P_y].y:
               # move9_1+x1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+2][P_y].x + 50
                attack_point_y= 1000 - maprect[P_x+1][P_y+1].y - 50
                attack_point_pop = True

            elif event.x > maprect[P_x+1][P_y].x and event.x < maprect[P_x+2][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
               # move3_1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+1][P_y].x + 50
                attack_point_y = 1000 -  maprect[P_x][P_y-1].y - 50
                attack_point_pop= True
            elif event.x > maprect[P_x+2][P_y-1].x and event.x < maprect[P_x+3][P_y-1].x and event.y > maprect[P_x+1][P_y-2].y and event.y < maprect[P_x+1][P_y-3].y:
               # move3_2
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+2][P_y-1].x + 50
                attack_point_y = 1000 -  maprect[P_x+1][P_y-2].y - 50
                attack_point_pop= True
            elif event.x > maprect[P_x+2][P_y].x and event.x < maprect[P_x+3][P_y].x and event.y > maprect[P_x+1][P_y-1].y and event.y < maprect[P_x+1][P_y-2].y:
               # move3_1+x1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+2][P_y].x + 50
                attack_point_y = 1000 -  maprect[P_x+1][P_y-1].y - 50
                attack_point_pop= True
            elif event.x > maprect[P_x+1][P_y-1].x and event.x < maprect[P_x+2][P_y-1].x and event.y > maprect[P_x][P_y-2].y and event.y < maprect[P_x][P_y-3].y:
               # move3_1-y1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x+1][P_y-1].x + 50
                attack_point_y = 1000 -  maprect[P_x][P_y-2].y - 50
                attack_point_pop= True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
              #  move7_1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x - 1][P_y].x + 50
                attack_point_y= 1000 - maprect[P_x][P_y + 1].y - 50
                attack_point_pop = True
            elif P_x < 2 and event.x > maprect[0][P_y+1].x and event.x < maprect[1][P_y+1].x and event.y > maprect[P_x-1][P_y+2].y and event.y < maprect[P_x-1][P_y+1].y:
              #  move7_2
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x - 2][P_y+1].x + 50
                attack_point_y= 1000 - maprect[P_x-1][P_y + 2].y - 50
                attack_point_pop = True

            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y+1].y and event.y < maprect[P_x][P_y].y:
              # move7_1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-1][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y+1].y - 50
                attack_point_pop= True
            elif P_x >= 2 and event.x > maprect[P_x-2][P_y].x and event.x < maprect[P_x-1][P_y].x and event.y > maprect[P_x-1][P_y+1].y and event.y < maprect[P_x-1][P_y].y:
              # move7_1-x1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-2][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x-1][P_y+1].y - 50
                attack_point_pop= True
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y+1].x and event.x < maprect[P_x][P_y+1].x and event.y > maprect[P_x][P_y+2].y and event.y < maprect[P_x][P_y+1].y:
              # move7_1+y1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-1][P_y+1].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y+2].y - 50
                attack_point_pop= True
            elif P_x >= 2 and event.x > maprect[P_x-2][P_y+1].x and event.x < maprect[P_x-1][P_y+1].x and event.y > maprect[P_x-1][P_y+2].y and event.y < maprect[P_x-1][P_y+1].y:
              # move7_2
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-2][P_y+1].x + 50
                attack_point_y = 1000 - maprect[P_x-1][P_y+2].y - 50
                attack_point_pop= True
            elif P_x < 2 and event.x > maprect[0][P_y].x and event.x < maprect[1][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
                # move7_1
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x - 1][P_y].x + 50
                attack_point_y= 1000 - maprect[P_x][P_y - 1].y - 50
                attack_point_pop= True
            elif P_x < 2 and event.x > maprect[0][P_y+1].x and event.x < maprect[1][P_y+1].x and event.y > maprect[P_x-1][P_y].y and event.y < maprect[P_x-1][P_y-1].y:
                # move7_2
                move_point_pop = False
                player_attack_trigger = True
                mouse_cursor_change = False
                attack_point_x = maprect[P_x - 2][P_y+1].x + 50
                attack_point_y= 1000 - maprect[P_x-1][P_y].y - 50
                attack_point_pop= True


            elif P_x >= 2 and event.x > maprect[P_x-1][P_y].x and event.x < maprect[P_x][P_y].x and event.y > maprect[P_x][P_y-1].y and event.y < maprect[P_x][P_y-2].y:
               # move1_1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-1][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y - 1].y - 50
                attack_point_pop= True
            elif P_x >= 2 and event.x > maprect[P_x-2][P_y-1].x and event.x < maprect[P_x-1][P_y-1].x and event.y > maprect[P_x-1][P_y-2].y and event.y < maprect[P_x-1][P_y-3].y:
               # move1_2
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-2][P_y-1].x + 50
                attack_point_y = 1000 - maprect[P_x-1][P_y - 2].y - 50
                attack_point_pop= True
            elif P_x >= 2 and event.x > maprect[P_x-2][P_y].x and event.x < maprect[P_x-1][P_y].x and event.y > maprect[P_x-1][P_y-1].y and event.y < maprect[P_x-1][P_y-2].y:
               # move1_1-x1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-2][P_y].x + 50
                attack_point_y = 1000 - maprect[P_x-1][P_y - 1].y - 50
                attack_point_pop= True
            elif P_x >= 2 and event.x > maprect[P_x-1][P_y-1].x and event.x < maprect[P_x][P_y-1].x and event.y > maprect[P_x][P_y-2].y and event.y < maprect[P_x][P_y-3].y:
               # move1_1-y1
                player_attack_trigger = True
                move_point_pop = False
                mouse_cursor_change = False
                attack_point_x = maprect[P_x-1][P_y-1].x + 50
                attack_point_y = 1000 - maprect[P_x][P_y - 2].y - 50
                attack_point_pop= True

        elif event.type == SDL_MOUSEMOTION:
            if move == True or attack == True:
                if event.y < 700 and event.y > 300:
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




class Mousecursor:
    global cursor_x, move_point_x
    global cursor_y, move_point_y


    def __init__(self):
        self.image = load_image('cursor.png')
        self.move_point_image = load_image('move_point.png')
        self.move_point_image.opacify(600)





    def attack_cursor(self):
        self.image.clip_draw(100, 0, 100, 100, cursor_x, cursor_y, 100, 100)


    def move_cursor(self):
        self.image.clip_draw(0, 0, 100, 100, cursor_x, cursor_y, 100, 100)

    def move_point_move(self):

        self.move_point_image.clip_draw(0,0,100,100,move_point_x,move_point_y,100,100)
    def move_point_attack(self):

        self.move_point_image.clip_draw(100,0,100,100,attack_point_x,attack_point_y,100,100)



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
    p_x=11
    p_y=2

    hp = 10
    ep = 10
    damage = 2
    speed = 1
    ATTACK = 1
    SEARCH = 2
    REROADING = 3
    REST = 4
    FALLBACK = 5
    scare_stack = 0

    move = True
    attack = False
    rest = False
    reroading = False

    run_stack = [None for i in range(5)]




    state = SEARCH

    def enemy_move1(self):
        global enemy_move1_trigger

        if self.move == True and turn == 3 and self.ep >=2:
            if self.p_x > P_x and (self.p_x - P_x) != 1 and (self.p_x - P_x) != -1: # x만 해놓음
                self.p_x -= 1
                self.x -= 100
            elif self.p_x < P_x:
                self.p_x += 1
                self.x += 100
        self.ep -= 2
        print('enemy move')

        self.move == False
        enemy_move1_trigger = False
    def enemy_fallback(self):
        global enemy_fallback_trigger,enemy_rest_trigger
        rand_pick = random.randint(1,3)

        if turn == 3 and self.p_x < 14 and self.p_y > 1 and self.p_y < 4 and self.ep >= 2:
            print('enemy fallback')
            if rand_pick == 2:
                self.p_x += 1
                self.x += 100
                self.ep -= 2
            elif rand_pick == 1 and self.p_y < 4:
                self.p_x += 1
                self.p_y += 1
                self.x += 100
                self.y += 100
                self.ep -= 2
            elif rand_pick == 3 and self.p_y > 1:
                self.p_x += 1
                self.p_y -= 1
                self.x += 100
                self.y -= 100
                self.ep -= 2

        elif turn ==3 and self.p_y ==1 and self.ep >=2:
            self.p_y+=1
            self.y += 100
            self.ep -= 2
        elif turn ==3 and self.p_y ==4 and self.ep >=2:
            self.p_y-=1
            self.y -= 100
            self.ep -= 2
        elif turn ==3 and self.p_x ==14 and self.ep >=2:
            self.p_x-=1
            self.x -= 100
            self.ep -= 2
        elif turn ==3 and self.ep < 2:
            self.state = self.REST
            enemy_rest_trigger = True

        self.move == False

        enemy_fallback_trigger = False


    def enemy_attack(self):
        global enemy_attack_trigger
        if self.state == self.ATTACK:
            global player_hp,gunnerX,gunnerY,enemy_shot_sound
            global player_hit_trigger
            if enemy_shot_sound == None:

                enemy_shot_sound = load_wav('Gun.wav')
                enemy_shot_sound.set_volume(96)




            #self.image.clip_draw(100, 0, 100, 100, cursor_x, cursor_y, 100, 100)
            self.testimage=load_image('cursor.png')
            if self.attack == True:
                enemy_shot_sound.play()
                #self.image.clip_draw(100, 0, 100, 100,maprect[P_x + random.randint(-1, 1)][P_x + random.randint(-1, 1)].x,maprect[P_x + random.randint(-1, 1)][P_x + random.randint(-1, 1)].y, 100, 100)
                random_pick = random.randint(0, 5)
                if random_pick <= 4:  #4/5확률로 맞음
                    if random_pick == 2:
                        player_hp -= 2
                    else:
                        player_hp -= 1
                    player_hit_trigger = True

            self.ep -=1
            print('enemy attack')
            self.attack == False
            self.state = self.SEARCH
            enemy_attack_trigger = False
    def enemy_rest(self):
        global enemy_rest_trigger
        print('enemy rest')
        if self.ep < 8:
            self.ep+=3
        else:
            self.ep == 10





    def enemy_ai(self):
        global enemy_attack_trigger, enemy_hit_trigger, enemy_move1_trigger, enemy_move2_trigger, enemy_rest_trigger,enemy_fallback_trigger
        lessposition = min(self.p_x,P_x)
        biggerposition = max(self.p_x,P_x)
        interval = biggerposition-lessposition   #플레이어와 적 사이의 거리(칸수)를 interval로 설정
        rand_pick = random.randint(1,4)

        print('random ',rand_pick,'enemy EP  ',self.ep,'interval ',interval)
        """
        1~2 = serch
           3 = fallback
        4 = rest
        
        """

        if self.hp < 3 and self.p_x<14 and self.p_y < 4 and self.scare_stack < 3:
            self.state = self.FALLBACK
            enemy_fallback_trigger = True
            self.scare_stack +=1
        elif self.ep == 0:
            self.state = self.REST
            enemy_rest_trigger = True


        elif rand_pick <= 3:
            if rand_pick <= 2 and self.ep > 2 and interval > 3:
                self.statae = self.SEARCH
                enemy_attack_trigger = False
                enemy_rest_trigger = False
                enemy_fallback_trigger = False
                enemy_move1_trigger = True
            elif interval <= 4 and rand_pick < 3 and self.ep > 1:
                self.state = self.ATTACK
                self.attack = True
                enemy_move1_trigger = False
                enemy_attack_trigger = True
            elif rand_pick == 3 and self.ep > 2:
                enemy_attack_trigger = False
                enemy_rest_trigger = False
                enemy_fallback_trigger = True
                enemy_move1_trigger = False
                self.state = self.FALLBACK
            else:
                self.state = self.REST
                enemy_rest_trigger = True
        elif rand_pick == 4:
            self.state = self.REST
            enemy_rest_trigger = True
        if self.scare_stack >=3:
            self.scare_stack == 0



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
       self.bgm = load_music('Lo+malo+lo+bueno+y+lo+feo.mp3')
       self.bgm.set_volume(74)
       self.bgm.repeat_play()

   def draw(self):
       self.image.draw(700, 500)

def player_rest():
    global  player_ep,player_rest_trigger
    if player_ep < 8:
        player_ep += 3
    else:
        player_ep = 10
    player_rest_trigger = False

def player_move():
    global move,move6_1, move8_1,move4_1,move2_1,move7_1,move9_1,move1_1,move3_1,move6_2, move8_2,move4_2,move2_2,move7_2,move9_2,move1_2,move3_2
    global gunnerX,gunnerY,P_x,P_y,player_move1_trigger,move_point_pop,attack_point_pop,player_ep

    if turn == 3 and move == True and player_ep >= 2:
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
        player_ep -= 2
    player_move1_trigger = False
    move_point_pop = False


enemy = Enemy()

class UserInterface:


    def __init__(self):
        self.image = load_image('button_test.png')
        self.hit_image = load_image('hit.png')

    def draw(self):
        self.image.clip_draw(0, 0, 100, 40, 100, 350, 100, 30)
        self.image.clip_draw(0, 40, 100, 40, 100, 400, 100, 30)
        self.image.clip_draw(0, 80, 100, 40, 100, 450, 100, 30)
        ##(x가시작되는위치,y가시작되는위치,표시할넓이,표시할높이,x좌표,y좌표,x축스케일,y축스케일)

    def hit_on_player(self):
        global player_hit_trigger, p_hit_frame
        if p_hit_frame < 120:
            self.hit_image.draw(gunnerX, gunnerY)  # hitframe으로 그릴 시간조정, hit_trigger활성시 발동. 맞는 이펙트 그리기
            p_hit_frame += 1
        else:
            p_hit_frame = 0
            player_hit_trigger = False
    def hit_on_enemy(self):
        global enemy_hit_trigger, e_hit_frame,player_shot_sound

        if e_hit_frame < 120:

            self.hit_image.draw(enemy.x, enemy.y)  # hitframe으로 그릴 시간조정, hit_trigger활성시 발동. 맞는 이펙트 그리기
            e_hit_frame += 1
        else:
            e_hit_frame = 0
            enemy_hit_trigger = False

def player_attack():
    global player_shot_sound,gunnerX, gunnerY, P_x, P_y, player_move1_trigger, move_point_pop, attack_point_pop,attack_point_x,attack_point_y,enemy_hit_trigger,player_ep
    if player_shot_sound == None:
        player_shot_sound = load_wav('Gun5.wav')
        player_shot_sound.set_volume(96)
    random_pick = random.randint(1,3)
    if attack_point_pop == True and player_ep >= 1:
        player_shot_sound.play()
        if enemy.x <= attack_point_x+100 and enemy.x >= attack_point_x and enemy.y >= attack_point_y and enemy.y <= attack_point_y+100:
            enemy_hit_trigger = True

            if random_pick == 2:
                enemy.hp -= 2
            else:
                enemy.hp -= 1
        player_ep -= 1
    attack_point_pop = False


class Point_bar:
    def __init__(self):
        self.image = load_image('point_bar.png')
        self.back_image = load_image('point_bar_background.png')
    def draw_HP(self):
        self.back_image.clip_draw(0, 0, 300, 50, 1015 + (35 / 2) * 10, 195, 350, 120)
        self.image.clip_draw(0, 50, 300, 50, 1015+(35/2)*player_hp, 195, 35*player_hp, 100)
        numbers.draw(player_hp, 1200, 245, 0.7)
        self.back_image.clip_draw_to_origin(0, 0, 300, 50, enemy.x - 55, enemy.y + 67, 100, 30)
        self.back_image.clip_draw_to_origin(0, 0, 300, 50, gunnerX - 55, gunnerY + 67, 100, 30)
        self.image.clip_draw_to_origin(0, 50, 300, 50, enemy.x-55, enemy.y + 70, enemy.hp*10, 25)
        self.image.clip_draw_to_origin(0, 50, 300, 50, gunnerX - 55, gunnerY + 70, player_hp * 10, 25)
    def draw_EP(self):
        self.back_image.clip_draw(0, 0, 300, 50, 1015 + (35 / 2) * 10, 95, 350, 120)
        self.image.clip_draw(0, 0, 300, 50, 1015+(35/2)*player_ep, 95, 35*player_ep, 100)
        numbers.draw(player_ep, 1200, 145, 0.7)

gunner = Gunner()
UI = UserInterface()
ground = Ground()
map = Map()
m_cursor = Mousecursor()
p_bar = Point_bar()

object_num = 8

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
    if enemy_fallback_trigger == True:
        action_list[2] = enemy.enemy_fallback()
    else:
        action_list[2] = None
    if player_attack_trigger == True:
        action_list[3] = player_attack()
    else:
        action_list[3] = None
    if enemy_attack_trigger == True:
        action_list[4] = enemy.enemy_attack()
    else:
        action_list[4] = None

    if player_rest_trigger == True:
        action_list[5] = player_rest()
    else:
        action_list[5] = None
    if enemy_rest_trigger == True:
        action_list[6] = enemy.enemy_rest()
    else:
        action_list[6] = None

def end_check():
    global end
    if player_hp == 0:
        end = True
    elif enemy.hp == 0:
        end = True


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
    end_check()

    #ground.draw()
    map.draw()
    p_bar.draw_HP()
    p_bar.draw_EP()



    if move_point_pop == True:

        m_cursor.move_point_move()
    elif attack_point_pop == True:
        m_cursor.move_point_attack()




    gunner.draw()
    enemy.draw()

    if enemy_hit_trigger == True:
        UI.hit_on_enemy()


    elif player_hit_trigger == True:
        UI.hit_on_player()



    #UI.draw()
    numbers.draw(turn, 450, 250, 1)  # 턴 나타내는 숫자. 테스트용

    if mouse_cursor_change == True:
        if move == True:
            m_cursor.move_cursor()
        elif attack == True:
            m_cursor.attack_cursor()
    if end == True:
        load_image('game_over.png').draw(700,500)


    update_canvas()
    clear_canvas()

close_canvas()