from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
products = [
    {'id': 1, 'name': 'Apples', 'price': 1.00},
    {'id': 2, 'name': 'Bananas', 'price': 0.50}
]

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
