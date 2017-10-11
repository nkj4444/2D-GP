LEFT_RUN= 0
RIGHT_RUN,
LEFT_STAND,
RIGHT_STAND


def handle_left_run(self):
    self.x -= 5
    self.run_frames += 1
    if self.x < 0:
        self.state = self.RIGHT_RUN
        self.x = 0
    if self.run_frames == 100:
        self.state = self.LEFT_STAND
        self.stand_frames = 0

def handle_left_statnd(self):
    self.stand_frames += 1
    if self.stand_frames == 50:
        self.state = self.LEFT_RUN
        self,run_frames = 0

def handle_right_run(self):
    self.x += 5
    self.run_frames += 1
    if self.x > 800:
        self.state = self.LEFT_RUN
        self.x = 800
    if self.run_frames == 100:
        self.state = self.RIGHT_STAND
        self.stand_frames = 0


def handle_right_statnd(self):
    self.stand_frames += 1
    if self.stand_frames == 50:
        self.state = self.RIGHT_RUN
        self,run_frames = 0
handle_state = {
    LEFT_RUN: handle_left_run,
    RIGHT_RUN: handle_right_run,
    LEFT_STAND: handle_left_statnd,
    RIGHT_STAND: handle_right_statnd
}
def updaate(self):
    self.frame = (self.frame + 1) % 8
    self.handle_state[self.state](self)