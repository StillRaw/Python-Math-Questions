#Ritmik sayma sayıları şu şekildedir.
# 2-4-6-8….
# 3-6-9-12…
# 1'den 10'a kadar olan tüm sayıların 100'e kadar olan ritmik sayılar
# tablosunu iç-içe döngü yapılarını kullanarak python dilinde kodlayınız.
for i in range(2,11):
    for j in range(1,101):
        if j % i == 0:
            print(j,end=" ")
    print("\n")