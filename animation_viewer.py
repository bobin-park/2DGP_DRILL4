from pico2d import *

open_canvas()
grass = load_image('grass.png')
attackcharacter = load_image('images/Woodcutter_attack1.png')
hurtcharacter = load_image('images/Woodcutter_hurt.png')
idlecharacter = load_image('images/Woodcutter_idle.png')
deathcharacter = load_image('images/Woodcutter_death.png')

motionNum=1 #모션 애니 번호
imageFrame=6 #모션 애니 프레임수
frame=0
if motionNum==1 or motionNum==4:
    imageFrame=6
elif motionNum==2:
    imageFrame=3
elif motionNum==3:
    imageFrame=4
while 1:
    for x in range(0, imageFrame * 6, 1):
        clear_canvas()
        grass.draw(400, 30)
        attackcharacter.clip_draw(frame * 48, 0, 48, 48, 400, 300, 450, 450)
        update_canvas()
        frame = (frame + 1) % 7
        delay(0.05)

close_canvas()