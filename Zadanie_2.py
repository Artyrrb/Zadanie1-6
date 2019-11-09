#Нахождение Fибоначи через рекурсию

def fib(n):
    if n==1:
        return 0
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)

print('Введите число N:')
a= fib(int(input()))
print('Число:',a)
