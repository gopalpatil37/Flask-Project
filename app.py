from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def create_app():
    return "<h2>Welcome to the Flask App!</h2>"

if __name__ == '__main__':
    app.run(debug=True)