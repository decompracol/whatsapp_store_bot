from flask import Blueprint, request, jsonify
from .openai_agent import generate_answer
from .pdf_loader import extract_text_from_pdf
from .whatsapp_utils import enviar_mensaje

whatsapp_blueprint = Blueprint("whatsapp", __name__)
contexto = extract_text_from_pdf("data/productos_catalogo.pdf")

@whatsapp_blueprint.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    data = request.get_json()
    try:
        mensaje = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        numero = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

        respuesta = generate_answer(mensaje, contexto)
        enviar_mensaje(numero, respuesta)

        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
