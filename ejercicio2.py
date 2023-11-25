# potencia de un numero


def potencias(base,exponente):
    resultado =1
    
    for i in range(exponente):
        resultado*= base 
    
    print(resultado)
    
potencias(2,3)    