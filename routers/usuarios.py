from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from auth import obtener_usuario_actual


router = APIRouter(
    prefix="/api/usuarios",
    tags=["usuarios"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#añado un comentario para comprobar el despliegue continuo
# @router.get("/")
# def listar_usuarios(db: Session = Depends(get_db)):
#     return db.query(Usuario).all()

@router.get("/")
def listar_usuarios(
    db: Session = Depends(get_db),
    usuario_actual: str = Depends(obtener_usuario_actual)  # 🔒 protege la ruta
):
    return db.query(Usuario).all()

