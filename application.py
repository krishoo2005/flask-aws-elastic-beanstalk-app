from flask import Flask
import os

application = Flask(__name__)

@application.route('/')
def home():
    return '<h1>Krushna AWS Flask LIVE 🚀</h1>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port)
