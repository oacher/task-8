try:
        n = int(input("Введите число: ")) 
except ValueError:
        print("Ошибка")
else:
    try:
        base = int(input("Введите основание системы счисления: ")) 
    except ValueError:
        print("Ошибка")
    else:
        if not((base==8) or (base==2)):
           print("Ошибка")
        if base == 8:
            if n == 0:
                print("Вывод:0")
            n2=n
            n=abs(n)
            newN = ''
            while n > 0:
                newN = str(n % base) + newN
                n //= base
            if n2 < 0:
                print("Вывод: -" + str(newN))
            elif n2 >0:    
                print("Вывод:" + str(newN))
        if base == 2:
            if n == 0:
                print("Вывод:0")
            if n>0:
                r1 = bin(n)[2:]
                res = '0' * (8-len(r1)) + r1
                print("Вывод:" + str(res))    
            if n<0:
                r1 = bin(~(-n))[4:]
                res = '1' * (7-len(r1)) + '0' + r1
                print("Вывод:" + str(res))
                
            
    
