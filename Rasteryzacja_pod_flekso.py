from PIL import Image
import math

width = 2560
height = 1620
im = Image.open("Gierymski_czarno_biale.png")
im_pix = im.load()
# im.show()
# img.show()


def rasteryzacja_punktu(obraz, x, y, rozmiar_punktu, procent):
    procent = 1-(procent/255)
    promien = (rozmiar_punktu[-1]*procent*1.42)/2
    srodek = rozmiar_punktu[-1]/2
    for y_m in rozmiar_punktu:
        for x_m in rozmiar_punktu:
            a = y_m - srodek
            b = x_m - srodek
            c = math.sqrt(a*a+b*b)
            if c < promien:
                obraz[x+x_m, y+y_m] = (0, 0, 0)
            else:
                obraz[x + x_m, y + y_m] = (255, 255, 255)


def rasteryzacja_obrazu(bok_rastru, szer, wys, obraz, obraz_pix):
    br = bok_rastru
    br_range = range(br)
    krok_szer = range(0, szer-1, br)
    krok_wys = range(0, wys-1, br)
    for y in krok_wys:
        for x in krok_szer:
            procent_rastra = 0
            for y_m in br_range:
                for x_m in br_range:
                    procent_rastra = procent_rastra + obraz.getpixel((x_m+x, y_m+y))[0]
            procent_rastra = round(procent_rastra/(bok_rastru*bok_rastru))
            rasteryzacja_punktu(obraz_pix, x, y, br_range, procent_rastra)
    obraz.save('Wersja_robocza.png')


rasteryzacja_obrazu(20, width, height, im, im_pix)
