#Klavyeden girilen ikilik sayı sistemindeki herhangi bir sayıyı
# 10'luk sayı sistemine çeviren yazılımı python dilinde yazınız.

x=str(input("İkilik tabanda bir sayı giriniz:"))

liste=list(x)
liste=liste[::-1]

luz=len(liste)
s1=0
print(liste)
#print(luz)

for i in range(1,luz+1):
    s1=s1+(2**(i-1))*int(liste[i-1])
print("İkilik tabandaki {0} sayısının, onluk tabandaki karşılığı {1} sayısıdır.".format(x,s1))