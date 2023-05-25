rent=int(input("¿Cuál es tu renta anual? "))
if rent<10000:
    print("Tu impositivo es del 5%")
elif rent<20000:
    print("Tu impositivo es del 15%")
elif rent<35000:
    print("Tu impositivo es del 20%")
elif rent<60000:
    print("Tu impositivo es del 30%")
else:
    print("Tu impositivo es del 45%")