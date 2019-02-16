#0 ile 100 arasında rastgele sayı üretip, kullanıcının bu sayıyı tahmin etmesini isteyen 
# ve kaç tahmin sonunda sayıyı bulduğunu kullanıcıya gösteren yazılımı python dilinde kodlayınız.
# Not: Sistemin rastgele sayı üretmesi için
# random modülünden yararlanabilirsiniz.import random
# sayi=random.randint(1,100)
import random
sayi=random.randint(1,100)
print("### 0 ile 100 arasında üretilen sayıyı tahmin ediniz ###")

for i in range(500):
    x = input("Tahmin değerini giriniz:")
    if x == "q":
        print("Üretilen değer {} sayısıydı.".format(sayi))
        break
    elif int(x) > 100:
        print("Tahmin değeri 100'den büyük girdiniz.")
    elif x==str(sayi):
        print("Tahmin değerini {}. girişinizde buldunuz.".format(i+1))
        break
    