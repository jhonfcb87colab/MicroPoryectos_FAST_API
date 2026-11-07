# B) Recibir Query Parameters en el curpo de la petición
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Ejemplo de Query Parameters",
    description="Ejemplo de cómo usar Query Parameters en FastAPI",
    version="1.0.0"
)

# Para operaciones como POST y PUT, normalmente necesitamos recibir datos en el cuerpo de la petición, típicamente en formato JSON.

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

class User(BaseModel):
    username: str
    full_name: str = None



app = FastAPI()

@app.post("/items/")
async def create_item(item: Item):
    return item

# http://127.0.0.1:8000/items

# en el cuerpo de la petición, enviar un JSON con los datos del item, por ejemplo:
# {
#   "name": "Monitor",
#   "description": "Pantalla de 24 pulgadas",
#   "price": 299.99,
#   "tax": 21.0
# }


@app.post("/items/{item_id}")
async def create_user(item_id: int, item: Item, user: User):
    return {"item_id": item_id, "item": item, "user": user}

# http://127.0.0.1:8000/items/300

# en el cuerpo de la petición, enviar un JSON con los datos del item, por ejemplo:
# {
#   "item": {
#     "name": "Teclado",
#     "description": "Mecánico retroiluminado",
#     "price": 89.99,
#     "tax": 18.0
#   },
#   "user": {
#     "username": "carlos23",
#     "full_name": "Carlos Ramírez"
#   }
# }