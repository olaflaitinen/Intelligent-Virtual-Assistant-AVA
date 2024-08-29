from flask import Flask, request, jsonify
from src.dialogue.response_generation import generate_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = generate_response(user_input)
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
