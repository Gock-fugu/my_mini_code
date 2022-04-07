def arif():
    while True:
        try:
            a=int(input("впиши число а:"))
            b=int(input("впиши число b:"))
            i=input("Яку дію виконати")
        
        except ValueError:
            pass
        try:
            if i == '+':
                print(a, '+', b, '=', a+b)
            elif i == '-':
                print(a, '-', b, '=', a-b)
            elif i == '*':
                print(a, '*', b, '=', a*b)
            elif i == '/':
                print(a, '/', b, '=', a/b)
            elif i == '**':
                print(a, '**', b, '=', a**b)
        except ZeroDivisionError:
            print("На 0 не ділиться")
        
            

arif()
