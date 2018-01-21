# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:14:28 2018

@author: mauri
"""

import PyPDF2
import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import matplotlib.style as style
style.use('ggplot')

def Leer_pdf(direc, pagina):
    """
    Esta función lee el archivo PDF e imprime el numero de paginas contenidas en el mismo.
    Se pide una pagina, la cual es la pagina del archivo que contiene el primer estado financiero.
    """
    pdf = open(direc, 'rb')
    pdf = PyPDF2.PdfFileReader(pdf)
    print("El documento contiene: ", pdf.numPages,  " paginas")
    finanzas = []
    for paginas in range((pagina-1), (int(pdf.numPages))):
        finanza = pdf.getPage(paginas).extractText()
        finanzas.append(finanza)
    return(finanzas)

def Estado_Consolidado_Ingresos(finanzas):
    """
    Esta función regresa una lista del estado consolidado de ingresos (Consolidated Income Statement). 
    """
    estados = {}
    finanzas = finanzas[0]
    try:
        inicio = finanzas.find('Revenues')
    except:
        inicio = None
        print('No se ha encontrado el string "Revenues"')
    try:
        fin = finanzas.find('Enron Corp. and Subsidiaries Consolidated Statement', inicio)
    except:
        fin = None
        print('No se ha encontrado fin de el Estado Consolidado de Ingresos')
    ECI = finanzas[inicio:fin]    
    estados['Consolidated Income Statement'] = re.findall('\d', ECI)
    return(estados)
    
def Balance_General_Consolidado(finanzas, estados):
    """
    Función para Consolidated Balance Sheet
    """
    Act = finanzas[1]
    inicio_act = Act.find('ASSETS')
    if inicio_act == -1:
        inicio_act = None
        print('No se ha encontrado el inicio del balance general: "ASSETS"')
    fin_act = Act.find('The accompanying notes are an integral part of these consolidated', inicio_act)
    if fin_act == -1:
        fin_act = None
        print('No se ha encontrado final del Balance General Consolidado')
    BGC_act = Act[inicio_act:fin_act]
    BS = {}
    BS['Assets'] = re.findall('\d', BGC_act)
    Pas = finanzas[2]
    inicio_pas = Pas.find('LIABILITIES AND SHAREHOLDERS')
    if inicio_pas == -1:
        inicio_pas = None
        print('No se ha encontrado el inicio del balance general: "Liabilities y equity"')
    BGC_pas = Pas[inicio_pas:]
    BS['Liabilities And Equity'] = re.findall('\d', BGC_pas)
    estados['Consolidated Balance Sheet'] = BS
    return(estados)

def Flujo_Efectivo_Consolidado(finanzas, estados):
    """
    Función para consolidated Cash Flows Statement
    """
    finanzas = finanzas[3]
    inicio = finanzas.find('Cash Flows From Operating Activities')
    if inicio==-1:
        inicio=None
        print('No se ha encontrado inicio del estado de flujo de efectivo')
    fin = finanzas.find('The accompanying notes are an integral part of these consolidated')
    if fin ==-1:
        fin = None
        print('No se ha encontrado final en el Estado de Fujos de efectivo consolidados')
    FEC = finanzas[inicio:fin]
    estados['Consolidated Statement of Cash Flows'] = re.findall('\d', FEC)
    return (estados)

def Cambios_Capital(finanzas, estados):
    """
    Función para Consolidated Statement Of Changes in Shareholders' Equity
    """
    finanzas = finanzas[4]
    inicio = finanzas.find('Cumulative Second Preferred Convertible Stock')
    if inicio ==-1:
        inicio = None
        print('No se ha encontrado inicio del Estado de cambios en el capital contable')
    fin = finanzas.find('The accompanying notes are an integral part of these consolidated')
    if fin ==-1:
        fin = None
        print('No se ha encontrado final del Estado de cambios en el capital contable')
    CC = finanzas[inicio:fin]
    estados["Consolidated Statement Of Changes in Shareholders' Equity"] = re.findall('\d', CC)
    return (estados)

def total(estados, numero_balance):
    """
    Función para la cuenta de repeticiones de los digitos de cada uno de los estados financieros.
    """
    total ={}
    estado = []
    for i in range(10):
        total['Cuenta'+str(i)] = 0
    for key in estados:
        estado.append(estados[key])
    if numero_balance != 1:
        for numero in estado[numero_balance]:
            if numero == '0':
                total['Cuenta0'] +=1
            elif numero == '1':
                total['Cuenta1'] +=1
            elif numero == '2':
                total['Cuenta2'] +=1
            elif numero == '3':
                total['Cuenta3'] +=1
            elif numero == '4':
                total['Cuenta4'] +=1 
            elif numero == '5':
                total['Cuenta5'] +=1
            elif numero == '6':
                total['Cuenta6'] +=1
            elif numero == '7':
                total['Cuenta7'] +=1
            elif numero == '8':
                total['Cuenta8'] +=1 
            else:
                total['Cuenta9'] += 1
    else:
        estado1 = estado[1]
        for llave in estado1:
            estado.append(llave)
        for numeros in estado:
            for numero in numeros:
                if numero == '0':
                    total['Cuenta0'] +=1
                elif numero == '1':
                    total['Cuenta1'] +=1
                elif numero == '2':
                    total['Cuenta2'] +=1
                elif numero == '3':
                    total['Cuenta3'] +=1
                elif numero == '4':
                    total['Cuenta4'] +=1 
                elif numero == '5':
                    total['Cuenta5'] +=1
                elif numero == '6':
                    total['Cuenta6'] +=1
                elif numero == '7':
                    total['Cuenta7'] +=1
                elif numero == '8':
                    total['Cuenta8'] +=1 
                else:
                    total['Cuenta9'] += 1
    return(total)

def total_totales(est1, est2, est3, est4):
    """
    Función que obtiene el total de todos los estados financieros.
    """
    suma_total = { k: est1.get(k, 0) + est2.get(k, 0) + est3.get(k, 0) + est4.get(k, 0) for k in set(est1) & set(est2) & set(est3) & set(est4) }
    return(suma_total)

def cada_uno(estados):
    """
    Regresa una lista de diccionarios con todos los estados financieros.
    """
    lista_tot = []
    for i in range(4):
        lista_tot.append(total(estados, i))
    est1 = lista_tot[0]
    est2 = lista_tot[1]
    est3 = lista_tot[2]
    est4 = lista_tot[3]
    return(lista_tot, est1, est2, est3, est4)
    
def convertir_df(lista_tot, suma_total):
    """
    Convierte un diccionario en un DataFrame, tomando como base la lista (con cada uno de los diccionarios).
    """
    df = pd.DataFrame.from_dict(suma_total, orient='index')
    count = 1
    for dic in lista_tot:
        df1 = pd.DataFrame.from_dict(dic, orient = 'index')
        df1.columns = [count]
        df = df.join(df1)
        count += 1
    df.columns = ['Total', 'Income Statement', 'Balance Sheet', 'Cash Flows', 'Changes Equity']
    df = df.sort_index()
    df = df.drop(df.index[0])
    return(df)
    
def graficar(df, cuenta):
    """
    Esta función grafica el numero de digitos vistos en los estados financieros de Enron.
    """
    espacio = ' '
    for name in range(10):
        df = df.rename(index={('Cuenta'+str(name)):name})
    fig, grafico = plt.subplots()
    grafico.bar(df.index, df[cuenta], width = 0.7, tick_label=df.index, color = 'darkorange')
    grafico.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)
    if cuenta == 'Total':
        grafico.text(x = 1.5, y = 385, s = 'Total de estados financieros - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        grafico.text(x = 0, y = -50,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        grafico.text(x = 1.5, y = 350, s= 'Cuenta de los dígitos en los estados financieros de Enron\npara detectar fraude usando la ley de Benford', fontsize = 15, alpha = 0.85)
    elif cuenta =='Balance Sheet':
        grafico.text(x = 2.5, y = 190, s = 'Consolidated Balance Sheet - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        grafico.text(x = 0, y = -25,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        grafico.text(x = 2.5, y = 170, s= 'Cuenta de los dígitos en los estados financieros de Enron\npara detectar fraude usando la ley de Benford', fontsize = 15, alpha = 0.85)
    elif cuenta == 'Cash Flows' or 'Income Statement':
        grafico.text(x = 2, y = 57, s = 'Consolidated ' + cuenta + ' - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        grafico.text(x = 0, y = -6,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        grafico.text(x = 2, y = 52, s= 'Cuenta de los dígitos en los estados financieros de Enron\npara detectar fraude usando la ley de Benford', fontsize = 15, alpha = 0.85)
    else:
        grafico.text(x = 2.5, y = 75, s = cuenta + ' - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        grafico.text(x = 0, y = -8,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        grafico.text(x = 2.5, y = 67, s= 'Cuenta de los dígitos en los estados financieros de Enron\npara detectar fraude usando la ley de Benford', fontsize = 15, alpha = 0.85)
    plt.show()

def data_frame_esperado(df):
    """
    Esta función crea un DataFrame con los valores esperados.
    Toma como referencia la cuenta total de digitos vista en los estados financieros de Enron.
    """
    benford = pd.Series([0.301, 0.176, 0.125, 0.097, 0.079, 0.067, 0.058, 0.051, 0.046], index = (range(1,10)))
    df_esperado = pd.DataFrame()
    for column in df.columns:
        serie = df[column].sum()
        serie = serie * benford
        df_esperado[column] = serie
    return(df_esperado)  

def graficar_comparacion(df_esperado, df, cuenta):
    """
    Esta función devuelve una gráfica comparando los valores esperados con los vistos en Enron.
    """
    espacio = ' '
    for name in range(10):
        df = df.rename(index={('Cuenta'+str(name)):name})
    bar_width = 0.43
    N = np.arange(1, 10)
    fig, ax = plt.subplots()
    ax.bar(N, df_esperado[cuenta], bar_width, color = 'mediumseagreen', label = 'Ley de Benford')
    ax.bar(N + bar_width, df[cuenta], bar_width ,color = 'orangered', label = 'Visto en Enron')
    ax.set_xticks(N + bar_width / 2)
    ax.set_xticklabels(range(1,10))
    plt.legend(loc = 'upper right')
    if cuenta == 'Total':
        ax.text(x = .5, y = 715, s = 'Comparación del total de estados financieros - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        ax.text(x = 0, y = -60,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        ax.text(x = 1.7, y = 650, s= 'Distribución de los primeros dígitos según la ley de Benford '+ r'$log _{10}\left(1+{\frac {1}{d}}\right)$'+'\nLos estados maquillados no estan distribuidos uniformemente', fontsize = 15, alpha = 0.85)
    elif cuenta =='Balance Sheet':
        ax.text(x = 1.5, y = 360, s = 'Comparación del Balance Sheet - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        ax.text(x = 0, y = -35,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        ax.text(x = 1.5, y = 320, s= 'Distribución de los primeros dígitos según la ley de Benford '+ r'$log _{10}\left(1+{\frac {1}{d}}\right)$'+'\nLos estados maquillados no estan distribuidos uniformemente', fontsize = 15, alpha = 0.85)
    elif cuenta == 'Cash Flows':
        ax.text(x = 2, y = 110, s = 'Comparación ' + cuenta + ' - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        ax.text(x = 0, y = -11,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        ax.text(x = 2, y = 100, s= 'Distribución de los primeros dígitos según la ley de Benford '+ r'$log _{10}\left(1+{\frac {1}{d}}\right)$'+'\nLos estados maquillados no estan distribuidos uniformemente', fontsize = 15, alpha = 0.85)
    elif cuenta == 'Income Statement':
        ax.text(x = 1.5, y = 98, s = 'Comparación '+ cuenta + ' - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        ax.text(x = 0, y = -8,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        ax.text(x = 1.5, y = 89, s= 'Distribución de los primeros dígitos según la ley de Benford '+ r'$log _{10}\left(1+{\frac {1}{d}}\right)$'+'\nLos estados maquillados no estan distribuidos uniformemente', fontsize = 15, alpha = 0.85)
    else:
        ax.text(x = 1.5, y = 140, s = 'Comparación '+ cuenta + ' - Corporación Enron', fontsize = 20, weight = 'bold', alpha = 0.75)
        ax.text(x = 0, y = -11,
        s = '   ©Mauricio Mani'+ espacio*115 +'Source: Enron Annual Report                ',
        fontsize = 12, color = '#f0f0f0', backgroundcolor = 'grey')
        ax.text(x = 1.5, y = 128, s= 'Distribución de los primeros dígitos según la ley de Benford '+ r'$log _{10}\left(1+{\frac {1}{d}}\right)$'+'\nLos estados maquillados no estan distribuidos uniformemente', fontsize = 15, alpha = 0.85)
    plt.show()
    
def prueba_chi(df, df_esperado, estado):
    """
    Esta función realiza una Prueba X^2 de bondad de ajuste.
    """
    print('Prueba X^2 de bondad de ajuste:')
    chi, p = sp.chisquare(df[estado], f_exp=df_esperado[estado])
    print(estado)
    print('El valor de la prueba X^2 es: ', chi ,'El p-value es: ', p)
    return(chi, p)

def ks_test(df, estado):
    """
    Esta función realiza una prueba Kolmogorov-Smirnov.
    """
    xk = np.arange(1,10)
    pk = []
    for x in xk:
        pk.append(np.log10(1+(1/x)))
    Bdist = sp.rv_discrete(a = 1, b = 9, name = 'Bdist', values = (xk, pk))
    visto = np.array(df[estado])
    n=sum(visto)
    visto = visto/n
    Bdist1 = sp.rv_discrete(a=1, b=9, name = 'Bdist1', values = (xk, visto))
    real = []
    visto = []
    for i in range(1, 10):
        real.append(Bdist1.cdf(i))
        visto.append(Bdist.cdf(i))
    real =np.array(real)
    visto = np.array(visto)
    ks = (np.absolute(visto - real)).max()
    print('Prueba Kolmogorov-Smirnov')
    plt.figure()
    plt.plot(xk, real, label = 'Distribución Enron')
    plt.plot(xk, visto, label = 'Ley de Benford')
    plt.title('Comparación de la distribución acumulada. Prueba Kolmogorov-Smirnov')
    plt.legend()
    plt.show()
    print('H0 = La distribución cumulatva vista y esperada son iguales')
    print('H1 = La distribución cumulatva vista y esperada no son iguales')
    valor_D = 1.63/np.sqrt(n-1)
    print('El valor "D" de la prueba Kolmogorov-Smirnov con alpha = 0.01 es: ', valor_D)
    if valor_D > ks:
        print(valor_D, ' > ', ks, 'No hay pruebas suficientes para reachazar la hipotesis nula')
    else:
        print(ks, ' > ', valor_D, 'Hay pruebas suficientes para rechazar la hipotesis nula')
    return(ks)

def grafica_relativa(df, df_esperado, cuenta):
    """
    Esta función regresa 2 graficas. 
    La primera regresa los porcentajes de la cuenta de cada uno de los digitos.
    La segunda regresa una comparación entre los porcentajes esperados y los vistos.
    """
    for name in range(10):
        df = df.rename(index={('Cuenta'+str(name)):name})
    relativo = df[cuenta]/(df[cuenta].sum())
    relativo_esperado = df_esperado[cuenta]/(df_esperado[cuenta].sum())
    fig, grafico = plt.subplots()
    grafico.bar(df.index, relativo, width = 0.7, tick_label=df.index, color = 'darkorange')
    grafico.axhline(y = 0, color = 'black', linewidth = 1.3, alpha = .7)
    plt.title('Observación relativa de: ' + cuenta)
    grafico.set_ylabel('% de aparición')
    plt.show()
    bar_width = 0.43
    N = np.arange(1, 10)
    fig, ax = plt.subplots()
    ax.bar(N, relativo_esperado, bar_width, color = 'mediumseagreen', label = 'Ley de Benford')
    ax.bar(N + bar_width, relativo, bar_width ,color = 'orangered', label = 'Visto en Enron')
    ax.set_xticks(N + bar_width / 2)
    ax.set_xticklabels(range(1,10))
    ax.set_ylabel('% de aparición')
    ax.legend(loc = 'upper right')
    plt.title('Comparación de las observaciones relativas de ' + cuenta)
    plt.show()
    

def todo(direc, pagina, cuenta):
    """
    Esta función compila todas las demas funciones y regresa un DataFrame con la información de la cuenta de digitos
    en los estados financieros de Enron.
    Direc, es la dirección de el PDF que contiene los estados financieros de Enron.
    Pagina es el numero de pagina en donde se inician los estados financieros del PDF de Enron
    Las posibles cuentas son: 'Total', 'Income Statement', 'Balance Sheet', 'Cash Flows' y  'Changes Equity'
    """
    finanzas = Leer_pdf(direc, pagina)
    estados = Estado_Consolidado_Ingresos(finanzas)
    estados = Balance_General_Consolidado(finanzas, estados)
    estados = Flujo_Efectivo_Consolidado(finanzas, estados)
    estados = Cambios_Capital(finanzas, estados)
    lista_tot, est1, est2, est3, est4 = cada_uno(estados)
    suma_total = total_totales(est1, est2, est3, est4)
    df = convertir_df(lista_tot, suma_total)
    df_esperado = data_frame_esperado(df)
    graficar(df, cuenta)
    graficar_comparacion(df_esperado, df, cuenta)
    grafica_relativa(df, df_esperado, cuenta)
    prueba_chi(df, df_esperado, cuenta)
    ks_test(df, cuenta)
    return(df)
    

if __name__ =='__main__':
    df = todo("C:/Users/mauri/Desktop/Big Data/Portfolio/Enron/EnronAnnualReport2000.pdf", 33, 'Cash Flows')

