from flask import Flask, request, jsonify
from transactionSheet import TransactionSheet
from transaction import Transaction

import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "message": "Pymoney - API Rest Python com Flask"})
    
@app.route('/list', methods=['GET'])
def list():
    sheet = TransactionSheet()
    transactions = sheet.getAll()
    return jsonify(transactions)

@app.route('/total', methods=['GET'])
def total():
    sheet = TransactionSheet()
    _total = sheet.getTotal()
    return {
        'total': _total['total'],
        'types': json.loads(_total['types']),
    }

@app.route('/new', methods=['POST'])
def new() -> Transaction:
    sheet = TransactionSheet()
    transaction = Transaction()
    
    transaction.title = request.json['title']
    transaction.value = request.json['value']
    transaction.type = request.json['type']
    transaction.category = request.json['category']
    
    sheet.add(transaction)    
    
    return jsonify(transaction.__dict__), 201

if __name__ == '__main__':
    app.run()