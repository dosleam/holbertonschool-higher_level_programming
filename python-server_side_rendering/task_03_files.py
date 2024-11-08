import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            item_data = data.get("items")
    except FileNotFoundError:
        data = []

    return render_template('items.html', items=item_data)


@app.route('/products', methods=['GET'])
def display_products():

    source = request.args.get('source', '')

    product_id = request.args.get('id', None)
    message = None
    products = []

    if source not in ['json', 'csv']:
        message = "Wrong source"

    try:
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)

        elif source == 'csv':
            with open('products.csv', 'r') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]

        if product_id:
            products = [
                product for product in products if str(
                    product['id']) == product_id]
            if not products:
                message = "Product not found."

    except FileNotFoundError:
        message = "File not found."

    except Exception as e:
        message = f"An error occurred: {e}"

    return render_template('product_display.html', products=products, message=message)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
