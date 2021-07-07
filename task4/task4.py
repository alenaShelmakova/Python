import sys

if len (sys.argv) < 3:
    print ("Ошибка. Слишком мало параметров.")
    sys.exit (1)

if len (sys.argv) > 3:
    print ("Ошибка. Слишком много параметров.")
    sys.exit (1)

a = sys.argv[1]
b = sys.argv[2]

c = '*'

if a == b:
    print('OK')
else:
    if len(a)==len(b): 
        n = len(a)
        for i in range(n):
            if a[i] == b[i] or b[i] == c:
                isEquial = True         
            else: 
                isEquial = False
                break   
        if isEquial == True:
            print('OK')
        else:
            print('KO')

    elif len(a)>len(b): 
        n = len(b)
        for i in range(n):
            if a[i] == b[i] or b[i] == c:
                isEquial = True         
            else: 
                isEquial = False
                break   
        if isEquial == True and b[-1] == c:
            print('OK')
        else:
            print('KO')

    elif len(b)>len(a): 
        n = len(a)
        m = (int)(len(b)-len(a))
        k = b[-m:]
        for i in range(n):
            if a[i] == b[i] or b[i] == c:
                isEquial = True         
            else: 
                isEquial = False
                break  
        for i in range(m):
            if k[i] == c:
                isEquial = True         
            else: 
                isEquial = False
                break  
                             
        if isEquial == True:
            print('OK')
        else:
            print('KO')

