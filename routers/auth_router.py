from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from auth import verificar_password, crear_token

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.username == form_data.username).first()
    if not usuario or not verificar_password(form_data.password, usuario.password.strip()):
        print(verificar_password(form_data.password, usuario.password))
        raise HTTPException(status_code=400, detail="Usuario o contraseña incorrectos")

    token = crear_token({"sub": usuario.username})
    return {"access_token": token, "token_type": "bearer"}

