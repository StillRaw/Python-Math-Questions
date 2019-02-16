#x ve y değeri ile x üssü y sayısını döngü yapılarını kullanarak 
# hesaplayan yazılımı python dilinde yazınız.En sonda oluşan None düzeltilmeli!
x=int(input("Taban Değeri:"))
y=int(input("Üs Değeri:"))

def f(x,y):
    son=1
    if x > 0 and y > 0:
        for i in range(y):
         son=son*x
         i+=1
        return son
    else:
        print("0 Üssü 0 durumu belirsizliği ifade eder!")
print(f(x,y))