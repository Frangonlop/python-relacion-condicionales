punt=float(input("Dime la puntuación obtenida "))
if punt==0.0:
    print("Su nivel es inaceptable")
    print("El dinero obtenido es "+str(2400*punt))
elif punt==0.2:
    print("Su nivel es aceptable")
    print("El dinero obtenido es "+str(2400*punt))
elif punt>=0.6:
    print("Su nivel es meritorio")
    print("El dinero obtenido es "+str(2400*punt))
else:
    print("La puntuación dada no es válida, vuelve a probar")
