from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Función para calcular el IMC
def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return round(imc, 2)
    except ZeroDivisionError:
        return "Altura no válida"

# Ruta principal que renderiza la página con el formulario
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar el formulario y calcular el IMC
@app.route('/calcular', methods=['POST'])
def calcular():
    if request.method == 'POST':
        try:
            peso = float(request.form['peso'])
            altura = float(request.form['altura'])
            imc = calcular_imc(peso, altura)
            return render_template('index.html', imc=imc, peso=peso, altura=altura)
        except ValueError:
            return render_template('index.html', error="Por favor, ingresa valores válidos.")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

