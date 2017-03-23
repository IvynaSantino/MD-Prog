#coding: utf-8

conjunto = [1,2,3]
matriz = [[1,2], [1,1], [1,3]]

def fechoReflexivo(conjunto, matriz):
	# não modifiquem a assinatura da função!
	
	repete = repetidos(matriz)
	b = fechoCompleto(conjunto, repete)
	reflexo = fechoReflexo(b, repete)
	
	return reflexo

def repetidos(r):
	feixoR = []

	for i in range(len(r)):
		if r[i][0] == r[i][1]:
			feixoR.append(r[i])
			
	return feixoR

def fechoCompleto(a, feixoR):
	feixoCompleto = []

	for i in range(len(a)):
		for j in range(len(feixoR)):
			if a[i] == feixoR[j][0] or a[i] in feixoR:
				break
		feixoCompleto.append([a[i],a[i]])
		
	return feixoCompleto	
	
	
def fechoReflexo(feixoCompleto, feixoR):
	lista = []
	for i in range(len(feixoCompleto)):
		if feixoCompleto[i] not in feixoR:
			lista.append(feixoCompleto[i])
			
	return lista

def main():
	conjunto = [1,2,3]
	matriz = [[1,2], [1,1], [1,3]]

	print fechoReflexivo(conjunto, matriz)
	
if __name__ == "__main__":
	main()
