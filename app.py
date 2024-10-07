from flask import Flask
# Hello Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! This is a simple Flask app."

if __name__ == '__main__':
    app.run(debug=True)
