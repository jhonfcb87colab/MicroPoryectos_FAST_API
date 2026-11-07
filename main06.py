# B) Query Parameters

from fastapi import FastAPI
from typing import Optional
app = FastAPI(
    title="Ejemplo de Query Parameters",
    description="Ejemplo de cómo usar Query Parameters en FastAPI",
    version="1.0.0"
)


@app.get('/')
async def root():
    return {"message": "Hola FASTAPI!"}
   



###############   crear endpoints
@app.get("/items/")
async def read_items(skip: int = 1, limit: int = 10, q: Optional[str] = None):
    results = {"skip": skip, "limit": limit}
    if q:
        results.update({"q": q})
    return results



#    http://127.0.0.1:8000/items/?skip=2&limit=5&q=fastapi

