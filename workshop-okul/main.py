from ogrenciler import ogrenci
from ogretmenler import ogretmen

listeOgrenci=[]
listeOgretmen=[]

#print(listeOgrenci)    

def ogrenciKaydi():
    ogrenci.add(listeOgrenci)
def ogrenciOku():
    ogrenci.read(listeOgrenci)
def ogretmenKaydi():
    ogretmen.add(listeOgretmen)
def ogretmenOku():
    ogretmen.read(listeOgretmen) 

while True:
    islem=input("Hangi işlemi yapmak istersiniz:\nÖğrenci Kaydı: A\nÖğrenci Listesi: B\nÖğretmen Kaydı: C\nÖğretmen Listesi: D\nÇıkış: Q\nSeçim :")
    if islem == "Q":
        break
    elif islem == "A":
        ogrenciKaydi()
    elif islem == "B":
        ogrenciOku()
    elif islem == "C":
        ogretmenKaydi()
    elif islem == "D":
        ogretmenOku()
            
