from fastapi import FastAPI
from routers import usuarios, auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://condofront.onrender.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"mensaje": "API funcionando correctamente"}

# Montar rutas
app.include_router(usuarios.router)
app.include_router(auth_router.router)

