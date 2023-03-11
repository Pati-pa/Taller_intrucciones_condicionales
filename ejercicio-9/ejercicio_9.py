# programa para determinar si un numero es multiplo del otro

print("-----------------------------------------")
print("----------DETERMINAR EL TRIANGULO---------")
print("-----------------------------------------")

# INPUT
import math
Lado_A=int(input("ingrese el primer lado: "))
Lado_B=int(input("ingrese el segundo lado: "))
Lado_C=int(input("ingrese el tercer lado: "))
# PROCESSING

if Lado_C**2<Lado_A**2+Lado_B**2:
   rta= ("Es un triangulo agudo")
else:
   if Lado_C**2==Lado_A**2+Lado_B**2: 
      rta= ("Es un triangulo recto")
   else:
      if Lado_C**2>Lado_A **2+Lado_B**2:
         rta= ("Es un triangulo obtuso")
      else:
         rta= ("No es un triangulo")

         

   
# OUTPUT

print("-------------------------------------------")
print("-------------EL RESULTADO ES---------------")
print(rta)
print("-------------------------------------------")