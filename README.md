Uno de los mayores fraudes de la historia
--------------------------------------------

#Traducciones:
* [Español](README.md)
* [Ingles](README-en.md)

A través de la Ley de Benford descubriras los fraudes contables en los estados financieros de Enron del año 1998, 1999 y 2000.
Podrás visualizar la aparición de los digitos en cada uno de los cuatro estados mas importantes generados por la empresa, 
generaras dos pruebas estadísticas para la aparición de ciertos digitos o unos mas extremos.

## Estados Financieros:
> Tiene como fin indicar la posición financiera de un ente económico en una fecha determinada. Es una fotografía de la empresa en un momento del tiempo.

El estado financiero de una empresa muestra si sus finanzas son sanas. Para invertir en una empresa, queremos que esta gane mucho dinero
y deba muy poco. Si la empresa tiene mas ingresos es una buena opción para invertir ya que el reparto de dividendos (comunmente) será mayor.
Los estados contables son importantes para los analistas financieros, ya que estos les permiten tomar decisiones sobre comprar 
o vender sus posiciones de la empresa. Aquellos que poseen muchas acciones de la empresa (o que son dueños) les conviene que la acción suba
de precio. Pero no solo sirve para que las acciones suban de precio, tambien sirve para que te den prestamos.
Pero, ¿porque no inventar los numeros, en pocas palabras, fingir tener más ganancias y menos perdidas? Debido a que a eso se le llama 
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
Enron fue una empresa energética. Al principio se dedicaba a la administración de gasoductos 
luego expandió sus operaciones como intermediario de los contratos de futuros y derivados del gas natural 
y la construcción y operación de gasoductos y plantas de energía por todo el mundo. 
En 1997 llegó como COO (Chief Operations Officer) Jeff Skilling, esperando que los beneficios aumentaran
pero estos no lo hacian. La gente de Enron recibia su salario en acciones, por lo que les importaba que 
subieran de precio y harían lo que fuera para lograrlo.
Enron era auditada por Arthur Andersen esta empresa fue fundada en 1913 y desapareció en el 2002 debido a las operaciones contables
fraudulentas que cubrió en Enron, recibian alrededor de $1,000,000 de dólares semanales.
En agosto del año 2000 lograron una cotización de $ 90.56 dólares por cada acción. Para el año 2001 empezaron 
a descender hasta que el 2 de diciembre pidieron protección por bancarrota.
Debido a que la empresa Enron era auditada por Arthur Andersen, nadie creía que se estuvieran maquillando los estados.

> Publicación intencionada de información falsa en cualquier parte de un estado financiero.  

Si sabes que tus finanzas no son sanas vendes tus acciones (carísimas) antes de que todos se den cuenta. Para la quiebra en 2001
Kenneth Lay había vendido 300 millones de acciones y Jeff Skilling 200 millones. 
Si deseas saber mas información hay miles de articulos y documentales. 

## Ley de Benford
La idea de analizar las finanzas del caso Enron fue debido a un capitulo en el libro "la seducción de las matemáticas" 
dedicado a la ley de Benford. Los numeros que genera un humano no siguen la ley de Benford.
> Los numeros que aparecen en la naturaleza siguen una distribución particular.

<br/>
<p align="center">
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/46/Rozklad_benforda.svg/220px-Rozklad_benforda.svg.png" alt="Benford">
</p><br/>
Según la ley de Benford el numero 1 aparece con mayor frecuencia que el numero 2, y el número 2 aparece con mayor frecuencia que 
el numero 3 y así sucevivamente. El ser humano cuando va inventar numeros, quiere que estos parezcan lo mas aleatorios posibles.
Y por alguna razón cree que el 1 o el 3 no son tan aleatorios como el 6, 7 y 8. Por lo que los repite con mayor frecuencia.

## Pruebas estadísticas.
Realizaras dos pruebas estadísticas:
* X^2 de bondad de ajuste.
* Kolmogorov-Smirnov. Se basa en la diferencia maxima de la distribucion acumulada vista vs. la esperada.

## Mayor generalización.
Para analizar distintos estados en diferenetes archivos y de diferentes empresas. 
Usaría `input` para ingresar tanto el string en donde inicia el estado y otro para
donde termina. Por lo demás este código te puede servir para generalizar.

