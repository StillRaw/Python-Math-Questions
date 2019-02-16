#İç içe for döngü yapısını kullanarak
#  çarpım tablosunu ekrana yazdıran yazılımı python dilinde yazınız.
n=0
for i in range(1,10):
    for j in range (1,10):
        n=i*j
        print(n,end=" ")
    print("\n")

