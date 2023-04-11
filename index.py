# classes.py içindeki Humanı kullan
#import classes => tüm classes modülünü import eder
#from classes import Human => classes modülünden Human'ı import eder
from classes import Human
import random 
#Alias => takma ad
#from classes import Human as Insan
#import classes as Classlarim

human1 = Human("Halit",25)
human1.talk("Selam")

print(random.random())

