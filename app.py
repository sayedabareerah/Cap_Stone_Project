from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    # Simulate detection logic
    return jsonify({"output": "Detection completed"})

@app.route('/store', methods=['POST'])
def store():
    data = request.json
    action = data.get('action')
    if action == 'object':
        return jsonify({"output": "Object stored"})
    elif action == 'face':
        return jsonify({"output": "Face stored"})

if __name__ == '__main__':
    app.run()
