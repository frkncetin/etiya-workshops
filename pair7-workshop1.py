#Bir hesap makinesi kodladığımızı varsayalım, kullanıcı ilk olarak sırayla 2 adet sayı girecek ve bu sayılar
#arasında yapmak istediği dört işlemi seçecek. Seçerken verdiği değerler dört işlemden birisi değil ise 
#kullanıcı uyarılacak ( + - * / ). Girilen işleme göre bu iki sayı arasında ilgili işlem yapılarak kullanıcıya 
#sonuç gösterilecek. 

#kullanıcıdan vize ve final notları alacak.
#vize %40  final %60 etkili olacak
#vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
#uygulama ortalamayı hesaplayacak ve ortalamaya göre
#0-49 FF
#50-59 DD
#60-69 CC
#70-79 BB
#80-100 AA
#not ortalamasını ve not harfini kullanıcıya gösterecek programı kodlayınız.


sayi1 = float(input("Lütfen sayı giriniz: "))
sayi2 = float(input("Lütfen 2. sayıyı giriniz:"))

islem = input("yapmak istediniz işlemi seçiniz : (*, -,+,/) : ")

if islem == "+":
    print(sayi1 + sayi2)
elif islem == "-":
    print(sayi1 - sayi2)
elif islem == "*":
    print(sayi1 * sayi2)
elif islem == "/":
    print(sayi1 / sayi2)
else:
    print("seçim yanlıştır")


#-------------------------------------------------------

vize = float(input("Vize notunuzu giriniz: "))
final = float(input("Final notunu giriniz: "))
ortalama = (vize * 0.4) + (final*0.6)
if vize < 100 and final< 100:

    if ortalama <50:
        print("FF")
    elif ortalama <50 and ortalama < 60:
        print("DD")
    elif ortalama < 60 and ortalama <70:
        print("CC")
    elif ortalama < 70 and ortalama <80:
        print("BB")
    elif ortalama < 80 and ortalama <101:
        print("AA")
else:
    print("Yanlış girdiniz")
