# Üçgensel sayı dizileri ardışık doğal sayıların toplanmasıyla üretilir.
# Örneğin 7. üçgensel sayı 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28'dir. 
# İlk 10 üçgensel sayı şöyledir:1, 3, 6, 10, 15, 21, 28, 36, 45, 55, …
# Siz de, klavyeden girilecek herhangi bir pozitif tam sayının üçgensel sayı değerini 
# hesaplayan yazılımı python dilinde yazınız.
print("""
                      ÜÇGENSEL SAYI DEĞERİ HESAPLAMA
_________________________________________________________________________________
Açıklama: Üçgensel sayı dizileri ardışık doğal sayıların toplanmasıyla üretilir.
          Örneğin 7. üçgensel sayı 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28'dir.

Amaç:     Bu program girilen sayının Üçgensel Değerini hesaplar.

                                                           created by Onur Gülşin
_________________________________________________________________________________""")

try:
    x=int(input("Lütfen bir sayı giriniz:"))
    i=0
    top=0
    if int(x) < 0:
        print("Lütfen geçerli formda bir sayı kullanınız!")
    else:
        while i <= int(x):
            top+=i
            i+=1
        print("{} sayısının Üçgensel Sayı Değeri:{}".format(x,top))
except ValueError:
    print("Lütfen geçerli formda bir sayı kullanınız!")