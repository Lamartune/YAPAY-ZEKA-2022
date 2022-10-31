ad=input("Adınızı giriniz: ")
vize=int(input("Vize notunuzu giriniz: "))
final=int(input("Final notunuzu giriniz:"))

not1=float(vize*0.4+final*0.6)
print("Ortalama: ",not1)
if not1>=59.5 or final>=85:
    print(ad,"Geçti")
else:
    print(ad,"Kaldı")