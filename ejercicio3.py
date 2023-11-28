# EJERCICIO 3:CONTEO RECRESIVO

def cuenta_regresiva(n):
    
    if n < 1 :
        print("el numero debe ser mayor a 1")
    
    else :    
     while n >= 1 :
        print( n)
        n -= 1   

# cuenta_regresiva(10)    


# EJERCICIO RECURSIVO

def recursion_cuenta( n):
    
    if n < 1 :
        return 0
    
    else :
        print(n)
    return recursion_cuenta(n -1)

recursion_cuenta(10)    

