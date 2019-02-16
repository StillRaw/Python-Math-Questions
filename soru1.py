#10000den küçük 2 veya 3e bölünebilen sayıların adedi
x = [i for i in range(10000)    if i % 2 == 0 or i % 3 ==0 ]    
lenx=len(x)
print("10.000 küçük,2 veya 3 sayısına tam bölünen sayılar {0} tanedir.".format(lenx))

#Girilen sayıdan küçük 2 veya 3e bölünebilen sayıların adedi
a=int(input("Lütfen bir sayı giriniz:"))
y = [i for i in range(a)    if i % 2 == 0 or i % 3 ==0 ] 
leny=len(y)
print("{1} sayısından küçük, 2 veya 3 sayısına tam bölünen sayılar {0} tanedir.".format(leny,a))