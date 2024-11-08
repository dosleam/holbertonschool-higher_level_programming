from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Fonction pour lire les données depuis un fichier JSON
def read_json():
    with open('products.json', 'r') as file:
        data = json.load(file)
    return data['items']

# Fonction pour lire les données depuis un fichier CSV
def read_csv():
    products = []
    with open('products.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            products.append(row)
    return products

# Fonction pour lire les données depuis SQLite
def read_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    products = [{"id": row[0], "name": row[1], "category": row[2], "price": row[3]} for row in cursor.fetchall()]
    conn.close()
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Lecture des données selon la source
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        return render_template('product_display.html', error="Source invalide. Veuillez utiliser 'json', 'csv' ou 'sql'.")

    # Filtrage par ID si spécifié
    if product_id:
        data = [product for product in data if str(product['id']) == product_id]
        if not data:
            return render_template('product_display.html', error="Produit non trouvé.")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
