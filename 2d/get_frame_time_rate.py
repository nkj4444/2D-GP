from pico2d import *

current_time = get_time()

def FPS():
    global  current_time,frame_time
    frame_time = get_time() - current_time
    frame_rate = 1.0 / frame_time
    print("Frame Rate : %f fps, Frame Time : %f sec"%(frame_rate,frame_time))

    current_time += frame_time
    return  frame_time
