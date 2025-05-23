s1=int(input("1. sayıyı girin"))
s2=int(input("2. sayıyı girin"))
toplam=0
for i in range(s1,s2):
    toplam=toplam+i
     
adet=s2-s1
ortalama=toplam/adet
print(ortalama)