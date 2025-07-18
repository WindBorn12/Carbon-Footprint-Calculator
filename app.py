from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hesapla', methods=['POST'])
def hesapla():
    elektrik = request.form['electricity']
    gaz = request.form['gas']
    su = request.form['water']

    return render_template('result.html',)

if __name__ == '__main__':
    app.run(debug=True)