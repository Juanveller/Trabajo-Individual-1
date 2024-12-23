## Sistema de Recomendación de Películas

#### Descripción del Proyecto
En el marco de mi Proyecto Individual 1 en Henry, desarrollé e implementé un sistema de recomendación de películas basado en métricas y características específicas,
 empleando la métrica de similitud de coseno. El proceso incluyó una etapa inicial de preprocesamiento y análisis exploratorio de datos. 
 Posteriormente, implementé la API del sistema de recomendación utilizando FastAPI, la cual fue desplegada en Render, permitiendo consultas personalizadas de manera eficiente.
#### Tecnologías Utilizadas
- **Python**: Lenguaje principal para la manipulación de datos y la implementación del modelo.
- **FastAPI**: Framework de desarrollo backend para la creación de APIs.
- **Render**: Plataforma de despliegue para hospedar la API.
- **Pandas y NumPy**: Librerías para la manipulación y análisis de datos.
- **Scikit-Learn**: Para la implementación del modelo de recomendación.
- **Git/GitHub**: Control de versiones y colaboración en el repositorio del proyecto.

#### Conjuntos de Datos
El proyecto utiliza dos conjuntos de datos principales:
link https://drive.google.com/drive/folders/1UHgzUzbY-sI53QU7X71fqABnacbvYTrG?usp=sharing

Los datasets fueron sometidos a un proceso de **Extracción, Transformación y Carga (ETL)** para garantizar su calidad y coherencia. Dando como resultado:

1. **DF_final**: Contiene información de las peliculas, como titulo, generos,director, año de lanzamiento, país de origen, entre otros.
2. **df_caracteristicas**: Matriz de datos utilizada para sistema de recomendaciones.

## Arquitectura del Sistema

1. **ETL y Preprocesamiento**: Limpieza de datos, eliminación de duplicados, manejo de valores nulos y estandarización de formatos.
2. **Análisis Exploratorio de Datos (EDA)**: Generación de insights y análisis de correlaciones entre los atributos.
3. **Creacion de funciones y Modelo de Recomendación**: Desarrollo de funciones de consulta y sistema de recomendacion.
4. **Despliegue del API con FastAPI**: Configuración de endpoints para consultas y recomendaciones.
5. **Despliegue en Render**: Publicación de la API para permitir su consumo externo.

## Endpoints de la API
La API permite acceder a recomendaciones personalizadas y datos específicos de las películas mediante los siguientes endpoints:

1. **@app.get("/cantidad_peliculas_mes/")**
2. **@app.get("/cantidad_peliculas_dia/")**
3. **@app.get("/score_titulo/")**
4. **@app.get("/votos_titulo/")**
5. **@app.get("/get_actor/")**
6. **@app.get("/get_director/")**
7. **@app.get("/get_recomendaciones/")**

## Instalación y Uso
Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Clona el repositorio**:
    git clone https://github.com/juanveller/Proyecto-Individual-1.git
    cd Proyecto-Individual-1

2. **Crea y activa un entorno virtual**:
    python -m venv venv
    #en mac source `venv/bin/activate`  # En Windows `venv\Scripts\activate`

3. **Instala las dependencias**:
    pip install -r requirements.txt

4. **Ejecuta la API con FastAPI**:
    uvicorn main:app --reload

5. **Accede a la API**:
Una vez en ejecución, puedes acceder a los endpoints en `http://localhost:8000`.

## Video
Pruebas de funcionamiento de la APi https://drive.google.com/drive/folders/1TJk2lV3AhYqJp_kANi8vR8uN1NoBdJNl?usp=sharing

## link de pruebas
https://trabajo-individual-1-4dtp.onrender.com/docs

## Autores
Juan José Veller - Contacto: https://www.linkedin.com/in/juan-veller/