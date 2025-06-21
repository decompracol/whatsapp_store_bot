from flask import Flask
from app.whatsapp_webhook import whatsapp_blueprint

app = Flask(__name__)
app.register_blueprint(whatsapp_blueprint)

if __name__ == '__main__':
    app.run(port=8000, debug=True)
