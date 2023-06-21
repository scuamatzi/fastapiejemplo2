from fastapi import FastAPI, Request
import json
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

app=FastAPI()
templates=Jinja2Templates(directory="templates")

datos={
    "1":"Python",
    "2":"PHP",
    "3":"CSS",
    "4":"NGINX",
    "5":"DOCKER",
    "6":"AWS"
}

@app.get("/")
async def inicio(request: Request):
    #sin_codificar=json.dumps(datos)
    #return json.loads(sin_codificar)
    #print(len(datos))
    #return json.loads(json.dumps(datos))
    result=json.loads(json.dumps(datos))
    return templates.TemplateResponse("inicio.html",{"request":request, "listado":result})

@app.post("/add")
async def add(request: Request):
    #nuevos_datos={}
    formdata=await request.form()
    #i=1

    #for id in datos:
    #    nuevos_datos[str(id)]=datos[id]
    #    i+=1
    
    #datos[i]=formdata["nuevolenguaje"]
    #print(datos["1"])
    #print(len(datos))
    indexes=datos.keys()
    indexes_as_integers=[int(x) for x in indexes]
    new_index=max(indexes_as_integers)+1
    print(new_index)
    #datos[str(len(datos)+1)]=formdata["nuevolenguaje"]
    datos[str(new_index)]=formdata["nuevolenguaje"]
    return RedirectResponse("/",status_code=303)

@app.get("/delete/{id}")
async def delete(request: Request, id:str):
    del datos[str(id)]
    return RedirectResponse("/", status_code=303)