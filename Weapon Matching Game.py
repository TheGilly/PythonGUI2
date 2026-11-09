import pygame as py
py.init()

Screen = py.display.set_mode((800, 800))
py.display.set_caption("Weapon Matching Game")
font1 = py.font.SysFont("Calibri", 50)
text1 = font1.render("Match the charachtar to the weapons", True, "black")

Ninja = py.image.load("Ninja Image.jpg")
Ninja = py.transform.scale(Ninja, (150, 150))
NinjaSprite = Ninja.get_rect()
NinjaSprite.center = (100, 100)

Archer = py.image.load("Archer Image.jpg")
Archer = py.transform.scale(Archer, (150, 150))
ArcherSprite = Archer.get_rect()
ArcherSprite.center = (100, 300)

Wizard = py.image.load("Wizard Image.jpg")
Wizard = py.transform.scale(Wizard, (150, 150))
WizardSprite = Wizard.get_rect()
WizardSprite.center = (100, 500)

Katana = py.image.load("Ninja Katana Image.jpg")
Katana = py.transform.scale(Katana, (150, 150))
KatanaSprite = Katana.get_rect()
KatanaSprite.center = (600, 300)

Bow = py.image.load("Bow and Arrow Image.jpg")
Bow = py.transform.scale(Bow, (150, 150))
BowSprite = Bow.get_rect()
BowSprite.center = (600, 500)

Staff = py.image.load("Wizard Staff Image.jpg")
Staff = py.transform.scale(Staff, (150, 150))
StaffSprite = Staff.get_rect()
StaffSprite.center = (600, 100)


Running = True

nk = False
ns = False
nb = False
ak = False
ab = False
AS  = False
wk  = False
ws  = False
wb = False

Line1 = False
Line2 = False
Line3 = False

while Running:
    for event in py.event.get():
        if event.type == py.QUIT:
            Running = False
        if event.type == py.MOUSEBUTTONDOWN:
            if NinjaSprite.collidepoint(event.pos) and Line1 == False:
                
                nk = True
                ns = True
                nb = True
            if ArcherSprite.collidepoint(event.pos) and Line2 == False:
                
                ak = True
                AS = True
                ab = True
            if WizardSprite.collidepoint(event.pos) and Line3 == False:
               
                wk = True
                ws = True
                wb = True
        if event.type==py.MOUSEBUTTONUP:
            if KatanaSprite.collidepoint(event.pos):
                if nk:
                    Line1 =True
                    ns=False
                    nb=False
                    ak=False
                    wk=False
                    
                    print("ninja line stops")

                if ak:
                    nk=False
                    wk=False
                    ab=False
                    AS=False

                    Line2=True
                    print("archer line stops")


                if wk:
                    wb=False
                    ws=False
                    nk=False
                    ak=False

                    Line3=True
                    print("wizard line stops")
#bow
            if BowSprite.collidepoint(event.pos):
                if nb:
                    Line1=True
                    nk=False
                    ns=False
                    ab=False
                    wb=False
                    
                    print("ninja line stops")

                if ab:
                    nb=False
                    wb=False
                    AS=False
                    ak=False

                    Line2=True
                    print("archer line stops")


                if wb:
                    ws=False
                    wk=False
                    nb=False
                    ab=False

                    Line3=True
                    print("wizard line stops")

            if StaffSprite.collidepoint(event.pos):
                if ns:
                    Line1=True
                    nk=False
                    nb=False
                    AS=False
                    ws=False
                    
                    print("ninja line stops")

                if AS:
                    ns=False
                    ws=False
                    ak=False
                    ab=False

                    Line2=True
                    print("archer line stops")


                if ws:
                    wb=False
                    wk=False
                    ns=False
                    AS=False

                    Line3=True
                    print("wizard line stops")


    
            

    Screen.fill("white")
    if Line1 == True:
        if nk:
            py.draw.line(Screen, (0, 0, 255), NinjaSprite.center, KatanaSprite.center, width = 2)
        if ns:
            py.draw.line(Screen, (0, 0, 255), NinjaSprite.center, StaffSprite.center, width = 2)
        if nb:
            py.draw.line(Screen, (0, 0, 255), NinjaSprite.center, BowSprite.center, width = 2)

    if Line2 == True:
        if ak:
            py.draw.line(Screen, (0, 0, 255), ArcherSprite.center, KatanaSprite.center, width = 2)
        if AS:
            py.draw.line(Screen, (0, 0, 255), ArcherSprite.center, StaffSprite.center, width = 2)
        if ab:
            py.draw.line(Screen, (0, 0, 255), ArcherSprite.center, BowSprite.center, width = 2)
    
    if Line3 == True:
        if wk:
            py.draw.line(Screen, (0, 0, 255), WizardSprite.center, KatanaSprite.center, width = 2)
        if ws:
            py.draw.line(Screen, (0, 0, 255), WizardSprite.center, StaffSprite.center, width = 2)
        if wb:
            py.draw.line(Screen, (0, 0, 255), WizardSprite.center, BowSprite.center, width = 2)


    if Line1 and Line2 and Line3:
        if nk and ab and ws:
            text2 = font1.render("You did it correct!", True, "black")
        else:
            text2 = font1.render("You did it incorrect", True, "black")








    
    Screen.blit(Ninja, NinjaSprite)
    Screen.blit(Archer, ArcherSprite)
    Screen.blit(Wizard, WizardSprite)
    Screen.blit(Katana, KatanaSprite)
    Screen.blit(Bow, BowSprite)
    Screen.blit(Staff, StaffSprite)
    Screen.blit(text1)
    if Line1 and Line2 and Line3:
        Screen.blit(text2, (100, 200))

    py.display.update()

    














































py.quit()
