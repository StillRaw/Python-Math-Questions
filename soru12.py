x=int(input("Taban değerini giriniz:"))
y=int(input("Üs değerini giriniz:"))

def f(x,y):                                 #Üstel Fonksiyon tanımladık
    return x**y
print("Fonksiyon değeri:",f(x,y))                #Üslü Sayıyı yazdırdık

#Sonucun basamak değerlerini toplamam gerek!

z = str(f(x,y))                             #Sonucu Stringe çevirdik
numbers = [w for w in z if w.isdigit()]     #Stringdeki sayılardan bir liste oluşturduk

a=len(numbers)                              #
top=0                                       #
for i in range(a):                          #Oluşturduğumuz listeyi toplayıp yazdırdık
    top+=int(numbers[i])                    #
print("Basamak değerleri toplamı:{0}".format(top))

