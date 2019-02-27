#3'ün veya 5'in katı olan 10'dan küçük tüm doğal sayıları listelersek,
#  3, 5, 6, ve 9'u elde ederiz. 
# Bu katların toplamı 23'tür.
# 3'ün veya 5'in 1000'den küçük tüm katlarının toplamını 
# hesaplayan yazılımı python dilinde programlayınız.

üç=set([i for i in range(1,1001) if i % 3 == 0])
beş=set([i for i in range(1,1001) if i % 5 == 0])

birleşim = üç | beş

lenbir=len(birleşim)
top=sum(birleşim)
print("İstenilen toplam değeri:",top)
print("İstenilen aralıkta {} adet sayı vardır.".format(lenbir))