from flask import Flask, request, jsonify
from transactionSheet import TransactionSheet
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

if __name__ == '__main__':
    app.run()