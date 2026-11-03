from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    """Render halaman utama PA Jarkom Survival Kit (Huawei VRP eNSP)."""
    return render_template("index.html")

@app.route("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "app": "PA Jarkom Survival Kit - Huawei VRP (eNSP)",
        "modules": 8,
        "boss_battles": 2
    })

if __name__ == "__main__":
    print("🌷 Menjalankan PA Jarkom Survival Kit di http://127.0.0.1:5000 ...")
    app.run(host="0.0.0.0", port=5000, debug=True)
