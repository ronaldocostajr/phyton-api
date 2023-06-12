from flask import Flask, jsonify

app = Flask(__name__)

purchase_orders = [
    {
        'id': 1,
        'description': 'Pedido de compra',
        'itens': [
            {
                'id': 1,
                'description': 'Item do pedido 1',
                'price': 20.00
            }
        ]

    }
]



@app.route('/')
def home():
    return 'ronaldo costa {}'.format('teste api')

@app.route('/purchase_orders')
def get_purchase_orders():
    return jsonify(purchase_orders)

app.run(port=5000)