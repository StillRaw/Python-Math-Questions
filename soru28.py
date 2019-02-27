# Rakamlarının herbirinin faktöriyelleri toplamı kendisine eşit olan sayılara 'digit faktöriyel' denir.
# Örnek: 145 sayısı için 1! + 4! + 5! = 1+24+120 = 145 olduğundan 145 sayısı digit faktöriyeldir.
# Buna göre 100000'nin altındaki dijit faktöriyel sayıları listeleyen yazılımı python dilinde programlayınız. 
# (Not: 1 ve 2 sayıları yukarıdaki şartı sağlamalarına rağmen digit faktoriyel olarak değerlendirilmez.)
import math
def fak():
    liste=[]
    for i in range(3,10000000):
        liste =list(str(i))               #for döngüsüyle tarattığım sayıları stringe çevirip sayıları parçaladım.
        top=0
        for j in liste:   
            top += math.factorial(int(j)) #math kütüphanesindeki factorial() fonksiyonu kullandım
        #print(top)
        if (top == i):
            print(i)
fak()