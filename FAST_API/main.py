from fastapi import FastAPI
import pandas as pd



app = FastAPI()
new_data = pd.read_csv("./new_data.csv")

@app.get('/peliculas_idioma/{idioma}')
def peliculas_idioma(idioma):
    cantidad = (new_data["original_language"] == idioma).sum()
    return  f"{cantidad} cantidad de películas fueron estrenadas en {idioma}"

@app.get('/peliculas_pais/{pais}')
def peliculas_pais(Pais):
    cantidad = (new_data['countries'].str.lower() == Pais.lower()).sum()
    return f'Se producen {cantidad} películas en el país {Pais.title()}'

@app.get('/peliculas_duracion/{pelicula}')
def peliculas_duracion( pelicula):
    consulta = new_data.loc[new_data['title'].str.title() == pelicula.title()]
    duracion = consulta["runtime"].values[0]
    año = consulta["año"].values[0]
    return f"{pelicula.title()}. Duracion: {duracion}. Año: {año}"

@app.get('/productoras_exitosas/{productora}')
def productoras_exitosas(productora):
    cantidad = (new_data["production_companies"]== productora).sum()
    mascara = (new_data["production_companies"] == productora)
    ingreso = new_data[mascara]["revenue"].sum()
    return  f"La productora {productora} ha realizado {cantidad} peliculas y ha tenido un ingreso de {ingreso} "

@app.get('/franquicia/{franquicia}')
def franquicia(franquicia ):
    cantidad = (new_data["collection"]== franquicia).sum()
    mascara = (new_data["collection"] == franquicia)
    ganancia = (new_data[mascara]["revenue"]).sum()
    promedio = (new_data[mascara]["revenue"]).mean()
    return f"La franquicia {franquicia} posee {cantidad} peliculas, una ganancia total de {ganancia} y una ganancia promedio de {promedio}"

@app.get('/get_director/{nombre_director}')
def get_director(nombre):
    mascara = new_data["director"] == nombre.title()
    retorno = new_data[mascara]["return"].sum()
    lista = []
    for i in range(len(new_data[mascara]["title"])):
        lista.append(f"{new_data[mascara]['title'].iloc[i]} Año:{new_data[mascara]['año'].iloc[i]}, retorno_pelicula:{new_data[mascara]['return'].iloc[i]}, budget_pelicula:{new_data[mascara]['budget'].iloc[i]}, revenue_pelicula: {new_data[mascara]['revenue'].iloc[i]} ")
    return f"Director:{nombre.title()}, Retorno: {retorno}, Peliculas: {lista}"

@app.get('/recomendacion/{titulo}')
def recomendacion(pelicula):
    mascara = new_data["title"].str.lower() == pelicula.lower()
    resultado = new_data[mascara]["recomendaciones"].values[0]
    return resultado
