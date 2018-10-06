arq = open('texto.txt','w')
x ='v2.0 raw\n'
for i in range(0,255):
	x+=str(hex(ord(chr(i))))[2:]
	x+= ' '
arq.writelines(x)
arq.close()
