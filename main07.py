# B) Query Parameters
from fastapi import FastAPI
from fastapi import Path, Query
from typing import Optional

app = FastAPI(
    title="Ejemplo de Query Parameters",
    description="Ejemplo de cómo usar Query Parameters en FastAPI",
    version="1.0.0"
)



@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(
        ...,   ## Parametro obligatorio (no se puede omitir)
        title="ID del ítem",
        ge=1,           # mayor o igual a 1
        description="El ID único del ítem (debe ser un entero positivo)"
    ),
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        description="Término de búsqueda opcional"
    ),
    size: Optional[float] = Query(
        None,
        gt=0,           # mayor que 0
        le=1000,        # menor o igual a 1000 (corrigiendo el lt=1000 que parecía error)
        description="Tamaño opcional (valor entre 0 y 1000)"
    )
):
    results = {"item_id": item_id}
    
    if q:
        results["q"] = q
        
    if size is not None:
        results["size"] = size
        
    return results


#    http://127.0.0.1:8000/items/1
#    http://127.0.0.1:8000/items/0        # Error: item_id debe ser mayor o igual a 1

#    http://127.0.0.1:8000/items/1?q=abc
#    http://127.0.0.1:8000/items/1?q=a       # Error: q debe tener al menos 3 caracteres

#    http://127.0.0.1:8000/items/1?q=abc&size=10
#    http://127.0.0.1:8000/items/1?q=abc&size=1001   # Error: size debe ser menor o igual a 1000

