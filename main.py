from flask import Flask
import os
from app.whatsapp_webhook import whatsapp_blueprint

app = Flask(__name__)
app.register_blueprint(whatsapp_blueprint)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)