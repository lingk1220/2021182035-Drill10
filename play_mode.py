from pico2d import *
import game_framework

import game_world
from bird import Bird
from grass import Grass
from boy import Boy

# boy = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            #boy.handle_event(event)
            pass

def init():
    global grass
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    birds = [Bird() for _ in range(10)]

    for bird in birds:
        game_world.add_object(bird, 1)


def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    #delay(0.01)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

