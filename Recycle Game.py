import pygame as py
import time 
py.init()
screen = py.display.set_mode((800, 800))
py.display.set_caption("Recycle Game")


Running = True

bg1 = py.image.load("Banana Waste.jpg")
bg2 = py.image.load("Ceramic Waste.jpg")
bg3 = py.image.load("Crumpled Plastic Bottle.jfif")
bg4 = py.image.load("Glass Recylable Waste.jfif")
bg5 = py.image.load("Used Pizza Box Waste.jpg")
bingreen = py.image.load("green_bin_image-removebg-preview.png")
binblack = py.image.load("Black_Bin-removebg-preview.png")

bg1 = py.transform.scale(bg1,(50, 50))
bg2 = py.transform.scale(bg2,(50, 50))
bg3 = py.transform.scale(bg3,(50, 50))
bg4 = py.transform.scale(bg4,(50, 50))
bg5 = py.transform.scale(bg5,(50, 50))
bingreen = py.transform.scale(bingreen ,(150, 150))
binblack = py.transform.scale(binblack,(150, 150))

bg1sprite = bg1.get_rect()
bg2sprite = bg2.get_rect()
bg3sprite = bg3.get_rect()
bg4sprite = bg4.get_rect()
bg5sprite = bg5.get_rect()
greenbinsprite = bingreen.get_rect()
binblacksprite = binblack.get_rect()

bg1sprite.center = (50, 100)
bg2sprite.center = (150, 100)
bg3sprite.center = (250, 100)
bg4sprite.center = (350, 100)
bg5sprite.center = (450, 100)
greenbinsprite.center = (50, 600)
binblacksprite.center = (500, 600)

dragging_banana = False
dragging_ceramic = False
dragging_bottle = False
dragging_glass =  False
dragging_pizzabox = False
Score = 0
font1 = py.font.SysFont("Arial", 20)


while Running:
    for event in py.event.get():
        if event.type == py.QUIT:
            Running = False
        if event.type == py.MOUSEBUTTONDOWN:
            if bg1sprite.collidepoint(event.pos):
                dragging_banana = True
            if bg2sprite.collidepoint(event.pos):
                dragging_ceramic= True
            if bg3sprite.collidepoint(event.pos):
                dragging_bottle = True
            if bg4sprite.collidepoint(event.pos):
                dragging_glass = True
            if bg5sprite.collidepoint(event.pos):
                dragging_pizzabox = True
        if event.type == py.MOUSEMOTION:
            if dragging_banana == True:
                bg1sprite.center = event.pos
            if dragging_ceramic == True:
                bg2sprite.center = event.pos
            if dragging_bottle == True:
                bg3sprite.center = event.pos
            if dragging_glass == True:
                bg4sprite.center = event.pos
            if dragging_pizzabox == True:
                bg5sprite.center = event.pos
            
        if event.type == py.MOUSEBUTTONUP:
            dragging_banana = False
            dragging_ceramic = False
            dragging_bottle = False
            dragging_glass =  False
            dragging_pizzabox = False

    if bg1sprite.colliderect(greenbinsprite):
        dragging_banana = False
        bg1sprite.center = (1000,1000)
        time.sleep(1)
        Score = Score + 1
    if bg2sprite.colliderect(binblacksprite):
            dragging_ceramic = False
            bg2sprite.center = (1000,1000)
            time.sleep(1)
            Score = Score + 1
    if bg3sprite.colliderect(greenbinsprite):
            dragging_bottle = False
            bg3sprite.center = (1000,1000)
            time.sleep(1)
            Score = Score + 1
    if bg4sprite.colliderect(greenbinsprite):
            dragging_glass =False
            bg4sprite.center = (1000,1000)
            time.sleep(1)
            Score = Score + 1
    if bg5sprite.colliderect(binblacksprite):
            dragging_pizzabox = False
            bg5sprite.center = (1000,1000)
            time.sleep(1)
            Score = Score + 1


            
    if bg1sprite.colliderect(binblacksprite):
            dragging_banana = False
            bg1sprite.center = (1000,1000)
            time.sleep(1)
            Score = Score - 1
    if bg2sprite.colliderect(greenbinsprite):
                dragging_ceramic = False
                bg2sprite.center = (1000,1000)
                time.sleep(1)
                Score = Score - 1
    if bg3sprite.colliderect(binblacksprite):
                dragging_bottle = False
                bg3sprite.center = (1000,1000)
                time.sleep(1)
                Score = Score - 1
    if bg4sprite.colliderect(binblacksprite):
                dragging_glass =False
                bg4sprite.center = (1000,1000)
                time.sleep(1)
                Score = Score - 1
    if bg5sprite.colliderect(greenbinsprite):
                dragging_pizzabox = False
                bg5sprite.center = (1000,1000)
                time.sleep(1)
                Score = Score - 1
    
    
    
    
    screen.fill("White")
    text1 = font1.render("Score: " + str(Score), "black", True)
    screen.blit(text1, (50,50))
   
    screen.blit(bg1, bg1sprite)
    screen.blit(bg2, bg2sprite)
    screen.blit(bg3, bg3sprite)
    screen.blit(bg4, bg4sprite)
    screen.blit(bg5, bg5sprite)
    screen.blit(bingreen, greenbinsprite)
    screen.blit(binblack, binblacksprite)
    py.display.update()
































py.quit()