cicekler=["papatya","şakayık","gül","menekşe","kaktüs"]
#listenin şakayık kelimesi kaçıncı elemanı olduğunu bulunuz 
indeks=cicekler.index("şakayık")
print("şakayık elemanı listenin:",indeks,"inci elamanıdır")
cicekler.remove("kaktüs")
print("cicekler listesindeki kaktüs elemanı silindikten sonraki hali:",cicekler)
say=cicekler.count("papatya")
print("papatya elemaı listede:",say,"adet vardır")
cicekler.sort(reverse=True)
print("cicekler listesinin büyükten küçüğe sırlanmış hali:",cicekler)