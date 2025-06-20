from flask import Flask, render_template , request

BACKEND_URL = 'http://0.0.0.0:5000'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6000)
