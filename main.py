# main.py
from fastapi import FastAPI, HTTPException
from typing import Optional
import pandas as pd
import calendar
import ast
from sklearn.metrics.pairwise import cosine_similarity

# Inicializar FastAPI
app = FastAPI()

# Ruta raíz para verificar que la API esté activa
@app.get("/")
def root():
    return {"message": "API is running"}

# Cargar datos
DF_final = pd.read_csv("DF_final.csv", parse_dates=['release_date'], low_memory=False)

# Función auxiliar para convertir nombres de meses a número  
def mes_en_numero(mes):  
    meses_es = {  
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4, "mayo": 5,  
        "junio": 6, "julio": 7, "agosto": 8, "septiembre": 9,  
        "octubre": 10, "noviembre": 11, "diciembre": 12  
    }  
    return meses_es.get(mes.lower(), None)  # Uso de .get para manejar valores no válidos  

# Función auxiliar para convertir nombres de días a número  
def dia_en_numero(dia):  
    dias_es = {  
        "lunes": 0, "martes": 1, "miércoles": 2, "jueves": 3,  
        "viernes": 4, "sábado": 5, "domingo": 6  
    }  
    return dias_es.get(dia.lower(), None)  # Uso de .get para manejar valores no válidos

# Función 1: Cantidad de peliculas por mes
@app.get("/cantidad_peliculas_mes/")
def cantidad_filmaciones_mes(mes: str):
    mes_numero = mes_en_numero(mes)
    if mes_numero is None:
        raise HTTPException(status_code=400, detail="Mes no válido")
    
    count = DF_final[DF_final['release_date'].dt.month == mes_numero].shape[0]
    count = DF_final[DF_final['release_date'].dt.month == mes_numero].shape[0]

    return {"mes": mes, "peliculas estrenadas": count}

# Función 2: Cantidad de peliculas por día
@app.get("/cantidad_peliculas_dia/")
def cantidad_peliculas_dia(dia: str):
    dia_numero = dia_en_numero(dia)
    if dia_numero is None:
        raise HTTPException(status_code=400, detail="Día no válido")
    
    count = DF_final[DF_final['release_date'].dt.dayofweek == dia_numero].shape[0]
    return {"dia": dia, "Peliculas estrenadas": count}

# Función 3: Score de una pelicula
@app.get("/score_titulo/")
def score_titulo(titulo_de_la_Pelicula: str):
    pelicula = DF_final[DF_final['title'].str.lower() == titulo_de_la_Pelicula.lower()]
    
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    pelicula = pelicula.iloc[0]
    return {
        "Titulo": pelicula['title'],
        "Año": int(pelicula['release_year']),
        "Score": pelicula['vote_average']
    }

# Función 4: Votos de una pelicula
@app.get("/votos_titulo/")
def votos_titulo(titulo_de_la_pelicula: str):
    pelicula = DF_final[DF_final['title'].str.lower() == titulo_de_la_pelicula.lower()]
    
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Película no encontrada")
    
    pelicula = pelicula.iloc[0]
    return {
        "Titulo": pelicula['title'],
        "Cantidad_votos": int(pelicula['vote_count']),
        "Promedio_votos": pelicula['vote_average']
    }

# Función 5: Información de un actor
@app.get("/get_actor/")
def get_actor(nombre_actor: str):
    actor_films = DF_final[DF_final['cast_info'].apply(lambda cast: any(d['name'].lower() == nombre_actor.lower() for d in ast.literal_eval(cast)) if isinstance(cast, str) else False)]
    
    if actor_films.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado")

    retorno_total = actor_films['return'].sum()
    cantidad_peliculas = actor_films.shape[0]
    promedio_retorno = retorno_total / cantidad_peliculas if cantidad_peliculas > 0 else 0
    
    return {
        "Actor": nombre_actor,
        "Cantidad_peliculas": cantidad_peliculas,
        "Retorno_total": retorno_total,
        "Retorno_Promedio": promedio_retorno
    }

# Función 6: Información de un director
@app.get("/get_director/")
def get_director(nombre_director: str):
    # Filtra las filas donde el director está en el director_info
    director_info = DF_final[DF_final['director_info'].apply(
        lambda director_info: any(d.lower() == nombre_director.lower() for d in ast.literal_eval(director_info))
        if isinstance(director_info, str) else False)]
    
    if director_info.empty:
        raise HTTPException(status_code=404, detail="Director no encontrado")
    
    peliculas = []
    for _, film in director_info.iterrows():
        pelicula_info = {
            "Titulo": film['title'],
            "Fecha_lanzamiento": film['release_date'],
            "Retorno": film['return'],
            "Costo": film['budget'],
            "Ganancia": film['revenue'] - film['budget']
        }
        peliculas.append(pelicula_info)
    
    retorno_total = director_info['return'].sum()
    
    return {
        "director": nombre_director,
        "retorno_total": retorno_total,
        "peliculas": peliculas
    }

# sistema de remomendacion

# Cargar el df_características
df_caracteristicas = pd.read_csv("df_caracteristicas.csv")

# chequear que el título esté en df_caracteristicas
df_caracteristicas['title'] = DF_final['title'].values

# Función para obtener recomendaciones basadas en similitud de coseno
def get_recomendaciones(titulo: str, peliculas_recomendadas: int = 5):
    # Verificar si el título está en el dataset original
    if titulo.lower() not in DF_final['title'].str.lower().values:
        raise HTTPException(status_code=404, detail="Película no encontrada")

    # Obtener el índice de la película de entrada desde DF_final
    idx = DF_final[DF_final['title'].str.lower() == titulo.lower()].index[0]

    # Calcular la similitud de coseno
    matriz_caracteristicas = df_caracteristicas.drop(columns=['title']).values  # Excluir el título para la similitud
    similitud_de_coseno = cosine_similarity([matriz_caracteristicas[idx]], matriz_caracteristicas)[0]

    # Ordenar las películas por similitud de coseno y excluir la película de entrada
    similar_indices = similitud_de_coseno.argsort()[::-1][1:peliculas_recomendadas+1]

    # Obtener títulos y detalles de las películas similares
    peliculas_recomendadas = DF_final.iloc[similar_indices][['title','genres','vote_average','release_year']].to_dict(orient="records")

    return peliculas_recomendadas

# Configuración de FastAPI
@app.get("/get_recomendaciones/")
def obtener_recomendaciones(titulo: str, peliculas_recomendadas: Optional[int] = 5):
    try:
        recomendaciones = get_recomendaciones(titulo, peliculas_recomendadas)
        return {"Titulo": titulo, "Recomendaciones": recomendaciones}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ocurrió un error al generar las recomendaciones")




if __name__ == "__main__":  
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0",port=8000)