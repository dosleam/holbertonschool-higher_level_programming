from flask import Flask, render_template, request, jsonify
import sqlite3
import json
import csv

app = Flask(__name__)

# Fonction pour lire les données JSON
def load_data_from_json():
    with open('items.json', 'r') as file:
        data = json.load(file)
    return data.get('items', [])

# Fonction pour lire les données CSV
def load_data_from_csv():
    items = []
    with open('items.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
    return items

# Fonction pour lire les données depuis SQLite
def load_data_from_sql():
    items = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name, category, price FROM Products")
        rows = cursor.fetchall()
        for row in rows:
            items.append({
                'name': row[0],
                'category': row[1],
                'price': row[2]
            })
    except sqlite3.Error as e:
        print("Erreur de base de données:", e)
    finally:
        conn.close()
    return items

# Route pour afficher les produits en fonction de la source des données
@app.route('/products')
def products():
    source = request.args.get('source', 'json')

    # Charger les données en fonction de la source spécifiée
    if source == 'json':
        items = load_data_from_json()
    elif source == 'csv':
        items = load_data_from_csv()
    elif source == 'sql':
        items = load_data_from_sql()
    else:
        return "Source incorrecte", 400

    return render_template('product_display.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
