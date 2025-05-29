from fastapi import FastAPI
from routers import usuarios  # lo crearemos después
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}

# Montar rutas
app.include_router(usuarios.router)
