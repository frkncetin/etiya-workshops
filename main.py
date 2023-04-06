print("Merhaba Etiya")

# değişkenler -start
# metinler, numerik obje

text="Merhaba"

print(text)
print(text)
text="selam"
print(text)
print(text)

studentCount="45" #string
print(studentCount)

studentCount=45 #int, integer = tam sayı
print(studentCount)

averagePoint=25.5 #float, decimal, double = ondalıklı sayı
print(averagePoint+5)

isVerified = True # boolean, bool = true, false
print(isVerified)

print(type(text))
print(type(studentCount))
print(type(averagePoint))
print(type(isVerified))

# değişkenler -end

#operatörler -start
number = 10
#matematiksel operatörler - mantıksal operatörler
print(10+10)
print(number+number)

print(number - 5)
print(number / 2)
print(number / 3)
print(number * 3)

# mod operatörü 
print(number % 3)

# mantıksal operatörler - karşılaştırma operatörleri
print(number == 10)
print(number == 11) 
print(number != 10)

print(number > 10)
print(number >= 10)

print(number < 10)
print(number <= 10)

# operatörler -end

print("********************")

# diziler - listeler -start
sayilar = [100,200,300,400,500, "merhaba", 15.5, True] #listedeki tüm elemanların veri tipi aynı olmak zorunda değil
#Programcı saymaya 0dan başlar
# index indis => 0
print(sayilar[0])
print(sayilar[5])

sayilar.append(100)
sayilar.append(600) # listenin sonuna eleman ekler.
print(sayilar)

sayilar.pop() # pop() default son değeri siler. index de verileribilir.
print(sayilar)

# [100, 200, 300, 400, 500, 'merhaba', 15.5, True, 100]
sayilar.remove(100)
print(sayilar)

sayilarEkleme = [700,800,900]
sayilar.extend(sayilarEkleme) # append in aksine tek bir değer değil listedeki tüm elemanları listeye ekler.
print(sayilar)

sayilar.clear() # dizinin içini boşaltan fonksiyon
print(sayilar)

# diziler - listeler -end

# string interpolation -start
 
hello = "Merhaba"
userName = "Furkan"

print(hello + " " + userName)
totalText = hello + " " + userName
print(totalText)

totalText = "{message} Sayın {name}".format(message=hello, name=userName)
print(totalText)

#f-string
totalText = f"Hoşgeldiniz {userName}"

# string interpolation -end

# karar yapıları -start
ortalamaNot = input("Lütfen ortalamanızı giriniz:")

#numerik - int, double
#type conversation -start
ortalamaNotAsInteger = int(ortalamaNot)
#type conversation -start

#if else blokları
# 4 satır 1 tab/indent

#indent
if ortalamaNotAsInteger > 80:
    print("Bravo")
elif ortalamaNotAsInteger > 60:
    print("Ortalama")
elif ortalamaNotAsInteger > 50:
    print("Normal")
else:
    print("Kaldınız")

studentCount =44
if studentCount > 20:
    print("Öğrenciler ders için hazır")

print("if bloğundan bağımsız ksıım")

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




#karar yaıları -end


