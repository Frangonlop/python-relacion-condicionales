print("El precio de las entradas son, si eres menor de 4 años puedes entrar gratis, si tienes entre 4 y 18 años debes pagar 5€ y si eres mayor de 18 años, 10€.")
years=int(input("Dime tu edad "))
if years<4:
    print("Eres menor de 4 años, puedes entrar gratis")
elif years<18:
    print("Tienes más de 4 años, pero menos de 18, debes pagar 5€")
else:
    print("Eres mayor de 18 años, debes pagar 10€")