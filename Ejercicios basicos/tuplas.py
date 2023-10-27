tupas=(5,10,3)
#asi se crea y define una tupa, esta no podra ser modificada en un futuro siempre tendra sus mismos valores

print(tupas[2])

lista=list(tupas)
print(lista[:])
print(tupas[:])

#con list() podemos volver una tupa a lista 

lista.extend(["juan","andres","pedro"])
print(lista[:])
tupla=tuple(lista)
print(tupla[:])

#convertimos listas a tuplas con tuple()

print("juan" in tupla)
#in para buscar en la tupla
print(tupla.count(3))
#.count para contar cuantas veces se encuentra un elemento en la tupla

print(len(tupla))
#len() devuelve la cantida de elementos que tiene la tupla

mitupla="juan",3,2003,10,"obando"

print(mitupla[:])





