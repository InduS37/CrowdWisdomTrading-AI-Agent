from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Welcome to CrowdWisdomTrading AI Agent 🚀"}

# Simple prediction endpoint (demo only)
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json or {}
    stock = data.get("stock", "Unknown")

    # Very simple mock logic: if length of stock name is even → Buy, else → Sell
    prediction = "Buy" if len(stock) % 2 == 0 else "Sell"

    return jsonify({
        "stock": stock,
        "prediction": prediction
    })

if __name__ == "__main__":
    app.run(debug=True)
