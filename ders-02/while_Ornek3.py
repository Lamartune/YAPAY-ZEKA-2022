#klavyeden sıfır tuşluna basılıncaya kadar girilen sayıların ortalamasını alan döngü
sayi1 = 1
sayac = 0
toplam = 0
while sayi1!=0:
  sayi1 = int(input("Bir sayı giriniz: "))
  toplam += sayi1
  sayac+=1
  if(sayi1 ==0):
    ortalama = float(toplam/(sayac-1))
    print("Ortalama:",ortalama)