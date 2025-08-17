from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({"message": "Hello, OSSE Assignment by Shital Kumbhar (2023lm70195)"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
