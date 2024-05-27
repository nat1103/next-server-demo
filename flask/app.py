from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Web App with Python Flask!'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))  # Utilisez 8080 comme valeur par défaut si la variable d'environnement PORT n'est pas définie
    app.run(host='0.0.0.0', port=port)