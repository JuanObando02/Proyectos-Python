def mensaje():
	print("Hola, juan bienvenido")
	print("Hola, juan adios")
	print("Hola, juan buen dia")

#funcion en python que no retorna
def suma():
	nu1=5
	nu2=7
	print(nu1+nu2)
suma()
#definicion de funciones en python y retorna 
def retorna(n1,n2):
	return n1+n2

print(retorna(4,100))
mensaje()

#definicion de un arreglo
milista=["juan","andres","danna","jhon"]
print(milista[-2])

#se busca desde atras para delante con -2
print(milista[0:3])
#se imprimen los 3 primero
print(milista[:2])
#se imprimen todos los primeros hasta el 2
print(milista[1:3])
#se eimprimen del 1 al 3
print(milista[:3])
#se imprimen del 3 hasta el final de la lista

milista.append("Sandra")
#agrega el elemento al final

print(milista[:])

milista.insert(2,"pepe")
print(milista[:])
#inserta elemento en la posicion que se le indique con .insert a diferencia de .append que los inserta al final
milista.extend(["mateo","tomas","camilo"]);
print(milista[:])
#agrega al final de la lista varios elementos con .extend dentro de un [] y separados por ,

print(milista.index("mateo"))
#.index devuelve el indice de un elemento en especifico buscado. 
#en caso de haber dos elementos iguales retorna el primero elemento de la lista

print("pepe" in milista)
print("pepes" in milista)
#.in busca un elemento en la lista deseada y retoran true si esta y falce si no esta.
#una lista en python puede guardar distintos tipos de elementos en las listas o arreglos son importar.

milista.remove("danna")
#elimina elementos de la lsita deseada con nom_lista.remove("elemento") si no esta se crea una excepcion
#milista.remove("pepes")

print(milista[:])

milista.pop();

#elimina el ultimos elemento ingresado a la lista con .pop()

lista=[2,3,4,"carlos"]

lista3=milista+lista
print(lista3[:])
#se pueden sumar listas asi

# o con * podemos repetir los elementos de una lista una cantidad de veces en especifico
