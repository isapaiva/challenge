from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # O Flask busca automaticamente os arquivos dentro da pasta /templates
    return render_template('prot_integrado_synapse_health.html')

if __name__ == '__main__':
    # Roda o servidor localmente no modo de desenvolvimento/debug
    app.run(debug=True, port=5000)