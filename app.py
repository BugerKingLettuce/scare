from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# Route to serve the HTML file
@app.route('/')
def index():
    return send_from_directory('webpage', 'index.html')  # Serve index.html

# Route to serve static files (image and sound)
@app.route('/media/<path:filename>')
def serve_static(filename):
    return send_from_directory('media', filename)

if __name__ == '__main__':
    app.run(debug=True)
