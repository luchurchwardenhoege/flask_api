from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def say_hello():
    data = request.get_json()
    name = data['name']
    return jsonify({'message': f'Hello, {name}'})

if __name__ == '__main__':
    app.run(debug=True)
