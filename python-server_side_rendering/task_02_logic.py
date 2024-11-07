from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/items')
def items():

    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items_list = data.get("items", [])
    except FileNotFoundError:
        print("Erreur : Le fichier items.json est introuvable.")
        items_list = []
    except json.JSONDecodeError:
        print("Erreur : Impossible de décoder le fichier JSON.")
        items_list = []

    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
