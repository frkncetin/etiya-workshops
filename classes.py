# class, nesne, obje, sınıf

class Human:
    #property, attribute => özellik, nitelik

    #initialize
    def __init__(self,name,age):
        print("yapıcı blok çalıştı")
        self.name = name
        self.age = age

    #davranışlar
    def talk(self,message):
        print(f"{self.name}: {message}")
    def walk(self):
        print(f"{self.name} is walking..")


#instance üretmek - örnek üretmek
human1 = Human("Halit", 25) #constructor => yapıcı blok
#uman1.name = "Halit"
#human1.age = 25
human1.talk("Merhaba")
human1.walk()









