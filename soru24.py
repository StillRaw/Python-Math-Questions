# Klavyeden girilen 2 sayının permütasyonunu hesaplayan yazılımı python dilinde yazınız.
import math
import time


while True:
    x = input("1. sayıyı giriniz: ")
    if x=='q':
        print("Programdan çıktınız!")
        break
    y = input("2. sayıyı giriniz: ")
    if y=='q':
        print("Programdan çıktınız!")
        break
    try:
        print("Hesaplanıyor...")
        fakx=math.factorial(int(x))
        #faky=math.factorial(int(y))
        fakxy=math.factorial(int(x)-int(y))
        per=int(fakx / fakxy)
        time.sleep(1)
        print("{} sayısının {} sayısıyla permütasyonu: {}".format(x,y,per))
    except ValueError:
        print("Lütfen uygun format kullanınız! (1.sayı > 2.sayı olmalı.)")
   