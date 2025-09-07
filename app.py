from flask import Flask, request, jsonify
from flask_cors import CORS
from retriver import retrieval_chain  # Ensure this import works

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/get_answer', methods=['POST'])
def get_answer():
    data = request.get_json()
    user_input = data.get("input", "")

    if not user_input:
        return jsonify({"answer": "Please provide a valid input."})

    response = retrieval_chain.invoke({"input": user_input})
    return jsonify({"answer": response.get("answer", "No answer found.")})

if __name__ == '__main__':
    app.run(debug=True)
