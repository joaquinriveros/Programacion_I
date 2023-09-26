def most(a,b):
    if (a>b):
        return a
    else:
        return b
    
def least(a,b):
    if (a<b):
        return a
    else:
        return b
    
#PROGRAMA PRINCIPAL

x= int(input("Un numero: "))
y= int(input("Otro numero: "))

print(most(x-3, least(x+2, y-5)))