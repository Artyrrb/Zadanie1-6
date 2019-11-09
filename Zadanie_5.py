#Проверка на полиндромность

def pol(a):
    if len(a)<=1:
        return True
    if a[0]!=a[-1]:
        return False
    return pol(s[1:-1])

a=pol(input())
print (a)
