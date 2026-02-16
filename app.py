from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to CI/CD Flask App!",
        "version": "1.0.0",
        "status": "running"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "environment": os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/api/info')
def info():
    return jsonify({
        "app": "Flask CI/CD Demo",
        "author": "DevOps Engineer",
        "description": "Automated deployment pipeline demonstration"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
