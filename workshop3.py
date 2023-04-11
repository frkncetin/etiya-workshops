list = []
for i in range(10):
    sayi = int(input(f'{i+1}.sayıyı giriniz :') )
    list.append(sayi)

print("En büyük sayı :" ,max(list))

#***********************************************************

def ciftsayilar():
    list2 = []
    x = int(input ("Lütfen bir sayı giriniz: "))
    if x>0:
        for i in range(0,x,2):
            list2.append(i)
        print(list2)
    else:
        print("Lütfen 0'dan büyük sayı giriniz.")
        ciftsayilar()
ciftsayilar()

#************************************************************

def ciftsayilar():
    list2 = []
    x = int(input ("Lütfen üst limit giriniz: "))
    y = int(input ("Lütfen alt limit giriniz: "))

    if x%2==0:
        for i in range(y,x,2):
            list2.append(i)
        print(list2)
    elif x%2==1:
        for i in range(y+1,x,2):
            list2.append(i)
        print(list2)  

    else:
        print("Lütfen 0'dan büyük sayı giriniz.")
        ciftsayilar()
ciftsayilar()


def ciftsayilar():
    list2 = []
    x = int(input ("Lütfen üst limit giriniz: "))
    y = int(input ("Lütfen alt limit giriniz: "))

    if y%2==0:
        for i in range(y,x,2):
            list2.append(i)
        print(list2)
    elif y%2==1:
        for i in range(y+1,x,2):
            list2.append(i)
        print(list2)  

    else:
        print("Lütfen 0'dan büyük sayı giriniz.")
        ciftsayilar()
ciftsayilar()

#*******************************************************

forRangeMin = int(input("Üst limit"))
forRangeMax = int(input("Alt limit"))

for i in range(forRangeMin,(forRangeMax+1)):
    if i%2 ==0:
        print(i)

#************************************************************

biggestValue =0 
for i in range(10):
    sayi=int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi>biggestValue:
        biggesValue=sayi

print(f"Girdiğiniz en büyük sayı: {biggestValue}")

#**************************************************************

biggestValue =0
secondBiggestValue=0 
for i in range(10):
    sayi=int(input(f"{i+1}. sayıyı giriniz: "))
    if sayi>biggestValue:
        secondBiggestValue = biggestValue
        biggesValue=sayi

print(f"Girdiğiniz en büyük sayı: {biggestValue}")
print(f"Girdiğiniz 2. en büyük sayı: {secondBiggestValue}")

#*****************************************************************


sayilar =[]

for i in range(4):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz: ")))

sayilar.sort(reverse=True)
enBuyuk=int(input("Kaçıncı en büyük sayıyı görmek istersiniz: "))
print(sayilar[enBuyuk - 1])

#*********************************************************************

