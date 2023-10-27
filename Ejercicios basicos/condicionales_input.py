print("Programa evalua nota de alumnos:")

nota = int(input("introduce la nota del alumno:"))



def evaluar(nota):
	valoracion="aprobo"
	if nota<5:
		valoracion="No aprobo"
	return valoracion+" Nota = "+str(nota)

print(evaluar(nota))
