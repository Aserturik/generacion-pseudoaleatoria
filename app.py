from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import io
import base64
from congruencial_lineal import congruencial_lineal

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/congruencial_lineal', methods=['GET', 'POST'])
def congruencial_lineal_view():
    imagen = None
    resultados = None

    if request.method == 'POST':
        X0 = int(request.form['X0'])
        k = int(request.form['k'])
        c = int(request.form['c'])
        g = int(request.form['g'])
        minimo = float(request.form['minimo'])
        maximo = float(request.form['maximo'])
        n = int(request.form['n'])

        # Generar números pseudoaleatorios
        Xi, Ri, Ni = congruencial_lineal(X0, k, c, g, n, minimo, maximo)

        # Generar gráfico
        imagen = generar_grafico(Ni)

        # Preparar resultados para la tabla
        resultados = zip(range(1, n + 1), Xi, Ri, Ni)

    return render_template('congruencia_lineal.html', imagen=imagen, resultados=resultados)

def generar_grafico(numeros):
    plt.figure(figsize=(6,4))
    plt.plot(numeros, marker='o', linestyle='-')
    plt.title("Números Generados")
    plt.xlabel("Iteración")
    plt.ylabel("Valor")
    plt.grid()

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode()

if __name__ == '__main__':
    app.run(debug=True)
