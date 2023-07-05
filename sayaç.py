import time

def sayac(sure):
    while sure >= 0:
        print(sure)
        time.sleep(1)
        sure -= 1
    print("süre bitti")

sure_input = int(input("Süreyi saniye cinsinden girin: "))
sayac(sure_input)

