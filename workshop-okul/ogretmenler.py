class ogretmen():
    def __init__(self,name,number):
        
        self.name = name
        self.number = number
    
    def add(liste):
        ad=input("Öğretmenin adı: ")
        if ad == "Q":
            return
        yas=input("Öğretmenin yaşı: ")
        if yas == "Q":
            return
        ogretmen1=ogretmen(ad,yas)
        liste.append(ogretmen1)
        print("\nYeni öğretmen kaydı gerçekleşti.\n")

    def read(liste):
        for i in liste:
            print(f"\n{i.name}: Yaşı: {i.number}") 

        print(f"\nÖğretmenSayısı: {len(liste)}\n")
        
    