arq = open('texto2.txt','w') 
x ='v2.0 raw\n' 
y = input() 
 
for i in y: 
        x+=str(hex(ord(i)))[2:].lower()
        x+= ' ' 
        
arq.writelines(x) 
arq.close()

