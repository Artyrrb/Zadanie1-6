#Нахождение НОД и НОК чисел

def nod(a,b):
    if a==1 or b==1:
        return 1
    oli=[]
    tli=[]
    for i in range(1,a+1):
        if a%i==0:
            oli.append(i)
    for y in range(1,b+1):
        if b%y==0:
            tli.append(y)
    return  max(list(set(oli) & set(tli)))

def nok(a,b):
    if a==1 or b==1:
        return 1
    return a*b/nod(a,b)
print('Введите первое число:')
a=int(input())
print('Введите второе число:')
b=int(input())
dl = nod(a,b)
kr = nok(a,b)
print('Число НОД:',dl)
print('Число НОК:',kr)
