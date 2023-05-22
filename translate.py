print('Numero de caracteres: ',end='')
car=int(input())
carac=[""]*car
trans=[0]*car
transC=[""]*car
for i in range(car):
    print('Ingresar caracter ',i+1,' en binario: ',end='')
    carac[i]=input()
print()
#print(carac)
#print()
#print(len(carac))
for i in range(len(carac)):
    x=0
    c=0
    for j in range(len(carac[i]),0,-1):
        #print('{}'.format(carac[i][j-1]))
        if(carac[i][j-1]=='1'):
            x+=(2**c)
        c+=1
    #print(x)
    trans[i]=x
print(trans)
print()
abcMay='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
abcMin='abcdefghijklmnopqrstuvwxyz'
esp='ÁÉÍÑÓÚÜáéíñóúü'
aux=0
pattern=[0,8,4,4,2,7,2,5,8,4,4,2,7,2]
print('Traduccion: ',end='')
for i in range(len(trans)):
    c=2
    indice=0
    if(trans[i]==32):
        transC[i]=' '
    elif(trans[i]==44):
        transC[i]=','
    elif(trans[i]==46):
        transC[i]='.'
    elif(trans[i]<91):
        transC[i]=abcMay[trans[i]-65]
    elif(trans[i]<123):
        transC[i]=abcMin[trans[i]-97]
    else:
        aux=trans[i]-193
        while(aux>8):
            aux-=pattern[c]
            indice=c
            c+=1
        transC[i]=esp[indice]
    print(transC[i],end='')