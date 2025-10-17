def soma(n1,n2):
    return (f"{n1} + {n2} = {n1+n2}")
            
def subtracao(n1,n2):
    return (f"{n1} - {n2} = {n1-n2}")

def multiplicacao(n1,n2):
    return (f"{n1} x {n2} = {n1*n2}")
    
def divisao(n1,n2):
    if n1 == 0 or n2 == 0:
        print("não se pode dividir por 0")
    else:
        return (f"{n1} / {n2} = {n1/n2}")