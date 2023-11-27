# EJERCICIO 1 : SUMA DE NUMEROS 

def suma_num(n):
    
    suma = 0
    for i  in range (1, n+1):
        suma += i
    
    return suma
# print(suma_num(6))    


# FUNCION RECURSIVA 

def suma_recursiva(n):
    
    if n == 0 :
        return 0
    
    else :
       return n + suma_recursiva(n-1)
        
print(suma_recursiva(6))        
    

