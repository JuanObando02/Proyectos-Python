def main():
	palabra = input("Ingrese una palabra: ")
	resultado = twttrr(palabra)
	print("La palabra abreviada es: " + ''.join(resultado))

def twttrr(pal):

	pal = pal.lower()
	lista=[]
	for z in range(len(pal)):
		if pal[z] not in ["a","e","i","o","u"," "]:	
			lista.append(pal[z])
	return lista

if __name__ == "__main__":
	main()
