# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 19:39:24 2022

@author: Alvaro
"""

class Calculadora:
    
    def __init__(self,num1,num2):
        self.numero1=float(num1)
        self.numero2=float(num2)
    
    def imprimir(self):
      
        print("Los números son: ", str(self.numero1) + "," + str(self.numero2))
        #print(f"Los números son: {self.numero1}, {self.numero2}")
        #print("Los números son: {} {}".format(self.numero1, self.numero2))
    def suma(self):
        sum=self.numero1+self.numero2
        print("El resultado de la suma es: ", sum)
    def resta(self):
        res=self.numero1-self.numero2
        print("El resultado de la resta es: ", res)
    def multiplicacion(self):
        mul=self.numero1*self.numero2
        print("El resultado de la muñtiplicacion es: ", mul)
    def division(self):
        div=self.numero1/self.numero2
        print("El resultado de la division es: ", div)

print("Calculadora")
print("Esto es un cambio")
num1=float(input("Ingrese el primer número:"))   
num2=float(input("Ingrese el segundo número:"))  

operaciones=Calculadora(num1,num2)  
operaciones.imprimir() 
operaciones.suma()  
operaciones.resta()     
operaciones.multiplicacion()
operaciones.division()      