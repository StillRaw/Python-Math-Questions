#n! şu şekilde yazılabilir : 1*2*3*......(n-1)*n
# Örneğin, 10! = 10 * 9 * ... * 3 * 2 * 1 = 3628800.
# Ve 10! sayısının basamaklarının toplamı da 3 + 6 + 2 + 8 + 8 = 27 'dir.
# Yukarıdaki örnekte olduğu gibi, girilen sayının faktöriyel değerinin basamakları 
# toplamını hesaplayan yazılımı python dilinde yazınız.
x=input("Bir sayı giriniz:")
fak=1
for i in range(1,int(x)+1):
    fak=fak*i
print(fak)
top=0
liste=list(str(fak))
for i in range(len(liste)):
    top+=int(liste[i])
print(top)