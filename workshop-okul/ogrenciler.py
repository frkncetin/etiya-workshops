class ogrenci():
    def __init__(self,name,number):
        
        self.name = name
        self.number = number
    
    def add(liste):
        ad=input("Öğrencinin adı: ")
        if ad == "Q":
            return
        yas=input("Öğrencinin yaşı: ")
        if yas == "Q":
            return
        ogrenci1=ogrenci(ad,yas)
        liste.append(ogrenci1)
        print("\nYeni öğrenci kaydı gerçekleşti.\n")

    def read(liste):
        for i in liste:
            print(f"\n{i.name}: Yaşı: {i.number}") 

        print(f"\nÖğrenci Sayısı: {len(liste)}\n")
        
    
    