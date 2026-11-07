# B) Query Parameters

from fastapi import FastAPI

app = FastAPI(
    title="Ejemplo de Query Parameters",
    description="Ejemplo de cómo usar Query Parameters en FastAPI",
    version="1.0.0"
)


@app.get('/')
async def root():
    return {"message": "Hola FASTAPI!"}
   

@app.get("/buscar/")
def buscar(nombre: str):
    return {"nombre": nombre}

#     http://127.0.0.1:8000/buscar/?nombre=jhon