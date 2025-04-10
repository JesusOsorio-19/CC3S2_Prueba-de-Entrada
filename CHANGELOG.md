# Registro de actividades por día

## Día 1: Configuración inicial

- Creamos la carpeta del proyecto `Prueba-entrada-CC3S2/trivia-game-python` y la estructura base.

- Configuramos el entorno virtual con:
    - `python -m venv venv`
    - `source venv/Scripts/activate`

- Instalamos las dependencias principales, con `pip install fastapi uvicorn asyncpg databases python-dotenv`:
  - `fastapi`, `uvicorn`, `asyncpg`, `databases`, `python-dotenv`

- Generamos el archivo `requirements.txt` con las dependencias del entorno, usando el comando `pip freeze > requirements.txt`.

- Configuramos correctamente los archivos:
  - `.env` con las variables sensibles (`DATABASE_URL`, `SECRET_KEY`)
  - `Dockerfile` para construir la imagen de FastAPI
  - `docker-compose.yml` para levantar FastAPI y PostgreSQL

- Creamos la carpeta `app/` con el archivo `main.py` con un endpoint `/` que devuelve un mensaje de prueba.


- Inicializamos el repositorio Git:
  - Creamos la rama `develop` para desarrollo
  - Creamos la rama `feature/dia1` para trabajo diario

- Se documentó el contenido del `CHANGELOG.md` en la rama `feature/dia1`

- Se realizó el merge de `feature/dia1` → `develop` → `main`

- Se etiquetó el avance con el tag: `v1.0-day1`
