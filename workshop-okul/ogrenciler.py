class ogrenci():
    def __init__(self,name,number):
        
        self.name = name
        self.number = number
    
    def add(liste):
        ad=input("Öğrencinin adı: ")
        yas=input("Öğrencinin yaşı: ")
        ogrenci1=ogrenci(ad,yas)
        liste.append(ogrenci1)
        print("\nYeni öğrenci kaydı gerçekleşti.\n")

    def read(liste):
        for i in liste:
            print(f"\n{i.name}: Yaşı: {i.number}") 

        print(f"\nÖğrenci Sayısı: {len(liste)}\n")
        
    
    
    #def numara(self):
    #    print(f"{self.name}: Numarası: {self.number}")
    #def isim(self):
    #    print(f"{self.number}: Adı: {self.name}")
    """"
    listIsim=[]
    listNumara=[]
    def ogrenciKaydi(self):
        listIsim.append(self.name)
        listNumara.append(self.number)

    print(f"Öğrenci listesi :{listIsim} {listNumara}")
    """