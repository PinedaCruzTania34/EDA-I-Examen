import os
os.system("cls")
#Sistema indicador de color de semáforo COVID
op='0'
promedio=[]
datos=[]
contagios=[]
indicador=[]
ind=[]

print("\n\n\t\t\tBienvenido a nuestro sistema semáforo COVID")
while(op!='2'):
    print("\n 1) Ingresar\n 2) Salir\n")
    op=input("Elige una opción: ")
    if op=='1':
        edad=float(input("\nIngrese su edad: "))
        indicador=float(input("\nIndicador [0-1]: "))
        if (indicador)>= .8 and (indicador)<=1.0:
            indicador=str(indicador)
            edad=str(edad)
            regSi=edad+','+indicador+"Positivo"+'\n'
            indicador=float(indicador)
            datos.append(regSi)
            promedio.append(float(edad))
            print("\n\tPositivo a Covid\n")
            
            ind.append(str(indicador))
            
        elif (indicador)< .8 and (indicador)>= 0:
            print("\n\tNegativo a Covid\n")
            indicador=str(indicador)
            edad=str(edad)
            regNo=edad+','+indicador+','+"Negativo"+'\n'
            indicador=float(indicador)
            datos.append(regNo)
        else:
            print("\nError")
    elif op=='2':
        print("\n\n\t\tGracias por ingresar a nuestro sistema, no olvides cuidarte")
    else:
        print("\nError")

contagios=len(ind)

if contagios == 0:
    print("\n\n\t\t\t\t\tSEMÁFORO VERDE")
elif contagios>=1 and contagios<=30:
    print("\n\n\t\t\t\t\tSEMÁFORO AMARILLO")
elif contagios>=31 and contagios<=70:
    print("\n\n\t\t\t\t\tSEMÁFORO ANARANJADO")
else:
    print("\n\n\t\t\t\t\tSEMÁFORO ROJO (ALERTA)")

if sum(promedio)!=0:
    print("\nLa edad promedio de las personas que presentaron COVID es de: ",sum(promedio)/len(promedio))

a=open ("bd.csv","a")
a.writelines(datos)
a.close()

a=open("bd.csv",'r')
contenido=a.readlines()
a.close()
print(contenido)