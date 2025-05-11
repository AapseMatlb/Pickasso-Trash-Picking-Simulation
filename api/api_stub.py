
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/start', methods=['POST'])
def start_patrol():
    return jsonify({"status": "Patrol Started"})

@app.route('/api/scan_map', methods=['POST'])
def scan_map():
    return jsonify({"status": "Mapping Started"})

@app.route('/api/battery', methods=['POST'])
def battery_update():
    data = request.get_json()
    battery = data.get("battery", "Unknown")
    return jsonify({"status": f"Battery updated to {battery}%"})

@app.route('/api/object_detected', methods=['POST'])
def object_detected():
    data = request.get_json()
    category = data.get("category", "unknown")
    return jsonify({"status": f"Object detected: {category}"})

@app.route('/api/status', methods=['GET'])
def status():
    return jsonify({"status": "Robot is operational", "battery": "80%"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
