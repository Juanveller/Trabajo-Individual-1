# main.py
from fastapi import FastAPI, HTTPException
from typing import Optional
import pandas as pd
import calendar
import ast

# Inicializar FastAPI
app = FastAPI()

# Cargar datos
DF_final = pd.read_csv("DF_procesado.csv", parse_dates=['release_date'], low_memory=False)

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

if __name__ == "__main__":  
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0",port=8000) 