#Kullanıcının girdiği sayıyı 2'lik sayı sistemine çeviren yazılımı python dilinde yazınız.
import time

x=int(input("Sayı giriniz:"))
print("2'lik tabandaki değer hesaplanıyor...")
time.sleep(1)

if x==1:
    print("1 sayısının 2'lik tabandaki değeri 1'dir.")
else:
    liste=[]
    bolum=int(x/2) #2
    kalan=x%2      #1       
    liste.append(kalan) #1

    while bolum >= 2:
        kalan=bolum % 2
        bolum=int(bolum/2)
        liste.append(kalan)
    liste.append(bolum)
    liste=liste[::-1]
    listeuz=len(liste)
    print("""2'lik tabandaki değer aşağıdaki gibidir
↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓ ↓""")

    for i in range(listeuz):
        rakam=liste[i]
        print(rakam, end=" ")