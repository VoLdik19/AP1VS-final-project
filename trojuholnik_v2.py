"""Trojúhelník, výpočty a vykreslení."""
import tkinter as tk
from tkinter import Frame, N, E, NW, Label, W
from math import degrees, acos

root = tk.Tk()

frame = Frame(root)
frame.grid(row=0, column=0, sticky=N)
frame2 = Frame(root)
frame2.grid(row=0, column=0, sticky=E)

"""Vytvorí pole pre zadanie údajov"""
a_x = tk.Entry(frame, width=18)
a_y = tk.Entry(frame, width=18)

b_x = tk.Entry(frame, width=18)
b_y = tk.Entry(frame, width=18)

c_x = tk.Entry(frame, width=18)
c_y = tk.Entry(frame, width=18)


def data():
    """Vygenerovanie tabuliek pre zápis údajov."""
    Label(frame, text="Číslo nesmie presiahnúť 500 \n a musí byť 3 ciferné!") \
        .grid(row=0, column=0, columnspan=10, sticky=N)
    Label(frame, text="X").grid(row=1, column=1, sticky=N)
    Label(frame, text="Y").grid(row=1, column=2, sticky=N)

    Label(frame, text="Bod A:").grid(row=2, column=0, sticky=NW)
    a_x.grid(row=2, column=1, sticky=W)
    a_y.grid(row=2, column=2, sticky=W)
    Label(frame, text="Bod B:").grid(row=4, column=0, sticky=NW)
    b_x.grid(row=4, column=1, sticky=W)
    b_y.grid(row=4, column=2, sticky=W)
    Label(frame, text="Bod C:").grid(row=6, column=0, sticky=NW)
    c_x.grid(row=6, column=1, sticky=W)
    c_y.grid(row=6, column=2, sticky=W)

    tk.Button(frame, text='Nakresli', command=checkWrongData, width=15) \
        .grid(row=8, column=1, columnspan=2, rowspan=2, sticky=N)
    """Vygenerovanie tlačítka na spustenie výpočtov a vakreslovania"""


def strana(a1, a2, b1, b2):
    """Kontrola a výpočet stran."""
    if type(a1) not in [int, float]:
        raise TypeError("Musí byť číslo")
    if type(a2) not in [int, float]:
        raise TypeError("Musí byť číslo")
    if type(b1) not in [int, float]:
        raise TypeError("Musí byť číslo")
    if type(b2) not in [int, float]:
        raise TypeError("Musí byť číslo")
    return (((a1 - b1) ** 2 + (a2 - b2) ** 2) ** (1 / 2))
    """Metoda vrátí délku stran."""


def checkWrongData():
    """Vyprázdneni pole."""
    labelA1 = Label(frame, text="                                  ",
                    fg="#FF0000", font="Helvetica 8 bold")
    labelA1.grid(row=3, column=1)

    labelA2 = Label(frame, text="                                  ",
                    fg="#FF0000", font="Helvetica 8 bold")
    labelA2.grid(row=3, column=2)

    labelB1 = Label(frame, text="                                  ",
                    fg="#FF0000", font="Helvetica 8 bold")
    labelB1.grid(row=5, column=1)

    labelB2 = Label(frame, text="                                  ",
                    fg="#FF0000", font="Helvetica 8 bold")
    labelB2.grid(row=5, column=2)

    labelC1 = Label(frame, text="                                  ",
                    fg="#FF0000", font="Helvetica 8 bold")
    labelC1.grid(row=7, column=1)

    labelC2 = Label(frame, text="                                  ",
                    fg="#FF0000", font="Helvetica 8 bold")
    labelC2.grid(row=7, column=2)

    """Zadani promenne."""
    aa = 0
    ab = 0
    ba = 0
    bb = 0
    ca = 0
    cb = 0

    global a1
    """Overenie zadaných údajov pre a1"""
    if len(a_x.get()) <= 3:
        if a_x.get().isdigit() and int(a_x.get()) <= 500:
            a1 = int(a_x.get())
            aa = 1
        else:
            labelA1.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelA1.config(text="↑ Priveľa znakov! ↑")

    global a2
    """Overenie zadaných údajov pre a2"""
    if len(a_y.get()) <= 3:
        if a_y.get().isdigit() and int(a_y.get()) <= 500:
            a2 = int(a_y.get())
            ab = 1
        else:
            labelA2.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelA2.config(text="↑ Priveľa znakov! ↑")

    global b1
    """Overenie zadaných údajov pre b1"""
    if len(b_x.get()) <= 3:
        if b_x.get().isdigit() and int(b_x.get()) <= 500:
            b1 = int(b_x.get())
            ba = 1
        else:
            labelB1.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelB1.config(text="↑ Priveľa znakov! ↑")

    global b2
    """Overenie zadaných údajov pre b2"""
    if len(b_y.get()) <= 3:
        if b_y.get().isdigit() and int(b_y.get()) <= 500:
            b2 = int(b_y.get())
            bb = 1
        else:
            labelB2.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelB2.config(text="↑ Priveľa znakov! ↑")

    global c1
    """Overenie zadaných údajov pre c1"""
    if len(c_x.get()) <= 3:
        if c_x.get().isdigit() and int(c_x.get()) <= 500:
            c1 = int(c_x.get())
            ca = 1
        else:
            labelC1.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelC1.config(text="↑ Priveľa znakov! ↑")

    global c2
    """Overenie zadaných údajov pre c2"""
    if len(c_y.get()) <= 3:
        if c_y.get().isdigit() and int(c_y.get()) <= 500:
            c2 = int(c_y.get())
            cb = 1
        else:
            labelC2.config(text="↑ Nesprávny údaj! ↑")
    else:
        labelC2.config(text="↑ Priveľa znakov! ↑")

    if aa == 1 and ab == 1 and ba == 1 and bb == 1 and ca == 1 and cb == 1:
        vypis_vypocet()
    else:
        data()


def vypis_vypocet():
    """Globalizovaní a zaokrouhlení strany A."""
    global strana_A
    strana_A = strana(b1, b2, c1, c2)
    strana_A = round(strana_A, 2)

    """Globalizovaní a zaokrouhlení strany B."""
    global strana_B
    strana_B = strana(c1, c2, a1, a2)
    strana_B = round(strana_B, 2)

    """Globalizovaní a zaokrouhlení strany C."""
    global strana_C
    strana_C = strana(a1, a2, b1, b2)
    strana_C = round(strana_C, 2)

    if (strana_A + strana_B > strana_C and strana_B + strana_C > strana_A and
            strana_A + strana_C > strana_B):
        Label(frame, text=("  Trojuholník sa dá narýsovať  "),
              font="Helvetica 15 bold", fg="white")\
                  .grid(row=10, column=1, columnspan=2, sticky=N)

        """Výpis súradnic na kanvas"""
        Label(frame2, text="Súradnice:",
              font="Helvetica 12 bold").grid(row=0, column=0, sticky=N)
        Label(frame2, text=("Bod A má súradnice X: " + str(a1)+" Y: "+str(a2)),
              font="Helvetica 10").grid(row=1, column=0, sticky=W)
        Label(frame2, text=("Bod B má súradnice X: " + str(b1)+" Y: "+str(b2)),
              font="Helvetica 10").grid(row=2, column=0, sticky=W)
        Label(frame2, text=("Bod C má súradnice X: " + str(c1)+" Y: "+str(c2)),
              font="Helvetica 10").grid(row=3, column=0, sticky=W)

        """Výpis strán na kanvas"""
        Label(frame2, text="Strany:", font="Helvetica 12 bold")\
            .grid(row=0, column=1, sticky=N)
        Label(frame2, text=("Strana A je dlhá: "+str(strana_A)+" cm"),
              font="Helvetica 10").grid(row=1, column=1, sticky=W)
        Label(frame2, text=("Strana B je dlhá: "+str(strana_B)+" cm"),
              font="Helvetica 10").grid(row=2, column=1, sticky=W)
        Label(frame2, text=("Strana C je dlhá: "+str(strana_C)+" cm"),
              font="Helvetica 10").grid(row=3, column=1, sticky=W)

        """globalizovanie obvodu na kanvas"""
        global obvod
        obvod = obvod_Stran(strana_A, strana_B, strana_C)
        obvod = round(obvod, 2)

        """globalizovanie obsahu na kanvas"""
        global obsah
        obsah = Obsah_Trojuholnika(strana_A, strana_B, strana_C)
        obsah = round(obsah, 2)

        """Výpis obvodu a obsahu na kanvas"""
        Label(frame2, text="Výpočty:", font="Helvetica 12 bold")\
            .grid(row=0, column=2, sticky=N)
        Label(frame2, text=("Obsah trojuholníka sa rovná: "+str(obsah)+" cm²"),
              font="Helvetica 10").grid(row=1, column=2, sticky=W)
        Label(frame2, text=("Obvod trojuholníka sa rovná: "+str(obvod)+" cm"),
              font="Helvetica 10").grid(row=2, column=2, sticky=W)
        Label(frame2, text=(str(pravouhlost())),
              font="Helvetica 10").grid(row=3, column=2, sticky=W)
        kresba()
    else:
        Label(frame, text=("Trojuholník sa nedá narýsovať"),
              font="Helvetica 12 bold", fg="red")\
                  .grid(row=10, column=0, columnspan=10, sticky=N)


def obvod_Stran(strana_A, strana_B, strana_C):
    """Vypocet obvodu trojuholnika.

    :param strana_A: vstupní parameter strana A.
    :param strana_B: vstupní parameter strana B.
    :param strana_C: vstupní parameter strana C.
    :return: Vrátí jejich součet- obvod.

    ukázka použití:
    >>> obvod_Stran(1,2,3)
    6

    """
    return strana_A + strana_B + strana_C


def Obsah_Trojuholnika(strana_A, strana_B, strana_C):
    """Výpočet obsahu trojuholnika.

    :param strana_A: vstupní parameter strana A.
    :param strana_B: vstupní parameter strana B.
    :param strana_C: vstupní parameter strana C.
    :return: Vrátí obsah.
    """
    s = (strana_A + strana_B + strana_C)/2
    """Definovanie s ako polovica suctu stran"""
    obsah = ((s*(s-strana_A)*(s-strana_B)*(s-strana_C))**(1/2))
    """Vypocita obsah"""
    return obsah


def pravouhlost():
    """Vstupní parametry jsou úhly."""
    """Vypis pravouhlosti"""
    if ((uhol(a1, a2, b1, b2, c1, c2) == 90.00000000000001) or
        (uhol(a1, a2, b1, b2, c1, c2) == 90.0) or
        (uhol(a1, a2, b1, b2, c1, c2) == 89.99999999999999) or
        (uhol(c1, c2, a1, a2, b1, b2) == 90.00000000000001) or
        (uhol(c1, c2, a1, a2, b1, b2) == 90.0) or
        (uhol(c1, c2, a1, a2, b1, b2) == 89.99999999999999) or
        (uhol(b1, b2, c1, c2, a1, a2) == 90.00000000000001) or
        (uhol(b1, b2, c1, c2, a1, a2) == 90.0) or
            (uhol(b1, b2, c1, c2, a1, a2) == 89.99999999999999)):
        return ("Trojuholnik je pravouhly")
    else:
        return ("Trojuholnik nie je pravouhly")
    """Vypíše jestli je nebo není pravoúhlý."""


def uhol(a1, a2, b1, b2, c1, c2):
    """Vstupní parametry jsou X a Y souřadnice bodů."""
    """Vypocet uhlov v stupnoch"""
    A = strana(b1, b2, c1, c2)
    """Definuje stranu A"""
    B = strana(c1, c2, a1, a2)
    """Definuje stranu B"""
    C = strana(a1, a2, b1, b2)
    """Definuje stranu c"""
    return degrees(acos((A * A + B * B - C * C)/(2.0 * A * B)))
    """Vrati uhol v stupnoch"""


def kresba():
    """Nadefinuje rozměry a rozmiestnenie canvasu."""
    udaje = tk.Canvas(root, width=500, height=500, background='#c4c4c4')
    udaje.grid(row=0, column=1, columnspan=5)

    """Narýsuje trojúhelník"""
    udaje.create_line(a1, a2, b1, b2, fill="blue", width=5)
    udaje.create_line(b1, b2, c1, c2, fill="blue", width=5)
    udaje.create_line(c1, c2, a1, a2, fill="blue", width=5)

    """pomenovanie bodov"""
    udaje.create_text(a1-20, a2-20, fill="black",
                      font="Times 20", text="A", anchor="w")
    udaje.create_text(b1+20, b2-20, fill="black",
                      font="Times 20", text="B", anchor="w")
    udaje.create_text(c1-20, c2+20, fill="black",
                      font="Times 20", text="C", anchor="w")

    """pomenovanie stran"""
    udaje.create_text((a1+b1)/2, (a2+b2)/2, fill="red",
                      font="Times 20 bold", text="c", anchor="w")
    udaje.create_text((b1+c1)/2, (b2+c2)/2, fill="red",
                      font="Times 20 bold", text="a", anchor="w")
    udaje.create_text((a1+c1)/2, (a2+c2)/2, fill="red",
                      font="Times 20 bold", text="b", anchor="w")


data()

"""odkazuje na main loop canvasu"""
root.mainloop()
