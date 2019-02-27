# 10'dan küçük asal sayıların toplamı 2 + 3 + 5 + 7 = 17'dir.
# 2 milyondan küçük bütün asal sayıların toplamını bulan yazılımı python dilinde yazınız.
import math
print("""                        
                        ASAL SAYI TOPLAMI HESAPLAMA
_________________________________________________________________________________
Açıklama: 10'dan küçük asal sayıların toplamı 2 + 3 + 5 + 7 = 17'dir.

Amaç:     Bu programda girilen bir değerden küçük asal sayıları ekrana yazdırıp,
          bu sayıların toplamını bulacağız.

                                                          created by Onur Gülşin®
_________________________________________________________________________________""")   
x=int(input("Lütfen bir sayı giriniz:"))

liste=[2,3]
for i in range(5,x,2):
    a=math.floor(i**0.5)
    for j in range(3,a+3,2):
        if (i % j == 0):
            break
    if(i % j != 0):
        liste.append(i)

print("{} sayısından küçük asal sayılar= {}".format(x,liste))
toplam= sum(liste)
print("{} sayısından küçük asal sayıların toplamı: {}".format(x,toplam))
