from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener la URL desde la variable de entorno
DATABASE_URL = os.getenv("DATABASE_URL")

# Verificación (opcional, solo para debug):
if DATABASE_URL is None:
    raise Exception("DATABASE_URL no definida. Verifica tu archivo .env")

# Crear motor de conexión
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

