#Fibonacci serisinde her sayı, kendisinden önce gelen iki sayının toplamıdır.
# 1 ve 2 ile başlayan serinin ilk 10 sayısı:1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Bu serinin dört milyondan küçük tüm çift sayılarının toplamını hesaplayan
# yazılımı python dilinde yazınız.

fibo=[1,1]

for i in range(100):
    z=fibo[i]+fibo[i+1]
    if fibo[i+1] <= 4000000:
        fibo.append(z)
    else:
        break
print("4 milyondan küçük Fibonacci sayıları:",fibo)
print("\n")

fiboç=[i for i in fibo  if i % 2 == 0]
print("4 milyondan küçük ÇİFT Fibonacci sayıları:",fiboç)
print("\n")
    
top=sum(fiboç)
print("4 milyondan küçük ÇİFT Fibonacci sayılarının TOPLAMI:",top)