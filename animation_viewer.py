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
    imageFrame=7
elif motionNum==2:
    imageFrame=4
elif motionNum==3:
    imageFrame=3
while 1:
    for x in range(0, imageFrame * 5, 1):
        clear_canvas()
        grass.draw(400, 30)
        if(motionNum==1):
            attackcharacter.clip_draw(frame * 48, 0, 48, 48, 400, 300, 450, 450)
        elif(motionNum==2):
            hurtcharacter.clip_draw(frame * 48, 0, 48, 48, 400, 300, 450, 450)
        elif (motionNum == 3):
            idlecharacter.clip_draw(frame * 48, 0, 48, 48, 400, 300, 450, 450)
        elif (motionNum == 4):
            deathcharacter.clip_draw(frame * 48, 0, 48, 48, 400, 300, 450, 450)
        update_canvas()
        frame = (frame + 1) % imageFrame
        delay(0.05)
    if(motionNum>=4):
        motionNum=1
    else:
        motionNum = motionNum+1