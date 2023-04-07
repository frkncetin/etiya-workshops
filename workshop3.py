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