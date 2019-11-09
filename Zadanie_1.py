print ("Введи число N")
N = int(input())
mass = [i for i in range(2, N+1)]
mainmass =[]
print ('Массим иследуемых чисел:',mass)
           
for i in mass:
    for z in range(2,i):
        if i%z == 0:
            break
    else:
        mainmass.append(i)
        
print ("Простые числа",mainmass)
            
        
    
        
            
    
