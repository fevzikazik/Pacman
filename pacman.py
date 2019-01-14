from random import choice
from turtle import *
from freegames import floor, vector
title('PACMAN')

durum = {'skor': 0}
yol = Turtle(visible=False)
skorTablosu = Turtle(visible=False)
yonelim = vector(0, 0)
pacman = vector(-40, -80)
hayaletler = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]
fayanslar = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

def kareCiz(x, y):
    "Draw square using path at (x, y)."
    yol.up()
    yol.goto(x, y)
    yol.down()
    yol.begin_fill()

    for sayac in range(4):
        yol.forward(20)
        yol.left(90)

    yol.end_fill()

def yemOlustur(konum):
    "Return offset of point in tiles."
    x = (floor(konum.x, 20) + 200) / 20
    y = (180 - floor(konum.y, 20)) / 20
    index = int(x + y * 20)
    return index

def uygunYol(konum):
    "Return True if point is valid in tiles."
    index = yemOlustur(konum)

    if fayanslar[index] == 0:
        return False

    index = yemOlustur(konum + 19)

    if fayanslar[index] == 0:
        return False

    return konum.x % 20 == 0 or konum.y % 20 == 0

def oyunAlani():
    bgcolor('black')
    yol.color('blue')

    for index in range(len(fayanslar)):
        fayans = fayanslar[index]

        if fayans > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            kareCiz(x, y)

            if fayans == 1:
                yol.up()
                yol.goto(x + 10, y + 10)
                yol.dot(2, 'white')

def hareketEt():
    "Move pacman and all ghosts."
    skorTablosu.undo()
    skorTablosu.write(durum['skor'])

    clear()


    if uygunYol(pacman + yonelim):
        pacman.move(yonelim)

    index = yemOlustur(pacman)

    if fayanslar[index] == 1:
        fayanslar[index] = 2
        durum['skor'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        kareCiz(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')

    for konum, rota in hayaletler:
        if uygunYol(konum + rota):
            konum.move(rota)
        else:
            rotalar = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            rotaDene = choice(rotalar)
            rota.x = rotaDene.x
            rota.y = rotaDene.y

        up()
        goto(konum.x + 10, konum.y + 10)
        dot(20, 'red')

    update()

    for konum, rota in hayaletler:
        if abs(pacman - konum) < 20:
            print("Kaybettin")
            return

    ontimer(hareketEt, 100)

def yonDegistir(x, y):
    "Change pacman aim if valid."
    if uygunYol(pacman + vector(x, y)):
        yonelim.x = x
        yonelim.y = y

setup(420, 420)
hideturtle()
tracer(False)

skorTablosu.goto(160, 160)
skorTablosu.color('white')
skorTablosu.write(durum['skor'])

listen()
onkey(lambda: yonDegistir(5, 0), 'Right')
onkey(lambda: yonDegistir(-5, 0), 'Left')
onkey(lambda: yonDegistir(0, 5), 'Up')
onkey(lambda: yonDegistir(0, -5), 'Down')

oyunAlani()
hareketEt()

done()
