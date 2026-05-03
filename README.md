# readme-analytics (MS5)

Microservicio de analytics. Ejecuta queries en AWS Athena y expone los resultados como endpoints REST.

## Configuracion

```bash
cp .env.example .env
# Rellenar JWT_SECRET, credenciales AWS y ATHENA_OUTPUT_BUCKET
```

## Desarrollo local

```bash
uv run uvicorn app.main:app --reload --port 8005
```

Documentacion disponible en http://localhost:8005/docs

## Docker

```bash
docker build -t readme-analytics .
docker run --env-file .env -p 8005:8005 readme-analytics
```
