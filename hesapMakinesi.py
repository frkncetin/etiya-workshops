#kullanucu sürekli konsolda tutan => sonsuz döngü
#hesap makinesi
#4 işlem + mod alma
#q girdiğinde program sonlanacak => sonsuz döngüyü kırmak(break)
#fonksiyon


def getNumberFromUser():
    return float(input("Bir sayı giriniz :"))
def calculateSum():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"Toplama işleminin sonucu: {num1 + num2}")
def calculateMinus():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"Çıkarma işleminin sonucu: {num1 - num2}")
def calculateMultiply():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"Çarpma işleminin sonucu: {num1 * num2}")
def calculateDivide():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"Bölme işleminin sonucu: {num1 / num2}")
def calculateMod():
    num1 = getNumberFromUser()
    num2 = getNumberFromUser()
    print(f"Mod alma işleminin sonucu: {num1 % num2}")

while True:
    userInput = input("Yapmak istediğiniz işlemi seçiniz: ")
    if userInput == "q":
        break
    if userInput == "+":
        calculateSum()
    elif userInput == "-":
        calculateMınus()
    elif userInput == "*":
        calculateMultiply()
    elif userInput == "/":
        calculateDivide()
    elif userInput == "%":
        calculateMod()
