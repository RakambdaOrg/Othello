'''
@author: Olivier Froger
'''
from tkinter import Tk, Label, Button, Menu, Canvas
from Game import init, getColor, place

def initialisation():
    init()
    refresh()

def refresh():
    for x in range(0, 8):
        for y in range(0, 8):
            placer_pion(getColor(x, y), x, y)

def placer_pion(color, x, y):
    offsetGrid, backgroundColor, borderLineColor = 5, colorVert, "black"
    if color == blanc: backgroundColor = "white"
    elif color == noir: backgroundColor = "black"
    else: borderLineColor = colorVert
    Can.create_oval(gridOffsetCanvas + (x * tailleCase) + offsetGrid, gridOffsetCanvas + (y * tailleCase) + offsetGrid, gridOffsetCanvas + (tailleCase * (x + 1)) - offsetGrid, gridOffsetCanvas + (tailleCase * (y + 1)) - offsetGrid, fill = backgroundColor, outline = borderLineColor)

def mettre_pion(event):
    place(noir, ((event.x) - gridOffsetCanvas) // tailleCase, ((event.y) - gridOffsetCanvas) // tailleCase)
    refresh()

def mettre_pion2(event):
    place(blanc, ((event.x) - gridOffsetCanvas) // tailleCase, ((event.y) - gridOffsetCanvas) // tailleCase)
    refresh()
    
def regles():
    fen1 = Tk()
    fen1.title("Regles du jeu")
    fen1.geometry("500x500")
    fen1.resizable(0, 0)
    fen1.mainloop()

def preferences():
    fen2 = Tk()
    fen2.title("Preferences")
    fen2.geometry("500x500")
    fen2.resizable(0, 0)
    fen2.mainloop()

def a_propos():
    fen3 = Tk()
    fen3.title("A propos de")
    fen3.geometry("500x500")
    fen3.resizable(0, 0)
    fen3.mainloop()

colorVert, blanc, noir, yOffsetCanvas, xOffsetCanvas, gridOffsetCanvas, tailleCase , Comic = "#086126", 1, 2, 2, 8, 25, 50, ("Comic sans MS", "9")

fen = Tk()
fen.title("Othello")
fen.geometry("800x470")
fen.resizable(0, 0)

menubar = Menu(fen)
     
menufichier = Menu(menubar,tearoff=0)
menufichier.add_command(label = "Nouvelle partie", command = initialisation)
menufichier.add_command(label = "Préférences", command = preferences)
menufichier.add_command(label = "Quitter", command = fen.destroy)

menuaide= Menu(menubar,tearoff=0)
menuaide.add_command(label = "Regles du jeu", command=regles)
menuaide.add_command(label = "A propos de",command=a_propos)

menubar.add_cascade(label = "Fichier", menu = menufichier)
menubar.add_cascade(label = "Aide", menu = menuaide)

fen.config(menu = menubar)

Can = Canvas(fen, bg = colorVert, height = 435, width = 435)
Can.place(x = 10, y = 10)
Can.bind("<Button-1>", mettre_pion)
Can.bind("<Button-3>", mettre_pion2)
Label(Can, text = "A", font = Comic, bg = colorVert).place(x = 45, y = yOffsetCanvas)
Label(Can, text = "B", font = Comic, bg = colorVert).place(x = 95, y = yOffsetCanvas)
Label(Can, text = "C", font = Comic, bg = colorVert).place(x = 145, y = yOffsetCanvas)
Label(Can, text = "D", font = Comic, bg = colorVert).place(x = 195, y = yOffsetCanvas)
Label(Can, text = "E", font = Comic, bg = colorVert).place(x = 245, y = yOffsetCanvas)
Label(Can, text = "F", font = Comic, bg = colorVert).place(x = 295, y = yOffsetCanvas)
Label(Can, text = "G", font = Comic, bg = colorVert).place(x = 345, y = yOffsetCanvas)
Label(Can, text = "H", font = Comic, bg = colorVert).place(x = 395, y = yOffsetCanvas)
Label(Can, text = "1", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 40)
Label(Can, text = "2", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 90)
Label(Can, text = "3", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 140)
Label(Can, text = "4", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 190)
Label(Can, text = "5", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 240)
Label(Can, text = "6", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 290)
Label(Can, text = "7", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 340)
Label(Can, text = "8", font = Comic, bg = colorVert).place(x = xOffsetCanvas, y = 390)
Label(fen, text = "Othello", font=  Comic).place(x = 610, y = 5)
x1, x2, y1, y2 = gridOffsetCanvas, gridOffsetCanvas, gridOffsetCanvas, gridOffsetCanvas

for i in range(0, 9):
    Can.create_line(x1, y1, x1 + 400, y1)
    Can.create_line(x2, y2, x2, y2 + 400)
    y1 += tailleCase
    x2 += tailleCase
    
Button(fen, text = "Nouvelle partie", command = initialisation).place(x = 710, y = 1)
chaine = Label(fen)
chaine.place(x = 0, y = 450)

fen.mainloop()