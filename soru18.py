#Aşağıdaki tekrarlama dizisi pozitif tam sayılar için tanımlanmıştır:
# n → n/2 (n çift)
# n → 3n + 1 (n tek)
# Yukarıdaki kuralı uygulayarak ve 13'ten başlayarak aşağıdaki diziyi üretiriz:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# 13'ten başlayıp 1'de sonlanan bu dizinin 10 adet terim içerdiği görülebilir. 
# Henüz kanıtlanmış olmasa da (Collatz Problemi), bütün başlangıç sayılarının 1'de 
# sonuçlanacağı sanılmaktadır. Siz de, klavyeden girilecek herhangi bir pozitif tam sayının 
# collatz zincirini oluşturan yazılımı python dilinde yazınız.

n = int(input("Başlangıç değeri: "))
while n > 1:
    if n % 2 == 0:  # n çift sayıysa
        n = n/2
    else:   # n tek sayıysa
        n = 3*n + 1
    print(int(n), end=" → ")