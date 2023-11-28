# EJERCICIO 5 : SUMA ELEMENTOS DE UNA LISTA

def sumar_lista(lista):
    
    resultado = 0
    for elementos in lista :
        resultado += elementos
        
    return resultado

lista =[1,2,3,4,5,6,7,8,9,10]
# print(sumar_lista(lista))    


# FUNCION RECURSIVA 

def recursion_lista(lista):
    
    if  lista :
        return 0
    
    else :
        return lista[0] + recursion_lista(lista[1:])    

lista =[1,2,3,4,5,6,7,8,9,10]
print(recursion_lista(lista))

    