import pygame
import random
pygame.init()
live1=100
live2=100

blanco=(255,255,255)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

listamenu=[0]

screen=pygame.display.set_mode((1000,575))
pygame.display.set_caption("Prototipo I")

fuente= pygame.font.Font(None, 40)
fuente1= pygame.font.Font(None, 80)
t1=fuente.render("mapa", 0 ,(blanco))
t2=fuente.render("music",0,(blanco))
t3=fuente.render("p1",0,(blanco))
t4=fuente.render("p2",0,(blanco))
t5=fuente1.render("DOOM TOWN",0,(blanco))
t6=fuente.render("1,street",0,(blanco))
t7=fuente.render("2,desierto",0,(blanco))
t8=fuente.render("3,oriente",0,(blanco))
t9=fuente.render("4,futuro",0,(blanco))
tt1=fuente1.render("MAPA",0,(blanco))
reloj=pygame.time.Clock()

n=random.randint(0,5)

B1=pygame.image.load("B2.png")
B1= pygame.transform.scale(B1, (150,75))
B2=pygame.image.load("B2.png")
B2= pygame.transform.scale(B2, (150,75))
B3=pygame.image.load("B2.png")
B3= pygame.transform.scale(B3, (150,75))
B4=pygame.image.load("B2.png")
B4= pygame.transform.scale(B4, (150,75))
B5=pygame.image.load("B1.jpg")
B5= pygame.transform.scale(B5, (150,75))

menu1=pygame.image.load("menu6.jpg")
menu2=pygame.image.load("MENU.gif")
menu3=pygame.image.load("MENU2.PNG")
menu4=pygame.image.load("bg7.jpg")
menu5=pygame.image.load("menu5.jpg")
menu6=pygame.image.load("menu3.jpg")
menus=[menu1,menu2,menu3,menu4,menu5,menu6]
menu=menus[n]
menu=pygame.transform.scale(menu, (1000,575))


bg1=pygame.image.load("bg1.jpg")
bg1=pygame.transform.scale(bg1, (1000,575))
bg3=pygame.image.load("bg2.webp")
bg3=pygame.transform.scale(bg3, (1000,575))
bg2=pygame.image.load("bg.jpg")
bg2=pygame.transform.scale(bg2, (1000,575))
bg4=pygame.image.load("bg3.jpg")
bg4=pygame.transform.scale(bg3, (1000,575))
bg5=pygame.image.load("bg4.gif")
bg5=pygame.transform.scale(bg4, (1000,575))
bg6=pygame.image.load("bg6.jpg")
bg6=pygame.transform.scale(bg6, (1000,575))
bg7=pygame.image.load("bg5.jpg")
bg7=pygame.transform.scale(bg7, (1000,575))



walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = bg5
char = pygame.image.load('standing.png')

cal=0
pygame.display.flip();
game=True
factor=True
mecha=False

x=2000
y=1000
vel=10
salto=False
csalto=10
derecha=False
izquierda= False
cwalk=0




def funcion(x):
    A=listamenu[len(listamenu)-1]
    return A





def ventanaso(): #funciones de de ventana
    global cwalk
    if mecha==True:
        screen.fill((0,0,0,0))
        screen.blit(bg,(0,0))


    if cwalk >= 27:
        cwalk=0

    if izquierda:
        screen.blit(walkLeft[cwalk//3],(x,y))
        cwalk += 1

    elif derecha:
        screen.blit(walkRight[cwalk//3],(x,y))
        cwalk += 1
    else:
        screen.blit(char, (x,y))
        cwalk=0

    pygame.display.update()

def accionmenu(x):
    global teclas
    global bg
    if x == 1:
        if teclas[pygame.K_1]:
            bg=bg1

        if teclas[pygame.K_2]:
            bg=bg2


        if teclas[pygame.K_3]:
            bg=bg3


        if teclas[pygame.K_4]:
            bg=bg4


        if teclas[pygame.K_5]:
            bg=bg5


        if teclas[pygame.K_6]:
            bg=bg6


        if teclas[pygame.K_7]:
            bg=bg7





while game:



    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

    vmenu=funcion(listamenu)

    evento = pygame.mouse.get_pressed()
    pos=pygame.mouse.get_pos()
    reloj.tick(27)
    pygame.display.update()

    teclas=pygame.key.get_pressed()
    #print (pos)

    if teclas[pygame.K_p]:
        game=False

    if teclas[pygame.K_0]:
        factor=True
        x=2000
        y=1000
        mecha=False
        listamenu.append(0)

    accionmenu(vmenu)

    if factor==True:
        screen.blit(menu,(0,0))
        screen.blit(B1,(200,250))
        screen.blit(B2,(350,250))
        screen.blit(B3,(500,250))
        screen.blit(B4,(650,250))
        screen.blit(B5,(430,400))
        screen.blit(t1,( 235,270))
        screen.blit(t2,( 385,270))
        screen.blit(t3,( 555,270))
        screen.blit(t4,( 705,270))
        screen.blit(t5,( 350,70))

        if evento[0]:
            if pos[0] >= (230) and pos[1] >= (250) and  pos[0] <= (311) and pos[1]<= 307 :
                factor=False
                print(" haciendo click 1")
                screen.fill((0,0,0,0))
                screen.blit(menu,( 0,0))
                screen.blit(tt1,( 400,100))
                screen.blit(t6,( 300,200))
                screen.blit(t7,( 300,300))
                screen.blit(t8,( 300,400))
                screen.blit(t9,( 300,500))
                listamenu.append(1)


            if pos[0] >= (382) and pos[1] >= (250) and  pos[0] <= (460) and pos[1]<= 307:
                factor=False


                listamenu.append(2)
                screen.fill((0,0,0,0))
                screen.blit(menu,( 0,0))
                screen.blit(t2,( 300,100))
                listamenu.append(2)



            if pos[0] >= (532) and pos[1] >= (255) and  pos[0] <= (610) and pos[1]<= 307:
                factor=False

                listamenu.append(3)
                screen.fill((0,0,0,0))
                screen.blit(menu,( 0,0))
                screen.blit(t3,( 300,100))
                listamenu.append(3)

            if pos[0] >= (682) and pos[1] >= (250) and  pos[0] <= (760) and pos[1]<= 307:
                factor=False

                listamenu.append(4)
                screen.fill((0,0,0,0))
                screen.blit(menu,( 0,0))
                screen.blit(t4,( 300,100))
                print(listamenu)

            if pos[0] >= (430) and pos[1] >= (400) and  pos[0] <= (580) and pos[1]<= 474:
                factor=False
                listamenu.append(0)
                print(" haciendo click 5")
                screen.fill((0,0,0,0))
                screen.blit(bg,( 0,0))
                mecha=True
                x=250
                y=490




    if teclas[pygame.K_LEFT] and x>vel:
        x-=vel
        izquierda = True
        derecha = False
    elif teclas[pygame.K_RIGHT]and x<940 - vel:
        x+=vel
        izquierda = False
        derecha = True
    else:
        derecha = False
        izquierda = False
        cwalk=0


    if not salto:
        if teclas[pygame.K_SPACE]:
            salto=True

    else:
        if csalto>=-10:
            sign=1
            if csalto<0:
                sign=-1
            y -= (csalto**2)*0.5*sign
            csalto -=1
        else:
            salto=False
            csalto=10


    ventanaso()
    pygame.display.update()
    print (mecha)
    print(funcion(vmenu))

pygame.quit()















