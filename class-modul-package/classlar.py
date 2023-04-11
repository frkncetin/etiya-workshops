# sınıflar => classlar
# modules
# paket yönetimi
# self => this - self genel bir kullanım. başka isimlendirme de olur
# self keywordu calss içindeki diğer alanlara ulaşılmasını sağlar

""""
class Human:
    def talk(self):
        print("Human is talking..")
    def walk(self):
        print("Human is walking..")
"""
#instance => örnek
from Human import Human

human1 = Human("Enes")
#human1.name= "Enes"
human1.talk("talking")
human1.walk()
print(human1)

human2 = Human("Halit")
#human2.name = "Cem"
human2.talk("Selam")
human2.walk()
print(human2)

Human("Melike").talk("Merhaba")

