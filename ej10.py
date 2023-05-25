print("Bienvenido a la pizzería Bella Napoli")
veg=input("Desea pizza vegetariana, si o no ")
if veg.lower()=="si":
    print("Los ingredientes disponibles son pimiento y tofu, solo puede elegir uno")
    ingrediente=input("¿Cual desea? ")
    if ingrediente.lower()=="pimiento":
        print("Has elegido una pizza vegetariana, y sus ingredientes son tomate, mozarella y pimiento")
    elif ingrediente.lower()=="tofu":
        print("Has elegido una pizza vegetariana, y sus ingredientes son tomate, mozarella y tofu")
    else:
        print("El ingrediente seleccionado no esta disponible, solo puede elegir pimiento o tofu")
elif veg.lower()=="no":
    print("Los ingredientes disponibles son peperoni, jamón y salmón, solo puede elegir uno, por favor acuerdese de introducir también las tildes")
    ingrediente=input("¿Cual desea? ")
    if ingrediente.lower()=="peperoni":
        print("Has elegido una pizza no vegetariana, y sus ingredientes son tomate, mozarella y peperoni")
    elif ingrediente.lower()=="jamón":
        print("Has elegido una pizza no vegetariana, y sus ingredientes son tomate, mozarella y jamón")
    elif ingrediente.lower()=="samón":
        print("Has elegido una pizza no vegetariana, y sus ingredientes son tomate, mozarella y salmón")
    else:
        print("El ingrediente seleccionado no esta disponible, solo puede elegir peperoni, jamón o salmón")
else:
    print("No has introducido una respuesta válida, vuelve a probar, recuerde que debe escribir si o no")