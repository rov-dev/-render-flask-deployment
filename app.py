from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/tokenize", methods=["POST"])
def tokenize():
    data = request.get_json()
    text = data.get("text", "")
    tokens = simple_tokenize(text)
    return jsonify({"tokens": tokens})

def simple_tokenize(text):
    import re
    return re.findall(r'\b\w+\b', text.lower())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
