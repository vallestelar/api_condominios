from fastapi import FastAPI
from routers import usuarios  # lo crearemos después

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}

# Montar rutas
app.include_router(usuarios.router)
