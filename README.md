# Perfectio – FastAPI Backend

## 1. Estructura de carpetas y módulos
```text
Perfectio/
├─ app/
│  ├─ main.py                 # Punto de entrada FastAPI
│  ├─ routes/                 # Routers por dominio (users, habits, goals, etc.)
│  ├─ services/               # Casos de uso y lógica de negocio
│  ├─ schemas/                # Esquemas Pydantic (request/response)
│  ├─ models/                 # Modelos SQLAlchemy
│  ├─ database/               # Conexión, create_tables, sesión
│  ├─ core/                   # Configuración, seguridad, middlewares
│  └─ utils/                  # Utilidades compartidas
├─ tests/                     # Pytest por módulo
├─ requirements.txt
├─ .env.example
└─ README.md
```
Cada router consume servicios específicos, los servicios dependen de repositorios/modelos y los esquemas validan la entrada-salida para mantener responsabilidades separadas.

## 2. Instrucciones para ejecutar el proyecto en local
1. Clonar el repositorio y colocarse en la raíz `Perfectio/`.
2. Configurar variables en `.env` (ver sección 4).
3. Iniciar la API:  
   ```bash
   uvicorn app.main:app --reload
   ```
4. Verificar la salud en `http://localhost:8000/health` y consumir los endpoints desde Swagger o Redoc.

## 3. Entorno virtual, dependencias y requirements.txt
```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```
El archivo `requirements.txt` centraliza FastAPI, SQLAlchemy, Pydantic, Uvicorn, Pytest y demás librerías necesarias para correr y probar el backend.

## 4. Configuración de base de datos y variables de entorno (.env)
1. Duplicar `.env.example` a `.env`.
2. Ajustar variables:
   ```
   DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/perfectio
   SECRET_KEY=tu_clave_segura
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```
3. Crear la base vacía (`createdb perfectio` o equivalente).  
4. El evento `startup` ejecuta `create_tables()` para sincronizar modelos.

## 5. Documentación de la API
- Swagger UI: `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`
Ambas rutas permiten probar todos los endpoints sin herramientas externas.

## 6. Aplicación de principios SOLID
Todo lo descrito a continuación proviene exclusivamente del código presente en este repositorio (p. ej. `app/schemas/diary.py`, `app/schemas/reminder.py`, `app/schemas/goal.py`, `app/core/config.py`, `app/routes`, `app/main.py` y los modelos en `app/models`).
- **S – Single Responsibility**: en `app/schemas/diary.py` cada clase (`DiaryBase`, `DiaryCreate`, `DiaryUpdate`) se limita a validar la estructura del diario sin lógica adicional, y la clase `Settings` en `app/core/config.py` centraliza la configuración global para que los cambios de variables de entorno se gestionen en un único lugar.
- **O – Open/Closed**: `app/main.py` permite extender funcionalidad añadiendo nuevos `include_router` sin modificar los existentes, y los modelos de `app/models` crecen agregando columnas o relaciones aprovechando SQLAlchemy sin alterar la lógica de persistencia ya escrita.
- **L – Liskov Substitution**: los esquemas derivados (`DiaryCreate`, `DiaryResponse`, etc.) heredan de `DiaryBase` en `app/schemas/diary.py`, por lo que se pueden intercambiar donde se espera la clase base manteniendo contratos consistentes.
- **I – Interface Segregation**: `ReminderCreate` y `ReminderUpdate` en `app/schemas/reminder.py`, así como `GoalCreate` y `GoalUpdate` en `app/schemas/goal.py`, separan requisitos obligatorios de campos opcionales, evitando que consumidores implementen atributos innecesarios.
- **D – Dependency Inversion**: los routers bajo `app/routes` dependen de abstracciones como `get_db` (definido en `app/database/__init__.py`) para obtener la sesión sin conocer la implementación concreta, y la configuración se inyecta desde `Settings` en lugar de valores hardcodeados, permitiendo cambiar la fuente (env, Vault, etc.) sin tocar la lógica.
