# PRIMER PROYECTO INDIVIDUAL / MACHINE LEARNING OPERATIONS

Este proyecto tiene como objetivo desarrollar un modelo de machine learning para un sistema de recomendación de películas, además de la implementación de 6 funciones para obtener información específica de la base de datos a través de una FastApi. 

### EDA & ETL
En la primera parte se realizó todo el trabajo de ETL (Extract, Transformation and Load) y EDA (Exploratory Data Analysis) de los dos datasets disponibles. Esta parte consistió en la limpieza de los datos mientras se exploraba la información, algunas de las acciones que se ejecutaron fueron las siguientes; 

1-	Eliminación de columnas que no serían utilizadas por las funciones ni el modelo de ML.
2-	Observación de valores nulos o duplicados, y su eliminación o reemplazo (dependiendo la columna)
3-	Funciones para desempaquetar columnas anidadas y solo trabajar con datos específicos de las filas
4-	Cambios de tipos de datos, entre ellos una función para cambiar un tipo de dato float que representaba minutos a formato de horas y minutos.
5-	Creación de un solo dataset a partir de la unión de los dos datasets limpios.

### DESARROLLO DE LAS FUNCIONES

Lo segundo que se realizó fue el desarrollo de las 6 funciones que serían ejecutadas a través de la FastApi. Para ello, antes se hizo una exploración de datos para ver si las respuestas de las funciones coincidían con la información antes analizada, como por ejemplo;  conocer cuáles eran los idiomas con más frecuencia, los países con más películas y cuáles eran las productoras mas populares. Las funciones que desarrollaron fueron las siguientes;

1-	Función que recibe como parámetro un idioma y devuelve la cantidad de películas que realizaron en el idioma
2-	Función que recibe como parámetro una película y devuelve su duración y año de lanzamiento
3-	Función que recibe como parámetro el nombre de una franquicia y devuelve la cantidad de películas que ha producido junto con su ganancia total y el promedio de ganancia por película.
4-	Función que recibe como parámetro el nombre de un país y devuelve la cantidad de películas producidas por en el país
5-	Función que recibe como parámetro una productora y devuelve la cantidad de películas que se produjeron y la ganancia total
6-	Función que recibe como parámetro el nombre de un Director y devuelve su ganancia total, además de una lista de todas las películas que ha dirigido con año de lanzamiento, ganancia y costo de cada película.

### MODELO DE MACHINE LEARNING

Luego, se implementó un modelo de Machine Learning para desarrollar la función de recomendación, la cual recibe como parámetro el nombre de una película y devuelve la sugerencia de 5 películas similares. En este caso se estableció un modelo basado en contenido, esto es, en la similitud de sus reseñas. 

Para lo anterior, se utilizó el modelo BERT (Bidirectional Encoder Representations from Transformers) el cual es una técnica basada en redes neuronales que convierte cadenas de textos en vectores con el fin de preparar los datos para operaciones de algoritmos. En este caso se aplicó la técnica de similitud del coseno (similitud de coseno del ángulo entre vectores) para obtener que película (vector) guarda relación con otra. 

En el caso de este proyecto, una de las razones por las que se utilizó el modelo BERT fue que su capacidad de procesamiento fue más rápida y no consumió tantos recursos de almacenamiento en comparación a otros modelos como Count-Vectorizer o TF-IDF. 

Finalmente se implementó una FastAPI para hacer disponibles los datos a través de las funciones desarrolladas.
