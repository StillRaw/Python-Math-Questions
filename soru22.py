#İlk 6 asal asal sayıyı listelersek(2, 3, 5, 7, 11 ve 13) 6. asal sayının 13 olduğunu görürüz.
# 1923. asal sayıyı hesaplayan yazılımı python dilinde yazınız.

import math
print("""                        
                        ASAL SAYI TOPLAMI HESAPLAMA
_________________________________________________________________________________
Açıklama: İlk 6 asal asal sayıyı listelersek;
            (2, 3, 5, 7, 11 ve 13) ve 6. asal sayının 13 olduğunu görürüz.

Amaç:     Bu programda girilen bir değere karşılık gelen asal sayıyı bulup, 
          o asal sayıya kadar olan asal sayıları ekrana yazdıracağız.

                                                          created by Onur Gülşin®
_________________________________________________________________________________""")   
x=int(input("Kaçıncı asal sayıyı öğrenmek istiyosunuz?"))

liste=[2,3]

for i in range(5,x**2,2):
    if (len(liste) == x):
        break
    a=math.floor(i**0.5)
    for j in range(3,a+3,2):
        if (i % j == 0):
            break
    if(i % j != 0):
        liste.append(i)


print("{} sayısından küçük asal sayılar= {}".format(x,liste))
print("{}. asal sayı: {}".format(x,liste[x-1]))

