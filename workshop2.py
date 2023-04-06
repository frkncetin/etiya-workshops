vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final + 0.6)

#eğer final 40'dan küçükse kullanıcı kaldı
#eğer ortalama 50'den küçükse kullanıcı kaldı
#eğer vize finalin 2 katı ise kullanıcı kaldı
#bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyorum

if ortalama < 50 or final < 40 or vize > (final*2):
    print("Kullanıcı Kaldı")
else:
    print("Kullanıcı Geçti")
