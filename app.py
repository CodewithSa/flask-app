from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'})

@app.route('/multiply')
def multiply():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({'result': a * b})

if __name__ == '__main__':
    app.run(debug=True)