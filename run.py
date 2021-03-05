from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', zm = 'Analityk.edu')

@app.route('/innastrona')
def innastrona():
    return 'Witam na innej stronie!'

@app.route('/klient/<numer>')
def klient(numer):
    return f'Klient o podanym numerze {numer} to ...'

@app.route('/dodaj/<zmienna1>+<zmienna2>')
def dodaj(zmienna1, zmienna2):
    wynik = int(zmienna1)+int(zmienna2)
    return f'wynik to: {wynik}'

if __name__ == '__main__':
    app.run(debug=True) #tylko i wycznie w srodowisku developerskim
