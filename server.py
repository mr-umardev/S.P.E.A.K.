import os
import subprocess
from flask import Flask, jsonify, send_from_directory

app = Flask(__name__, static_folder='static')

# Ensure we use the Python inside the virtual environment
VENV_PYTHON = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")

@app.route('/')
def serve_index():
    """ Serve the frontend HTML file """
    return send_from_directory("static", "index.html")

@app.route('/run-main', methods=['POST'])
def run_main():
    try:
        subprocess.Popen([VENV_PYTHON, "main.py"], cwd=os.getcwd())  # Runs main.py inside venv
        return jsonify({"message": "main.py started"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/run-app', methods=['POST'])
def run_app():
    try:
        subprocess.Popen([VENV_PYTHON, "app.py"], cwd=os.getcwd())  # Runs app.py inside venv
        return jsonify({"message": "app.py started"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
