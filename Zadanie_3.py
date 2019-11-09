#Пересечение двух прямых

def otrezok(x1,y1,x2,y2,x3,y3,x4,y4):
    if (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)==0:
        return print('Не пересекаются')
    return print('Пересекаются')

print("Введите координаты отрезков:")
a= otrezok(int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()), int(input()))
print (a)
