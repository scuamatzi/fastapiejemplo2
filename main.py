from fastapi import FastAPI, Request
import json

app=FastAPI()

datos={
    "1":"Python",
    "2":"PHP",
    "3":"CSS",
    "4":"NGINX",
    "5":"DOCKER",
    "6":"AWS"
}

@app.get("/")
async def inicio():
    #sin_codificar=json.dumps(datos)
    #return json.loads(sin_codificar)
    return json.loads(json.dumps(datos))

@app.post("/add")
async def add(request: Request):
    nuevos_datos={}
    formdata=await request.form()
    i=1

    for id in datos:
        nuevos_datos[str(id)]=datos[id]
        i+=1
    
    datos[i]=formdata["nuevolenguaje"]