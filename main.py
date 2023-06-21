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
    result=json.loads(json.dumps(datos))
    return templates.TemplateResponse("inicio.html",{"request":request, "listado":result})

@app.post("/add")
async def add(request: Request):
    formdata=await request.form()
    indexes=datos.keys()
    indexes_as_integers=[int(x) for x in indexes]
    new_index=max(indexes_as_integers)+1
    datos[str(new_index)]=formdata["nuevolenguaje"]
    return RedirectResponse("/",status_code=303)

@app.get("/delete/{id}")
async def delete(request: Request, id:str):
    del datos[str(id)]
    return RedirectResponse("/", status_code=303)