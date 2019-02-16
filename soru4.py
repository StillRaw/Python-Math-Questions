#Klavyeden girilen iki sayıyı çarpma operatörü (*) kullanmadan
# çarpan yazılımı python dilinde kodlayınız. f(x,y)=x*y

def carpma(x,y):
    sonuc=0
    
    for i in range(x):

        sonuc=sonuc+y
    return sonuc
print (carpma(5,3))