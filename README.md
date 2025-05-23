
### para levantar la aplicacion
python -m uvicorn main:app --reload


### la api se levanta en este puerto
http://localhost:8000/

### desde postman en local
http://127.0.0.1:8000/api/usuarios


### para instalar nuevos paquetes (primero hay que activar )
source venv/bin/activate          # activamos el env por sino esta activi
pip install pandas                # instalamos el paquete que sea
pip freeze > requirements.txt     # para que se añada a los requerimentos