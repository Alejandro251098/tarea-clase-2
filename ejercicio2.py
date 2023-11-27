# potencia de un numero


def potencias(base,exponente):
    resultado =1
    
    for i in range(exponente):
        resultado*= base 
    
    # print(resultado)
    
# potencias(2,3)    


# FUNCION RECURSIVA

def potenciar_recursiva(base, exponente):
    
    if exponente == 0:
        return 1
    else :
        return base * potenciar_recursiva(base , exponente - 1)
    
    
print(potenciar_recursiva(2,3))
    
    
    
    
    