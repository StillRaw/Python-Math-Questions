#Kendisi dışındaki bütün pozitif bölenlerinin toplamı kendisine eşit olan sayılara,
#  mükemmel sayılar denir. Örnek: 28 sayısının tam bölenleri: 1-2-4-7-14
# Tam bölenlerinin toplamı: 1+2+4+7+14 = 28 olduğundan 28 sayısı mükemmel sayısıdır.
# 1000'den küçük tüm mükemmel sayıları listeleyen yazılımı python dilinde yazınız.

x=int(input("Bir sayı giriniz: "))
def mük(*args):
    for x in args:
        liste = [i for i in range(1,x+1)    if x % i == 0]
        liste.pop()
        listetop=sum(liste)
        #print("Tam bölenler: ",liste)
        #print("Tam bölenler toplamı: {}".format(listetop))
        if x == listetop:
            print(x)
        else:
            break
lis=(i for i in range(1,x))
for i in lis:
    mük(i)