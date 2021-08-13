#INGRESO
from time import sleep
from math import pi
#Función para ingresar una cadena y verificar que sea un entero positivo
def chknum():
    while True:
        a = input()
        try:
            a = int(a)
            if a<=0:
                print("\nAsegurar que el valor introducido sea positivo\n\nIntroducir valor: ",end="")
            else:
                break
        except ValueError:
            sleep(0.5)
            print("\nValor no válido, intentar con un entero positivo\n\nIngresar valor: ",end="")
    return(a)
#Función para ingresar una cadena y verificar que sea un float positivo
def chkflt(b):
    while True:
        sleep(0.4)
        a = input()
        try:
            a = float(a)
            if a<=0:
                print("\nAsegurar que el valor introducido sea positivo\n\nIntroducir %s: "%b,end="")
            else:
                break
        except:
            print("\nAsegurar que el valor introducido sea un número\n\nIntroducir %s: "%b,end="")
    return(a)
#Función para centrar una cadena o variable (lrg=espacio que abarca, tit=cadena o variable)
def ptit(lrg,tit):
    print("{1:^{0}}".format(lrg,tit))
#Función para imprimir dos columnas centradas (lrg=espacio que abarca, itm=variable-columna1 vlr=variable-columna2)
def pfil(lrg,itm,vlr):
    print("{1:^{0}}{2:^{0}}".format(lrg,itm,vlr))
#Función para generar la serie de fibonacci
def fibo(vact,b,a=0,ifib=0):
    sep = ", "
    ifib += 1
    if ifib == b:
        sep = " "
    print(a, end=sep)
    a += vact
    if ifib < b:
        #los valores de 'a' y 'vact' intercambian de lugar en cada invocación
        fibo(a,b,vact,ifib)
#Función para detectar si una cadena ingresada es un palíndromo
def pldr(a):
    lpld = []
    chk=True
    a = a.upper()
    #se crea una lista con cada caracter de la cadena ingresada
    for i in a:
        lpld.append(i)
    nltr = len(lpld)-1
    for i in range(nltr):
        #si los carácteres 'espejo' son distintos, la cadena no es un palíndromo
        if lpld[i] != lpld[nltr-i]:
            chk = False
            break
    return chk
#Función para el problema 1:
def p1():
    print("SUCESIÓN DE FIBONACCI:")
    print("-"*24)
    print("Introducir valor que le seguirá al cero en la serie: ",end="")
    numi = chknum()
    print("Introducir número de elementos que desea observar en la serie: ",end="")
    tser = chknum()
    print("")
    #si tser=0 se cancela la serie, ya que no se desea observar ningún elemento de la serie.
    if tser != 0:
        fibo(numi,tser)
    else:
        sleep(0.6)
        print("Serie cancelada")
    print()
#Función para el problema 2:
def p2():
    print("PALÍNDROMO:")
    print("-"*13)
    print("Ingresar cadena: ",end="")
    a = input()
    #se apreovecha que la función pldr retorna un valor booleano para imprimir si la cadena es o no un palíndromo
    chk = {True:"Es palindromo", False:"No es palindromo"}
    print(chk[pldr(a)])
#Función para el problema 3:
def p3():
    print("Volumen de un cilindro: \n(Importante: Introducir los valores en la misma unidad)")
    print("-"*45)
    #Para la introducción de r y h se utiliza la función que verifica que estos sean números enteros o float positivos
    print("Introducir radio de la base: ",end="")
    r = chkflt("radio")
    print("Introducir altura: ",end="")
    h = chkflt("altura")
    v = pi*(r**2)*h
    print("\n"+"-"*lcvol)
    ptit(lcvol,"VOLUMEN - CILINDRO")
    print("-"*lcvol)
    pfil(lclm,"ÍTEM","MEDIDA")
    pfil(lclm,"Radio",r)
    pfil(lclm,"Altura",h)
    print("-"*lcvol)
    pfil(lclm,"Volumen",round(v,3))
    print("-"*lcvol)
#Función para el problema 4:
def p4():
    print("Cálculo de descuento:")
    print("-"*20)
    print("Ingresar sueldo: ",end="")
    sld = chkflt("sueldo")
    while True:
        print("\nSeleccionar:\n1.AFP\n2.ONP\nOpción: ",end="")
        i = chknum()
        if 1<= i <= 2:
            if i == 1:
                dsc = sld*0.12
                a = "AFP"
            elif i == 2:
                dsc = sld*0.13
                a = "ONP"
            break
        else:
            print("\nValor fuera de los parámetros")
    snt = sld-dsc
    print()
    ptit(lcvol,"DESCUENTO PENSIÓN")
    print("-"*lcvol)
    pfil(lclm,"Sdo. Inicial",round(sld,2))
    pfil(lclm,"Descuento %s"%a,round(dsc,2))
    print("-"*lcvol)
    pfil(lclm,"Sdo. Final",round(snt,2))
    print("-"*lcvol)
#Función para el problema 5:
def p5():
    print("CUOTA DE AMORTIZACIÓN:")
    print("-"*25)
    print("Introducir cuantía: ",end="")
    c = chkflt("cuantía")
    print("Introducir tasa de interés (%): ",end="")
    i = chkflt("tasa de interés (%)")/100
    print("Introducir número de cuotas: ",end="")
    n = chkflt("número de cuotas")
    f = (1+i)**n
    a = (c*f*i)/(f-1)
    print()
    ptit(lcvol,"CUOTA DE AMORTIZACIÓN")
    print("-"*lcvol)
    pfil(lclm,"Cuantía",round(c,2))
    pfil(lclm,"Interés (%)",round(i*100,2))
    pfil(lclm,"Num. de cuotas",round(n,2))
    print("-"*lcvol)
    pfil(lclm,"Amortización",round(a,2))
    print("-"*lcvol)
#Función para imprimir las conclusiones:
def p6():
    print("CONCLUSIONES:\nLa creación de funciones permite un mejor desarrollo de código y mantener el orden en el mismo.\nAl crear una función se puede hacer de tal forma que este sea lo más reutilizables posible y permita una continua reducción de líneas en el código.")
#Largo
lclm = 17
lmen = 28

#PROCESO
lcvol = 2*lclm

#SALIDA
while True:
    sleep(0.8)
    ptit(lmen,"MENÚ")
    print("-"*lmen)
    print("1. Fibonacci\n2. Palíndromo\n3. Volumen - cilindro\n4. Cálculo de pensión\n5. Cuota de amortización\n6. Conclusiones\n7. Salir")
    print("-"*lmen)
    print("Opción: ",end="")
    #Evitamos repetición de código gracias a la función que verifica que el valor sea entero, y solo se necesita verificar que esté dentro del intervalo de las opciones
    i = chknum()
    if 1<= i <=7:
        print()
        if i == 1:
            p1()
        elif i == 2:
            p2()
        elif i == 3:
            p3()
        elif i == 4:
            p4()
        elif i == 5:
            p5()
        elif i == 6:
            p6()
        elif i == 7:
            break
        print()
    else:
        print("\nValor fuera de los parámetros")