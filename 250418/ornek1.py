otopark=int(input("kaç saat kaldınız:"))
if otopark <5:
    print("1 saate kadar 5 TL")
elif otopark>1 and otopark<5:
    print("ödeyeceğiniz tutar",otopark*4)
elif otopark >5:
    print("ödeyeğiniz tutar",otopark*3)
else:
    print("yanlış değer girdiniz")