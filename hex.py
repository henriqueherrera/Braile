arq = open('texto.txt','w')
i= input();x=list(( str(bin(ord( y)))[2:])for y in i)
arq.writelines('%s '%i for i in x)
arq.close()







