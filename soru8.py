#1^1 + 2^2 + 3^3 + ... + 1000^1000 işleminden elde edilen sayının
#  son 10 rakamını hesaplayan yazılımı python dilinde yazınız.

N=0
for x in range(1,1000):
    N += x**x
print("Sonuç={}".format(N))
M=str(N)
K=len(M)
#print(M)
Mson=M[K-10:K]
print("Sonucun son 10 basamağı={}".format(Mson))