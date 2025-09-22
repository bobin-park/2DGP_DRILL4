from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('images/Woodcutter_attack1.png')

frame=0
for x in range (0,800,10):
    clear_canvas()
    grass.draw(400,30)
    character.clip_draw(frame * 48, 0, 48, 48, x, 300, 400, 400)
    update_canvas()
    frame=(frame+1)%7
    delay(0.05)

close_canvas()