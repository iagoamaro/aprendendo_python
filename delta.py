#!/bin/python
#calculador baskara
a = int(input("Digite o primeiro termo da equacao: " ))
b = int(input("Digite o segundo termo da equacao: " ))
c = int(input("Digite o terceiro termo da equacao: " ))
delta = b**2-(4*a*c)
if(delta<0):
    print(delta)
    print("seu delta nao tem raiz, pois ele é um numero negativo")
else:
    raiz_delta = delta**1/2.0
    xum=(-b + raiz_delta)/2*a
    xdois=(-b - raiz_delta)/2*a
    print("x1 = ",xum,"\nx2 = ",xdois)

    
         

        
