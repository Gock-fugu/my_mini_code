def arif():
    while True:
        try:
            a=int(input("впиши число а:"))
            b=int(input("впиши число b:"))
            i=input("Яку дію виконати")
        
        except ValueError:
            pass
        try:
            print(f'{a}+{b}={a+b}' if i=='+' else (f'{a}-{b}={a-b}' if i=='-' else (f'{a}*{b}={a*b}' if i=='*' else (f'{a}/{b}={a/b}' if i=='/' else None))))

        except ZeroDivisionError:
            print("На 0 не ділиться")
        
            

arif()
