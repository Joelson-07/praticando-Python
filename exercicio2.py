contador=0
impares=0
pares=0
while contador<10:
    n=int(input("digite um número: "))
    if n%2==0:
        pares+=1
    else:
        impares+=1
    contador+=1
print("números pares" ,pares)
print("números pares" ,impares)
