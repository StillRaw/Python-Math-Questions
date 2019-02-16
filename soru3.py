#1 ile 5000 arasındaki tek sayıların ve çift sayıların toplamını ayrı ayrı hesaplayıp,
#ekrana yazdıran yazılımını python dilinde yazınız.

t=[i for i in range(5000)   if i % 2 == 1]
ç=[i for i in range(1,5000)   if i % 2 == 0]

ttop=sum(t)
çtop=sum(ç)

#print(t)
print(ttop)
#print(ç)
print(çtop)