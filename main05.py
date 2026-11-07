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
   



###############   crear endpoints
# End GET point sin parametros
@app.get("/item/")
async def read_item():
    return [{"item_id": "Item 01"}, {"item_id": "Item 02"}, {"item_id": "Item 03"}]

# End GET point con parametros
@app.get("/itemID/{item_id}")
async def read_item(item_id: int):
    return [{"item_id": item_id}, {"item_id": item_id}, {"item_id": item_id}]

# End point POST con parametros
@app.post("/itemID/{item_id}")
async def create_item(name: str):
    return [{"item_id": name, "create": "Item creado con exito"}]

# End point PUT con parametros
@app.put("/itemID/{item_id}")
async def update_item(name: str):
    return [{"item_id": name, "update": "Item actualizado con exito"}]

# End point DELETE con parametros
@app.delete("/itemID/{item_id}")
async def delete_item(name: str):
    return [{"item_id": name, "delete": "Item eliminado con exito"}]
