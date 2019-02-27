#k > 0 olmak şartıyla (k-1) sayısı 4’e tam bölünüyorsa
# hilbert sayısı olarak adlandırılır. Örnek: 9 sayısının 1 ekseği 
# olan 8 sayısı 4'e tam bölündüğü için 9 sayısı hilbert sayıdır.
# 1000'den küçük tüm hilbert sayılarını listeleyen yazılımı python dilinde yazınız.

print("===1000' den küçük Hilbert Sayıları===")
liste=[i for i in range(2,1000)  if (i-1) % 4 == 0]
print(liste)