from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load static dataset (simulating BrightData)
with open("data.json") as f:
    dataset = json.load(f)

@app.route("/")
def home():
    return {"message": "Welcome to CrowdWisdomTrading AI Agent 🚀"}

@app.route("/signals")
def get_signals():
    return jsonify(dataset)

@app.route("/signals/<stock>")
def get_signal(stock):
    stock = stock.upper()
    for item in dataset:
        if item["stock"] == stock:
            return jsonify(item)
    return {"error": "Stock not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)
