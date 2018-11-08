##Hey Ashish, Everything Runs
import pygame
import math
import random
pygame.init()
black=[0,0,0] ##colors
red=[255,0,0]
redLight=[255,0,0]
green=[0,255,0]
greenLight=[0,255,0]
blue=[0,0,255]
white=[255,255,255]
yellow=[255,255,0]
purple=[255,0,255]
lgreen=[102,209,114]
brown=[104,94,49]
dgreen=[29,180,30]
gray=[153,153,153]
pi=math.pi
font=pygame.font.Font (None, 50)
text = font.render("Happy Holidays", True, red)
pos_list=[]
vectorList=[]
smV=[]
smP=[]
smSize=[]
wind=[]
sizeList=[]
countList=[]
count=0
roofCount=0
shedx=0
shedy=0
change=0
changeDirec=0.5
roof=False 
smokeList=[]
for i in range(0,random.randint(15,20)):
    smokeList.append([[470+random.randint(-20,20),570+random.randint(-10,10)],random.randint(5,15)])
for i in range(0,50):
    x=random.randint(450,490)
    y=random.randint(560,580)
    rise=random.randint(-3,-1)
    size=random.randint(5,10)
    smP.append([x,y])
    smV.append(rise)
    smSize.append(size)
size=[800,800]
def smoke(pos,rise,size):
    pos[1]=pos[1]+rise
    pos[0]=pos[0]+random.randint(1,2)
    if pos[1]<0:
        pos[1]=random.randint(560,580)
        pos[0]=random.randint(450,490)
        rise=random.randint(-3,-1)
    pygame.draw.circle(screen,gray,pos,size)
lightPos=[]
def drawHouse():
    pygame.draw.rect(screen,lgreen,[300,650,200,150])
    pygame.draw.rect(screen,black,[450,580,20,40])
    pygame.draw.polygon(screen,brown,[[270,650],[400,575],[530,650]])
    pygame.draw.rect(screen,brown,[425,720,50,80])
    pygame.draw.rect(screen,yellow,[325,710,70,50])
    pygame.draw.rect(screen,brown,[325,710,70,50],3)
    pygame.draw.circle(screen,dgreen,[450,740],15,8)
def drawSnow(posList,size):
    pygame.draw.circle(screen,white,posList,size)
def snowFall():
    global count
    countList[i][1]=countList[i][1]+(sizeList[i]/2)
    count=count+.004
    global roofCount
    roofCount+=0.003
    pos_list[i][1]=random.randint(-20,-10)
    sizeList[i]=random.randint(2,5)
    vectorList[i]=random.randint(3,10)
    wind[i]=random.randint(-2,2)
def lightDraw(color,pos):
    global change
    global changeDirec
    change=change+changeDirec
    changeColor=int(change)
    if changeColor>255 or changeColor<0:
        changeDirec=changeDirec*-1
        change=change+changeDirec
        changeColor=int(change)
    displayColor=color
    if displayColor[0]>displayColor[1]:
        displayColor[0]=displayColor[0]-changeColor
        displayColor[1]=255-displayColor[0]
    else:
        displayColor[1]=displayColor[1]-changeColor
        displayColor[0]=255-displayColor[1]
    if displayColor[1]<=255 and displayColor[1]>=0:
        pygame.draw.circle(screen,displayColor,pos,5)
    else:
        pygame.draw.circle(screen,green,pos,5)
    displayColor=[]
for i in range(0,300):
    x=random.randint(1,800)
    y=random.randint(-700,0)
    #y=random.randint(-20,0)
    pos_list.append([x,y])
    countList.append([x,0])
for i in range (0,10):
    lightPos.append([int((270+(i*8*1.75))),int((650-i*8))])
    lightPos.append([int((400+(i*8*1.75))),int((575+i*8))])
    
    
screen=pygame.display.set_mode(size)
screen.fill(blue)
pygame.display.set_caption("Happy Holidays")
for i in range (0,len(pos_list)):
   vectorList.append(random.randint(3,7))
   wind.append(random.randint(-1,1))
   sizeList.append(random.randint(2,5))
clock=pygame.time.Clock()
done=False
zero=False
while done==False:
    clock.tick(30)
    screen.fill(blue)
    for i in range (0,len(smP)):
            smoke(smP[i],smV[i],smSize[i])
    for i in range (len(pos_list)):
        if pos_list[i][1]>800:
            snowFall()
        drawSnow(pos_list[i],sizeList[i])
        #pos_list[i][0]=pos_list[i][0]+wind[i]
        pos_list[i][1]=pos_list[i][1]+vectorList[i]
        pygame.draw.rect(screen,white,[0,800-int(count),800,int(count)])
        pygame.draw.ellipse(screen,white,[countList[i][0]-30,int(800-int(countList[i][1])),(int(countList[i][1]*1.75)),int(countList[i][1])])
        drawHouse()
        if roofCount <=10:
            pygame.draw.line(screen,white,[270,650],[400,575],int(roofCount))
            pygame.draw.line(screen,white,[400,575],[530,650],int(roofCount))
        else:
            shedx=shedx+0.01354166666666666666666666666667
            shedy=shedy+0.0078125
            pygame.draw.line(screen,white,[270,650],[400-(shedx),575+(shedy)],int(roofCount))
            pygame.draw.line(screen,white,[400+(shedx),575+shedy],[530,650],int(roofCount))
            pygame.draw.rect(screen,white,[270,650,(roofCount)/4,shedy*4])
            pygame.draw.rect(screen,white,[530,650,(roofCount)/4,shedy*4])
            if shedy >=75:
                roofCount=0
                shedx=0
                shedy=0
                roof=True
            if zero==True and i==len(pos_list)-1:
              roof=False
    for i in range(0,len(lightPos)):
        if i%2==1:
            lightDraw(redLight,lightPos[i])
        else:
            lightDraw(greenLight,lightPos[i])
    screen.blit(text,[275,100])
    pygame.display.flip()
    for event in pygame.event.get(): ##checks the giant list of events 
        if event.type==pygame.QUIT: ##handles quit event
            done=True
pygame.quit()##ends pygame to make it idlefriendly
