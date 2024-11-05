## Sistema de Recomendación de Películas

#### Descripción del Proyecto
En marco de mi Proyecto Individual 1 en Henry, diseñé e implementé un sistema de recomendación de películas basado en metricas y caracteristicas, utilizando la métrica de similitud de coseno. El proceso implicó una etapa inicial de preprocesamiento y análisis exploratorio de dos datasets sobre películas. Posteriormente, se entrenó un modelo de machine learning capaz de identificar características relevantes y calcular la similitud entre películas. Finalmente, se desarrolló una API para exponer las funcionalidades del sistema.

El sistema de recomendación está construido con **FastAPI** y desplegado en **Render**, permitiendo consultas eficientes y personalizadas. Los datos han sido limpiados, preprocesados y optimizados para mejorar la precisión de las recomendaciones.

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
Pruebas de funcionamiento de la APi

## Autores
Juan José Veller - Contacto: https://www.linkedin.com/in/juan-veller/