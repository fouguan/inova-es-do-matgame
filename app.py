from flask import Flask, render_template
import json

app = Flask(__name__)

# Função para ler o conteúdo de um arquivo Python (por exemplo, JSON)
def ler_arquivo():
    try:
        # Vamos supor que estamos lendo dados de um arquivo JSON
        with open("dados.json", "r") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {"error": "Arquivo não encontrado!"}
    except json.JSONDecodeError:
        return {"error": "Erro ao decodificar o arquivo!"}

@app.route('/')
def index():
    # Chama a função que lê o arquivo e extrai os dados
    dados = ler_arquivo()
    return render_template('index.html', dados=dados)

if __name__ == "__main__":
    app.run(debug=True)
