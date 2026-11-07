# B) Query Parameters

from fastapi import FastAPI

app = FastAPI()


@app.get("/buscar/")
def buscar(nombre: str):
    return {"nombre": nombre}

#     http://127.0.0.1:8000/buscar/?nombre=jhon