# Klavyeden girilen 2 sayının combinasyonunu hesaplayan yazılımı python dilinde yazınız.
import math


while True:
    x = input("1. sayıyı giriniz: ")
    if x=='q':
        break
    y = input("2. sayıyı giriniz: ")
    if y=='q':
        break
    try:
        fakx=math.factorial(int(x))
        faky=math.factorial(int(y))
        fakxy=math.factorial(int(x)-int(y))
        kom=int(fakx / (faky*fakxy))
        print("{} sayısının {} sayısıyla kombinasyonu: {}".format(x,y,kom))
    except ValueError:
        print("Lütfen uygun format kullanınız! (1.sayı > 2.sayı olmalı.)")
   