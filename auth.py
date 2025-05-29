from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

# Configuración JWT
SECRET_KEY = "tu_clave_super_secreta_123"  # ⚠️ Usa una clave segura y guárdala como variable de entorno
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Contexto de cifrado de contraseñas
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# hash = hash_password('1234')
# print("esto es",pwd_context.verify("1234", hash))

# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

# --------------------------
# Funciones de autenticación
# --------------------------

def verificar_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica si la contraseña ingresada coincide con la contraseña hasheada"""
    return pwd_context.verify(plain_password, hashed_password)

def hash_password(password: str) -> str:
    """Devuelve una versión hasheada de la contraseña"""
    return pwd_context.hash(password)

def crear_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """Crea un JWT válido a partir de los datos del usuario"""
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decodificar_token(token: str) -> dict:
    """Decodifica el token JWT y devuelve el contenido"""
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

def obtener_usuario_actual(token: str = Depends(oauth2_scheme)) -> str:
    """Obtiene el nombre de usuario desde el token JWT"""
    credentials_exception = HTTPException(
        status_code=401,
        detail="No se pudo validar el token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = decodificar_token(token)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        return username
    except JWTError:
        raise credentials_exception
