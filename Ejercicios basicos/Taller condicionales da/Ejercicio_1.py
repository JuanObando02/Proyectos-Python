import sys
try:
    numero = int(input("Escriba un número: "))
except ValueError:
    print("El número debe ser un entero, intente nuevamente")
    sys.exit()
es_par = str ()
es_positivo = str ()
if numero == 0:
    print("El número es cero, por lo que no es positivo, negativo, par o impar")
else:
    if numero > 0:
        es_positivo = "es positivo"
    else:
        es_positivo = "es negativo"
    if numero % 2 == 0:
        es_par = "es par"
    else:
        es_par = "es impar"
    print("El número ingresado " + es_positivo + " y " + es_par) 
