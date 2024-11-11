# 이것은 각 상태들을 객체로 구현한 것임.
from random import randint

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, load_font

import game_framework
from state_machine import *
from ball import Ball
import game_world



PIXEL_PER_METER = (10.0 / 0.3)
FLY_SPEED_KMPH = 40.0
FLY_SPEED_MPM = (FLY_SPEED_KMPH * 1000.0 / 60.0)
FLY_SPEED_MPS = (FLY_SPEED_MPM / 60.0)
FLY_SPEED_PPS = (FLY_SPEED_MPS * PIXEL_PER_METER)
BIRD_SIZE_METER = 5
BIRD_SIZE_PIXEL = BIRD_SIZE_METER * PIXEL_PER_METER

TIME_PER_ACTION = 2.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14









class Bird:

    def __init__(self):
        self.x, self.y = randint(100, 1200), randint(100, 550)
        self.width = int(918 / 5)
        self.height = int(506 / 3)
        self.face_dir = 1
        self.frame = 0
        self.dir = 1
        self.action = 0
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)

        self.font = load_font('ENCR10B.TTF', 16)
    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        self.x += self.dir * FLY_SPEED_PPS * game_framework.frame_time
        if self.x > 1600 - BIRD_SIZE_PIXEL / 2 or self.x - BIRD_SIZE_PIXEL / 2 < 0:
            self.dir *= -1

    def handle_event(self, event):

        pass

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * self.width, (2 - (int(self.frame) // 5)) * self.height,self.width - 10, self.height - 3, 0, '',  self.x, self.y, BIRD_SIZE_PIXEL, BIRD_SIZE_PIXEL)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * self.width, (2 - (int(self.frame) // 5)) * self.height,self.width - 10, self.height - 3, 0, 'h',  self.x, self.y, BIRD_SIZE_PIXEL, BIRD_SIZE_PIXEL)

