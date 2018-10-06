def bina(x,y):
	z = 0
	lista_1 = [] 
	for i in str(x):
		lista_1.append(int(i))
	lista_1.reverse()

	for i in range(0,y):
		z+=lista_1[i]*2**i
	return z	
x = '1 11 1001 11001 10001 1011 11011 10011 1010 11010 101 111 1101 11101 10101 1111 11111 10111 1110 11110 100101 100111 111010 101101 111101 110101'.split()
x = [(int(i)) for i in x ]
lista = []
for i in x:
	lista.append(bina(i, len(str(i))))
z = "v2.0 raw\n"
arquivo = open('ords.txt','w') 
for i in lista:
	z+= '%s'%str(hex(int(i)))[2:]
	z+= ' '
arquivo.writelines(z)
arquivo.close()

