a = [1,2,5,6]
r = [[1,1], [2,2], [1,2], [2,3], [3,1], [2,1], [3,2], [5,5]]

'''
Achar os elementos repetidos
'''
feixoR = []

for i in range(len(r)):
	if r[i][0] == r[i][1]:
		feixoR.append(r[i])
		
print feixoR

'''
Achar o fecho completo de repetidos
'''

feixoCompleto = []

for i in range(len(a)):
	for j in range(len(feixoR)):
		if a[i] == feixoR[j][0] or a[i] in feixoR:
			break
	feixoCompleto.append([a[i],a[i]])
	
print feixoCompleto		

'''
Achar o fecho reflexivo
'''

lista = []
for i in range(len(feixoCompleto)):
	if feixoCompleto[i] not in feixoR:
		lista.append(feixoCompleto[i])
		
print "Fecho reflexivo: %s" % lista