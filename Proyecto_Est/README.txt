                                    ***************************************************
                                      Bienvenidos a mi proyecto final de estadistica!
                                    ***************************************************


|--------------------------------------------------------------------------------------------------------------------------|
  El objetivo de este proyecto fue aplicar lo aprendido en Lenguaje C utilizando los recursos aprendidos en clase asi como
                       resolver problemas estadisticos que vimos en clase de Estadistica avanzada.
|--------------------------------------------------------------------------------------------------------------------------|




\\--------------------------------------------------------------------------------------------------------------------------//

    En este proyecto se vera lo siguiente:
    
        * Rutinas con Graficos:
            -Tallos y hojas
            -Grafica de puntos
            -Histograma
    
        * Rutinas para calcular:
            -Moda
            -Media
            -Media recortada
            -Mediana
            -Varianza y desviacion estandar
    
        * Rutinas para tablas Z y T:
            -Calcular Area bajo la curva(Tabla z)
            -Encontrar Z con alpha
            -Localizar T
            -Localizar grados de libertad y T
            -Diagrama de dispercion y regresion lineal

\\--------------------------------------------------------------------------------------------------------------------------//




~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

                                                **Instrucciones de uso**

    * Al correr este programa se abrira un menu que te dara la bienvenida y te mostrara todas las opciones de rutinas
      estadisticacs que hay. Tendras 13 opciones de rutinas.

    * Al escoger una rutina el programa te hara una pregunta " Deseas leer los datos de un archivo(1), o proporcionarlos
     tu(2)?" si escogs la opcion de leer de un archivo la rutina se encargara de leer el archivo con los datos y despues
     te dara el resultado esperado de la opcion que elegiste. Si escoges la opcion de proporcionarlos tu, el programa te
     preguntara cuantos datos seran y despues de dira que los proporciones de uno por uno, una ve dados los datos te 
     dara el resultado esperado de la opcion que elegiste. Una vez te de el resultado se te dara la bienvenida de nuevo 
     y se te mostrara nuevamente el menu con todas las opciones.

    * Al final del menu esta la opcion para poder salir del programa

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~




++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

                                            **Funcionamiento de cada rutina**


    -Tallos y hojas

        -> Descripción: Genera un gráfico de tallos y hojas para representar datos numéricos.

        -> Funcionalidad: Esta opción ejecuta un programa externo que crea un gráfico de tallos y hojas.
           este porgrama funciona de la siguiente manera:

            |> Inicio del Programa:
            
                El programa presenta un menú al usuario para elegir entre dos opciones: leer datos de un archivo
                o ingresarlos manualmente.

            |> Lectura de Datos:

                Si el usuario elige leer datos de un archivo, el programa cuenta los elementos en el archivo, asigna memoria para los
                datos y los lee desde el archivo.

                Si el usuario elige ingresar datos manualmente, el programa pide al usuario la cantidad de valores y luego solicita cada
                valor, almacenándolos en el arreglo.

            |> Dibujo de la Gráfica:

                El programa ordena los datos.

                Luego, inicializa una ventana gráfica y dibuja la gráfica de tallos y hojas, separando los datos en tallos y hojas.

                Cada tallo se representa por los dígitos principales y cada hoja por los dígitos restantes.

            |> Finalización del Programa:

                El programa espera a que el usuario presione una tecla para cerrar la ventana gráfica.

                Finalmente, libera la memoria asignada para los datos.


    -Grafica de puntos

        ->Descripción: Genera una gráfica de puntos para visualizar datos individuales.

        ->Funcionalidad: Al seleccionar esta opción, el programa ejecuta un archivo externo que crea una gráfica de puntos.
          este porgrama funciona de la siguiente manera:

            |> Inicio del Programa:
            
                El programa presenta un menú al usuario para elegir entre dos opciones: leer datos de un archivo o ingresarlos manualmente.

            |> Lectura de Datos:

                Si el usuario elige leer datos de un archivo, el programa cuenta los elementos en el archivo, asigna memoria
                para los datos y los lee desde el archivo.

                Si el usuario elige ingresar datos manualmente, el programa pide al usuario la cantidad de valores y luego
                solicita cada valor, almacenándolos en el arreglo.

            |> Dibujo de la Gráfica:

                El programa inicializa una ventana gráfica.
                
                Encuentra el valor máximo en los datos para determinar la escala del eje Y.
                
                Define márgenes y escalas para dibujar los puntos.
                
                Dibuja los ejes y las etiquetas del eje X.
                
                Agrupa los datos por valores y dibuja los puntos en la gráfica, apilando los puntos verticalmente si hay duplicados.
                
                Espera a que el usuario presione una tecla para cerrar la ventana gráfica.

            |> Finalización del Programa:

                El programa cierra la ventana gráfica.

                Finalmente, libera la memoria asignada para los datos.

    
    -Histograma

        ->Descripción: Genera un histograma para visualizar la distribución de frecuencias de los datos.

        ->Funcionalidad: Esta opción ejecuta un programa externo que genera un histograma. Un histograma muestra la frecuencia
         de los datos en intervalos específicos. Este porgrama funciona de la siguiente manera:

            |> Inicio del Programa:
            
                El programa presenta un menú al usuario para elegir entre dos opciones: leer datos de un archivo o
                ingresarlos manualmente.

            |> Lectura de Datos:

                Si el usuario elige leer datos de un archivo, el programa cuenta los elementos en el archivo, asigna memoria
                para los datos y los lee desde el archivo.

                Si el usuario elige ingresar datos manualmente, el programa pide al usuario la cantidad de valores y luego 
                solicita cada valor, almacenándolos en el arreglo.
                
            |> Dibujo de la Gráfica:
                
                El programa inicializa una ventana gráfica.
                
                Encuentra el valor máximo en los datos para determinar la escala del eje Y.
                
                Define el tamaño y la posición de las barras del histograma.
                
                Dibuja las barras del histograma, cada una representando la frecuencia de los datos.
                
                Añade etiquetas a las barras para mostrar los valores.
                
                Espera a que el usuario presione una tecla para cerrar la ventana gráfica.

            |> Finalización del Programa:

                El programa cierra la ventana gráfica.
                
                Finalmente, libera la memoria asignada para los datos.
                

    -Moda

        ->Descripción: 

            Calcula y muestra la moda de un conjunto de datos.

        ->Funcionalidad:
            
            El usuario puede elegir entre ingresar los datos manualmente o leerlos desde un archivo.
            
            Si se eligen datos manuales, el usuario debe especificar el tamaño del arreglo y luego ingresar cada valor.
            
            Si se opta por leer desde un archivo, el programa leerá los datos de un archivo de texto.
            
            El programa ordena los datos y calcula la moda, que es el valor que aparece con mayor frecuencia en el conjunto 
            de datos. La moda es especialmente útil para datos categóricos o para identificar el valor más común en un 
            conjunto de datos numéricos.

    -Media

        ->Descripción: 
            
            Calcula y muestra la media (promedio) de un conjunto de datos.

        ->Funcionalidad:

            El usuario puede ingresar datos manualmente o leerlos desde un archivo.
            
            El programa suma todos los valores y los divide por el número total de valores para calcular la media.
            
            La media proporciona una medida central del conjunto de datos, indicando el valor promedio.


    -Media recortada

        ->Descripción: 
            
            Calcula y muestra la media recortada de un conjunto de datos.

        ->Funcionalidad:
            
            El usuario puede ingresar los datos manualmente o leerlos desde un archivo.
            
            El programa solicita un porcentaje de recorte, eliminando los valores más altos y más bajos en función de este porcentaje.
            
            Luego, calcula la media de los valores restantes.
            
            La media recortada es útil para reducir el impacto de valores atípicos en la medida central.

    -Mediana

        ->Descripción: 
            
            Calcula y muestra la mediana de un conjunto de datos.

        ->Funcionalidad:
            
            El usuario puede ingresar los datos manualmente o leerlos desde un archivo.
            
            El programa ordena los datos y encuentra el valor central. Si el número de valores es par, la mediana es el promedio de los dos valores centrales.
            
            La mediana es una medida robusta de la centralidad, especialmente útil cuando los datos contienen valores atípicos.

    -Varianza y desviacion estandar

        ->Descripción: 
            
            Calcula y muestra la varianza y la desviación estándar de un conjunto de datos.

        ->Funcionalidad:
            
            El usuario puede ingresar los datos manualmente o leerlos desde un archivo.
            
            El programa calcula la media de los datos y luego utiliza dos fórmulas diferentes para calcular la varianza:
                
                |>Fórmula 1: Suma de los cuadrados de las diferencias entre cada valor y la media, dividida por el número de valores menos uno.
                
                |>Fórmula 2: Utiliza la suma de los cuadrados de los valores y la suma de los valores para calcular la varianza.

            La desviación estándar es la raíz cuadrada de la varianza.

            Estas medidas indican la dispersión de los datos alrededor de la media. La varianza mide el promedio de las desviaciones al cuadrado, 
            y la desviación estándar proporciona una medida de dispersión en las mismas unidades que los datos originales.

    -Calcular área bajo la curva (Tabla Z)

        ->Descripción: Calcula y grafica el área bajo la curva normal estándar utilizando la tabla Z.
            

        ->Funcionalidad:

            Esta opción ejecuta un programa externo que muestra la gráfica del área bajo la curva de una distribución normal estándar.
            Este porgrama funciona de la siguiente manera:

            |> Inicio del Programa:
            
                 El programa solicita al usuario que ingrese un valor para 'z'

            |>Cálculo de la PDF y CDF:
                
                La función normal_pdf calcula la función de densidad de probabilidad de la distribución normal estándar.
                
                La función normal_cdf calcula la función de distribución acumulativa utilizando el método del trapecio.

            |> Gráfico de la Distribución Normal Estándar:

                La función plot_normal_distribution inicializa una ventana gráfica.
                
                Dibuja los ejes X e Y.
                
                Grafica la curva de la distribución normal estándar ajustando la escala para visualizar mejor la gráfica.
                
                Rellena el área bajo la curva desde -5 hasta z utilizando líneas verticales.

            |> Finalización del Programa:
                
                El programa espera a que el usuario presione una tecla para cerrar la ventana gráfica.

                Finalmente, cierra la ventana gráfica y termina el programa.
                


    -Encontrar Z con alpha

        ->Descripción: 
        
        Calcula el valor Z correspondiente a un nivel de significancia (alpha).    

        ->Funcionalidad:

            El usuario puede elegir entre calcular Za o Za/2

            El programa solicita el valor de alpha

            Luego, calcula el valor Z que corresponde al área acumulada 

            Este valor Z es utilizado en pruebas de hipótesis para determinar los límites críticos.



    -Localizar T

        ->Descripción:
        
            Busca el valor T correspondiente a grados de libertad (gdl) y un nivel de significancia (alpha).    

        ->Funcionalidad:
            
            El usuario ingresa los grados de libertad y el nivel de significancia.
            
            El programa lee la tabla T desde un archivo, busca la fila correspondiente a los grados de libertad y la columna correspondiente al nivel de significancia.
            
            Luego, muestra el valor T encontrado, que es utilizado en pruebas t para determinar los límites críticos.


    -Localizar grados de libertad y T

        ->Descripción: 
            
            Busca los grados de libertad y el nivel de significancia que corresponden a un valor T especificado.

        ->Funcionalidad:
            
            El usuario ingresa el valor T.
            
            El programa lee la tabla T desde un archivo y busca la combinación de grados de libertad y nivel de significancia más cercana al valor T especificado.
            
            Luego, muestra los grados de libertad y el nivel de significancia encontrados, lo cual es útil para interpretar resultados de pruebas t.


    -

        ->Descripción: 
        
        Genera un diagrama de dispersión y realiza una regresión lineal para mostrar la relación entre dos conjuntos de datos.    

        ->Funcionalidad:

        Esta opción ejecuta un programa externo que crea un diagrama de dispersión, donde cada par de datos se representa como un punto en el gráfico.
        Este porgrama funciona de la siguiente manera:
            
            |> Inicio del Programa:
            
                El programa presenta un menú al usuario para elegir entre dos opciones: leer datos de un archivo o ingresarlos manualmente.

            |> Lectura de Datos:

                Si el usuario elige leer datos de un archivo, el programa lee los datos X e Y desde el archivo.

                Si el usuario elige ingresar datos manualmente, el programa solicita al usuario que ingrese los valores para las coordenadas X e Y.
                
            |> Dibujo de la Gráfica:
                
                El programa inicializa una ventana gráfica para dibujar el diagrama de dispersión.

                El programa dibuja cada punto en el gráfico usando las coordenadas X e Y proporcionadas.

            |> Cálculo de la Regresión Lineal:
                
                El programa calcula los parámetros de la línea de regresión (pendiente m y la intersección b).
                
                Dibuja la línea de mejor ajuste en el gráfico.

            |> Finalización del Programa:
                
                El programa espera a que el usuario presione una tecla para cerrar la ventana gráfica.
                
                Finalmente, cierra la ventana gráfica y termina el programa.



                                            **Funcionamiento de cada funcion**

    -bubbleSort

        ->Descripción: 
        
          Ordenar un arreglo de números en orden ascendente.

        ->Funcionalidad:
            
            Compara pares de elementos adyacentes.
            
            Intercambia los elementos si están en el orden incorrecto.
            
            Repite el proceso hasta que el arreglo esté completamente ordenado.
            

    -mediana

        ->Descripción: 
        
          Calcular la mediana de un arreglo de números.

        ->Funcionalidad:
            
            Primero, se asegura de que el arreglo esté ordenado.
            
            Si el número de elementos es impar, la mediana es el valor central del arreglo.
            
            Si el número de elementos es par, la mediana es el promedio de los dos valores centrales.
            
            
    -media

        ->Descripción: 
        
           Calcular la media (promedio) de un arreglo de números.

        ->Funcionalidad:
            
            Suma todos los valores del arreglo.
            
            Divide esta suma por el número total de valores.
            
            
    -moda

        ->Descripción: 
        
            alcular la moda (el valor que más se repite) de un arreglo de números.

        ->Funcionalidad:
            
            Cuenta la frecuencia de cada valor en el arreglo.
            
            Identifica el valor que aparece con mayor frecuencia.
            
            Devuelve este valor como la moda.
            
    
    -media_recortada

        ->Descripción: 

            Calcular la media recortada de un arreglo de números, eliminando un 
            porcentaje de los valores más altos y más bajos.  

        ->Funcionalidad:
            
            Ordena el arreglo.
            
            Elimina un porcentaje especificado de los valores más altos y más bajos.
            
            Calcula la media de los valores restantes.
            
    -varianza_for1 y varianza_for2

        ->Descripción: 
        
            Calcular la varianza de un arreglo de números usando dos fórmulas diferentes.

        ->Funcionalidad de Varianza_for1:
            
            Calcula la media del arreglo.
            
            Suma los cuadrados de las diferencias entre cada valor y la media.
            
            Divide esta suma por el número de valores menos uno.
            
        ->Funcionalidad de Varianza_for2:
            
            Calcula la suma de los cuadrados de los valores y la suma de los valores.
            
            Usa estas sumas para calcular la varianza con la fórmula:
            (Suma de los cuadrados - (Suma^2/n))\(n - 1)

    -calcular_tiempo

        ->Descripción: 
        
            Calcular el tiempo de ejecución entre dos puntos en el tiempo.

        ->Funcionalidad:
            
            Usa las estructuras timespec para registrar el tiempo de inicio y fin.
            
            Calcula la diferencia entre estos tiempos en segundos y nanosegundos.
            
            Devuelve el tiempo total en segundos.
            
    -Calc_Z

        ->Descripción: 
        
            Calcular el valor Z correspondiente a un nivel de significancia (alpha).

        ->Funcionalidad:
            
            Usa una fórmula aproximada para calcular el valor Z basado en el nivel de significancia.
            
            La fórmula toma en cuenta el área acumulada bajo la curva normal estándar.
            
    -leer_tabla

        ->Descripción: 
        
            Leer una tabla T desde un archivo y almacenar los valores en una estructura de datos.  

        ->Funcionalidad:
            
            Abre el archivo que contiene la tabla T.
            
            Lee los valores de grados de libertad y los valores T para diferentes niveles de significancia.
            
            Almacena estos valores en una estructura de datos para su posterior uso
            
    -buscar_valor_t

        ->Descripción: 
        
            Buscar el valor T correspondiente a grados de libertad (gdl) y un nivel de significancia (alpha)

        ->Funcionalidad:
            
            Busca en la estructura de datos que contiene la tabla T.
            
            Encuentra la fila correspondiente a los grados de libertad y la columna correspondiente al nivel de significancia.
            
            Devuelve el valor T encontrado.
            
    -encontrar_columna

        ->Descripción: 
        
            Encontrar el índice de columna basado en el valor más cercano.

        ->Funcionalidad:
            
            Calcula la diferencia entre el valor T proporcionado y cada valor en la fila.
            
            Encuentra el índice de la columna con la menor diferencia.
            
    -nivel_significancia

        ->Descripción: 
        
          Devolver la descripción textual del nivel de significancia.

        ->Funcionalidad:

            Devuelve una cadena de texto que representa el nivel de significancia basado en el índice de columna.

    -buscar_por_t

        ->Descripción: 
        
          Buscar los grados de libertad y nivel de significancia que corresponden a un valor T especificado.

        ->Funcionalidad:

            Busca en la estructura de datos que contiene la tabla T.
            
            Encuentra la combinación de grados de libertad y nivel de significancia que más se aproxima al valor T especificado.
            
            Devuelve los grados de libertad y el nivel de significancia encontrados.
            

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++




                                    ***************************************************
                                        Gracias por usar mi programa, hasta luego!
                                    ***************************************************