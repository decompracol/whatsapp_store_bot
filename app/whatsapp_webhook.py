from flask import Blueprint, request, jsonify
from .openai_agent import generate_answer
from .pdf_loader import extract_text_from_pdf
from .whatsapp_utils import enviar_mensaje

whatsapp_blueprint = Blueprint("whatsapp", __name__)
contexto = extract_text_from_pdf("data/productos_catalogo.pdf")

@whatsapp_blueprint.route("/webhook", methods=["GET", "POST"])
def whatsapp_webhook():
    if request.method == "GET":
        verify_token = "mitoken123"  # Usa el mismo token que pones en Meta
        mode = request.args.get("hub.mode")
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")

        if mode == "subscribe" and token == verify_token:
            print("WEBHOOK_VERIFICADO")
            return challenge, 200
        else:
            return "Error de verificación", 403

    # POST: manejo de mensajes
    data = request.get_json()
    print(data)
    try:
        mensaje_obj = data["entry"][0]["changes"][0]["value"]
    
        if "messages" not in mensaje_obj:
            return jsonify({"status": "no hay mensaje"}), 200

        mensaje = mensaje_obj["messages"][0]["text"]["body"]
        numero = mensaje_obj["messages"][0]["from"]

        respuesta = generate_answer(mensaje, contexto)
        print(respuesta)
        enviar_mensaje(numero, respuesta)
        print(numero)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
