# A) Path Parameters

# Tipos de Parámetros

from fastapi import FastAPI

app = FastAPI()

@app.get("/usuarios/{id}")
def obtener_usuario(id: int):
    return {"usuario_id": id}




#     http://127.0.0.1:8000/usuarios/5