#Bir sayı, pozitif tam bölenlerinin adedine de tam bölünüyorsa bu sayıya “Tau Sayısı” denir.
# Örnek: 24’ün pozitif tam bölenleri: 1, 2, 3, 4, 6, 8, 12, 24 => 8 adet tam böleni mevcut.
# 24 sayısı 8'e tam bölündüğü için 24 sayısı bir Tau Sayısıdır.
# Klavyeden girilen sayının Tau Sayısı olup olmadığını tespit eden yazılımı 
# python dilinde programlayınız.

x=int(input("Bir sayı giriniz: "))

liste = [i for i in range(1,x+1)    if x % i == 0]
listeuz=len(liste)
print(liste)
print("Tam bölen sayısı: {}".format(len(liste)))
if x % listeuz == 0:
    print("{} sayısı {} sayısına tam bölündüğü için bir Tau Sayısıdır.".format(x,listeuz))
else:
    print("{} sayısı bir Tau Sayısı değildir!".format(x))