#1000'den küçük asal sayıları ekrana yazdıran ve bu sayıların toplamını bulan yazılımı python dilinde yazınız.

#NOT: Ben bunu daha esnek olsun diye girilen değere karşılık 
#asal sayıların listelemesi ve toplamı olarak değiştirdim.
import math
x=int(input("Lütfen bir sayı giriniz:"))

liste=[2,3]
for i in range(5,x,2):
    a=math.floor(i**0.5)        #Burası biraz matematik kokuyor:)
    for j in range(3,a+3,2):
        if (i % j == 0):
            break
    if(i % j != 0):
        liste.append(i)

print("{} sayısından küçük asal sayılar= {}".format(x,liste))
toplam= sum(liste)
print("{} sayısından küçük asal sayıların toplamı: {}".format(x,toplam))

