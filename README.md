# Bot de WhatsApp para tienda virtual con OpenAI

Este bot responde automáticamente a preguntas de clientes sobre productos, usando WhatsApp y la API de OpenAI. El conocimiento del bot se entrena con un archivo PDF del catálogo de productos.

## Requisitos

- Cuenta en OpenAI con clave API
- Cuenta de WhatsApp Business (Meta) con número y token
- Archivo PDF con el catálogo de productos en `/data`

## Cómo ejecutar

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt

flask run --port=5000
```

Exponer con ngrok o localtunnel para pruebas:
```bash
ngrok http 5000
```

## Estructura

- `main.py`: arranca el servidor Flask
- `app/`: lógica principal del bot
- `.env`: credenciales (no compartir)
- `data/`: archivos PDF del catálogo

## Webhook WhatsApp

Registra tu webhook en Meta usando la URL pública de `ngrok` y configúralo con el método POST.
