numero = int(input("Digite el numero entero positivo: "))
es_primo = True

if numero<=1:
    es_primo=False
else:
    for x in range(2,(numero//2)+1):
        if numero % x == 0:
            es_primo = False
            break

if es_primo:
    print("El numero es primo.")
else:
    print("El numero no es primo.")