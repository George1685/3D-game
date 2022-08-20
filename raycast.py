from display import *
from copy import deepcopy
from math import *
obj_x1 = [[-1,-1,0,1,1,1]]
obj_y1 = [[-1,-1,0,1,1,1]]
obj_z1 = [[-1,-1,0,1,1,1]]
obj_x2 = [[-1,-1,0,1,1,1]]
obj_y2 = [[-1,-1,0,1,1,1]]
obj_z2 = [[-1,-1,0,1,1,1]]
fov = 120
x = 0
y = 0
z = 1
UP = 1073741906
DOWN = 1073741905
LEFT = 1073741904
RIGHT = 1073741903
font = pg.font.Font(None, 26)
bgcolor = 50, 50, 50

def mainloop(): #Raycast infinity loop
    global x,y,z,screen,font
    anti_disp= []
    while 1:
        z -= 0.1
        for ev in pg.event.get():
            if ev.type == pg.KEYDOWN:
                if ev.key == UP:
                    x += 1
                if ev.key == DOWN:
                    x -= 1
                if ev.key == LEFT:
                    y -= 1
                if ev.key == RIGHT:
                    y += 1
                if ev.key == 32:
                    z += 75000
            if ev.type == pg.QUIT:
                break
            z = int(z*10)/10
            text = str(x)+", "+str(y)+", "+str(z//25000)
            img = font.render(text, 1, (155, 155, 155), (0, 0, 0))
            pa = pg.PixelArray(img)
            ans = []
            disp(anti_disp)
            anti_disp= []
            for i in range(len(pa)):
                for j in range(len(pa[0])):
                    ans.append([i,j,pa[i][j]])
                    anti_disp.append([i,j,(0,0,0)])
            disp(ans)
mainloop()
