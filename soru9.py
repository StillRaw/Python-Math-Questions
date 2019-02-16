x=int(input("Bir sayı giriniz:"))

topkare=0
karetop=0
topkareson=0

for i in range(1,x+1):
    karetop+=i**2
    topkare+=i
    topkareson=topkare*topkare

fark=topkareson-karetop

print("Girdiğiniz {0} değeri için;\n\
Karelerinin toplamı:{1}\n\
Toplamlarının Karesi:{2}\n\
İkisinin Farkı:{3} olarak bulunmuştur.".format(x,karetop,topkareson,fark))