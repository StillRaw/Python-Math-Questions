#Bir sayı eğer 4 basamaklı ise ve sayıyı oluşturan rakamlardan her birinin
#  4. kuvvetinin toplamı (3 basamaklı sayılar için 3.kuvveti) o sayıya eşitse
#  bu sayıya "Armstrong" sayısı denir.
# Örnek: 1634 = 1**4 + 6**4 + 3**4 + 4**4 = 1634
# Kullanıcıdan alınan bir sayının "Armstrong" sayısı olup olmadığını 
# bulan yazılımı python dilinde programlayınız.
#########GİRİLEN DEĞERE KADAR AMSTRONG SAYILARINI HESAPLAYAN PROGRAM YAP#########
x=input("Bir sayı giriniz:")
lenx=len(x)
top=0
print(lenx)
for i in range(lenx):
    if x == 'q':
        break
    else:
        top+=int(x[i])**(lenx)
if top == int(x):
    print("Girdiğiniz {} sayısı bir Amstrong Sayısıdır.".format(x))
else:
    print("Girdiğiniz {} sayısı bir Amstrong Sayısı değildir.".format(x))