edad=int(input("Dime tu edad "))
if edad>16:
    ingresos=int(input("Dime tus ingresos mensuales "))
    if ingresos>1000:
        print("Debes tributar")
    else:
        print("Tus ingresos no superan los 1000 euros, no debes tributar")
else:
    print("No tienes más de 16 años, no debes tributar")