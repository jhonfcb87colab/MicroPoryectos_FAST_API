**Arracar API**
- uvicorn main04:app --reload

- Estructura de decoradores en FAST API

@app.metodo(
    ruta,
    status_code=codigo_estado,
    tags=['Etiqueta 01','Etiqueta 02'],
    summary="Resumen corto",
    response_model=ModeloRespuesta,
    deprecated=False
)

Parámetros obligatorios:

Sin valor por defecto:
item_id: int
Usando ... :
item_id: int = Path(...)

Parámetros opcionales:

Con valor por defecto:
skip: int = 0
Usando None con Optional:
q: Optional[str] = None
Usando Query o Path con None:
q: Optional[str] = Query(None)
O también:
q: Optional[str] = Query(...)


