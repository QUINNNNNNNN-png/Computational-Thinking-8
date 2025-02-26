#section 1
import codesters, random
from codesters import StageClass
stage = StageClass()
stage.disable_floor()
player = codesters.Sprite("cool_dog",0,-200)
stage.set_background("moon")
object_speed = -2#speed
chocolate = 3
player.set_size(0.1)

#section 2
def falling_object():
    global object_speed,chocolate
    if chocolate >= 1:
        x = random.randint(-200,200)
        y = 250
        object = codesters.Sprite("chocolate", x, y)
        object.set_y_speed(object_speed)
stage.event_interval(falling_object,3)#once every 3 seconds

#section 3
def collision(player, object):
    global chocolate

    if object.get_image_name() == "chocolate":
        stage.remove_sprite(object)
        chocolate -= 1
        if chocolate == 0:
            player.say(f"Oof I got poisoned",5)
        else:
            player.say(f"Ahh I can't eat chocolate",1)

player.event_collision(collision)

#section 4
def go_up():
    global chocolate
    if chocolate > 0:
    
        player.move_up(10)

player.event_key("up", go_up)

def go_down():
    global chocolate
    if chocolate > 0:
    
        player.move_down(10)

player.event_key("down", go_down)

def go_left():
    global chocolate
    if chocolate > 0:

        player.move_left(10)

player.event_key("left", go_left)

def go_right():
    global chocolate
    if chocolate > 0 and player.get_x() < 250:

        player.move_right(10)

player.event_key("right", go_right)