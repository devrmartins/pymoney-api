from flask import Flask, request, jsonify
from transactionSheet import TransactionSheet

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


if __name__ == '__main__':
    app.run()