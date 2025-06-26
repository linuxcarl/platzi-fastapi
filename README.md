# FastAPI Project

## Instalación

1. Instalar FastAPI con todas las dependencias:
```bash
python3 -m pip install fastapi[all]
```

## Ejecutar la API

### Modo desarrollo
```bash
python3 -m fastapi dev main.py
```

### Modo producción
```bash
python3 -m fastapi run main.py
```

## URLs disponibles

- **API**: http://127.0.0.1:8000
- **Documentación interactiva**: http://127.0.0.1:8000/docs
- **Documentación alternativa**: http://127.0.0.1:8000/redoc

## Endpoints

- `GET /` - Mensaje de bienvenida
- `GET /time/{iso_code}` - Obtener hora actual por código de país (US, CA, GB, FR, DE, JP, BR, MX, CO, AR)