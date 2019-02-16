# 1^1+2^2+...+n^n=N toplamını veren FOR döngüsü

a=int(input("Lütfen bir sayı giriniz:"))

toplam=0

for i in range(1,a+1):
    toplam+=i**i

print("Girdiğiniz {0} değeri için toplam: {1} olarak bulunmuştur.".format(a,toplam))