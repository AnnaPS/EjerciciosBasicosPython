#Ejercicio 1
a=[1,2,3,4,5]
b=['a','b','c','d','e']
c=[6,7,8,9,10]

#Ejercicio 2
print('Primer elemento de la lista a:',a[0])
print('Primer elemento de la lista b:',b[0])
print('Primer elemento de la lista c:',c[0])
print("\n")

#Ejercicio 3
print('Ultimo elemento de la lista a:',a[-1])
print('Ultimo elemento de la lista b:',b[-1])
print('Ultimo elemento de la lista c:',c[-1])
print("\n")

#Ejercicio 4
print('El contenido de la lista a es:',a[0:])
print('El contenido de la lista b es:',b[0:])
print('El contenido de la lista c es:',c[0:])
print("\n")

#Ejercicio 5
par=[2,4,6,8]
impar=[1,3,5,7]

#i)Sumar el primer elemento de par y el ultimo de impar
print('Resultado:',par[0]+impar[-1])

#ii) Restar el segundo elemento de par y el segundo impar 
print('Resultado:',par[1]-impar[1])

#iii)Multiplicar el ultimo elemento de par por el tercer de impar y anadirlo al final de la lista que corresponda
print('Resultado:',par[-1]*impar[2])
resultado=par[-1]*impar[2]
if resultado%2==0:
    par.append(resultado)
    print('El resultado de la multiplicacion fue par, se anade al final de la lista:',par[0:])
else:
    impar.append(resultado)
    print('El resultado de la multiplicacion fue impar, se anade al final de la lista:',impar[0:])
    
#iv)Dividir el segundo de impar entre el primer elemento de par y anadirlo al principo de la lista que corresponda
division=impar[3]//par[0]
if division%2==0:
    par.insert(0,division)
    print('El resultado de la division fue par, se anade al principio de la lista: ',par[0:])
else:
    impar.append(division)
    print('El resultado de la division fue impar, se anade al principio de la lista: ',impar[0:])
    
#v)Sumar el segundo elemento de impar + el tercer elemento de par + el ultimo de impar y anadirlo en el medio de la lista que corresponda
operacion=impar[1]+par[2]+impar[-1]

if operacion%2==0:
    par.insert(len(par)//2,operacion) 
    print('El resultado fue par, se anadio en el medio de la lista:',par[0:]) 
else:
    impar.insert(len(impar)//2,operacion) 
    print('El resultado fue impar,se anadio en el medio de la lista:',impar[0:])

#vi)Crear nueva lista y anadir las otras dos
c=[par]+[impar]
print('El contenido de la lista c es: ',c[0:])
