from pico2d import *
import pico2d
import game_framework
import numbers



open_canvas()
running = True

move = False
x = 60
y = 190

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
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            turn_change()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            turn_change()




        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.x > 50 and event.x <150 and event.y > 235 and event.y < 265:

                move = True
            elif event.x > 50 and event.x < 150 and event.y > 135 and event.y < 165:
                turn_change()
# 마우스 버튼이 눌릴 좌표를 확인해서 이벤트에 if로 넣어 버리면 부분 클릭 가능







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
   global x
   global y
   def __init__(self):
       self.image = load_image('gunner.png')

   def draw(self):
       self.image.draw(x, y)


class Ground:


   def __init__(self):
       self.image = load_image('ground_test.png')

   def draw(self):
       self.image.draw(400, 150)



gunner = Gunner()
UI = UserInterface()
ground = Ground()
rect = draw_rectangle(200,200,200,200)

while running == True:

    if x > 500:
        x = 200


    if turn == 2 and move == True:
        x = x + 100
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