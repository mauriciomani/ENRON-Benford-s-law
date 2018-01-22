Uno de los mayores fraudes de la historia
--------------------------------------------

#Traducciones:
* [Espa�ol](README.md)
* [Ingles](README-en.md)

A trav�s de la Ley de Benford descubriras los fraudes contables en los estados financieros de Enron del a�o 1998, 1999 y 2000.
Podr�s visualizar la aparici�n de los digitos en cada uno de los cuatro estados mas importantes generados por la empresa, 
generaras dos pruebas estad�sticas para la aparici�n de ciertos digitos o unos mas extremos.

## Estados Financieros:
> Tiene como fin indicar la posici�n financiera de un ente econ�mico en una fecha determinada. Es una fotograf�a de la empresa en un momento del tiempo.

El estado financiero de una empresa muestra si sus finanzas son sanas. Para invertir en una empresa, queremos que esta gane mucho dinero
y deba muy poco. Si la empresa tiene mas ingresos es una buena opci�n para invertir ya que el reparto de dividendos (comunmente) ser� mayor.
Los estados contables son importantes para los analistas financieros, ya que estos les permiten tomar decisiones sobre comprar 
o vender sus posiciones de la empresa. Aquellos que poseen muchas acciones de la empresa (o que son due�os) les conviene que la acci�n suba
de precio. Pero no solo sirve para que las acciones suban de precio, tambien sirve para que te den prestamos.
Pero, �porque no inventar los numeros, en pocas palabras, fingir tener m�s ganancias y menos perdidas? Debido a que a eso se le llama 
"fraude" y es un delito. Por ello las empresas deben ser auditadas, se le llama auditoria externa y se encarga de verificar que lo que 
muestran los estados financieros de la empresa sea cierto.

## Tipos de estados:
* Estado de resultados: `Income Statement`.
* Balance general: `Balance Sheet`.
* Estado de Fujo de efectivo: `Cash Flows`.
* Cambios en el capital contable: `Changes Equity`.

## Caso Enron.
<br/>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Logo_de_Enron.svg/1200px-Logo_de_Enron.svg.png" alt="Enron">
</p><br/>
Enron fue una empresa energ�tica. Al principio se dedicaba a la administraci�n de gasoductos 
luego expandi� sus operaciones como intermediario de los contratos de futuros y derivados del gas natural 
y la construcci�n y operaci�n de gasoductos y plantas de energ�a por todo el mundo. 
En 1997 lleg� como COO (Chief Operations Officer) Jeff Skilling, esperando que los beneficios aumentaran
pero estos no lo hacian. La gente de Enron recibia su salario en acciones, por lo que les importaba que 
subieran de precio y har�an lo que fuera para lograrlo.
Enron era auditada por Arthur Andersen esta empresa fue fundada en 1913 y desapareci� en el 2002 debido a las operaciones contables
fraudulentas que cubri� en Enron, recibian alrededor de $1,000,000 de d�lares semanales.
En agosto del a�o 2000 lograron una cotizaci�n de $ 90.56 d�lares por cada acci�n. Para el a�o 2001 empezaron 
a descender hasta que el 2 de diciembre pidieron protecci�n por bancarrota.
Debido a que la empresa Enron era auditada por Arthur Andersen, nadie cre�a que se estuvieran maquillando los estados.

> Publicaci�n intencionada de informaci�n falsa en cualquier parte de un estado financiero.  

Si sabes que tus finanzas no son sanas vendes tus acciones (car�simas) antes de que todos se den cuenta. Para la quiebra en 2001
Kenneth Lay hab�a vendido 300 millones de acciones y Jeff Skilling 200 millones. 
Si deseas saber mas informaci�n hay miles de articulos y documentales. 

## Ley de Benford
La idea de analizar las finanzas del caso Enron fue debido a un capitulo en el libro "la seducci�n de las matem�ticas" 
dedicado a la ley de Benford. Los numeros que genera un humano no siguen la ley de Benford.
> Los numeros que aparecen en la naturaleza siguen una distribuci�n particular.

<br/>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Rozklad_benforda.svg/220px-Rozklad_benforda.svg.png" alt="Benford">
</p><br/>
Seg�n la ley de Benford el numero 1 aparece con mayor frecuencia que el numero 2, y el n�mero 2 aparece con mayor frecuencia que 
el numero 3 y as� sucevivamente. El ser humano cuando va inventar numeros, quiere que estos parezcan lo mas aleatorios posibles.
Y por alguna raz�n cree que el 1 o el 3 no son tan aleatorios como el 6, 7 y 8. Por lo que los repite con mayor frecuencia.

## Pruebas estad�sticas.
Realizaras dos pruebas estad�sticas:
* X^2 de bondad de ajuste.
* Kolmogorov-Smirnov. Se basa en la diferencia maxima de la distribucion acumulada vista vs. la esperada.

## Mayor generalizaci�n.
Para analizar distintos estados en diferenetes archivos y de diferentes empresas. 
Usar�a `input` para ingresar tanto el string en donde inicia el estado y otro para
donde termina. Por lo dem�s este c�digo te puede servir para generalizar.

