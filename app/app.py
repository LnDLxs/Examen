from flask import Flask 
from flask import render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods= ['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            nombre = request.form['nombre']
            edad = int(request.form['edad'])
            cantidad = int(request.form['cantidad'])
        except KeyError:
            return "Por favor complete todos los campos del formulario.", 400

        precio_tarro = 9000
        total_sin_descuento = cantidad * precio_tarro
        descuento = 0

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25

        monto_descuento = total_sin_descuento * descuento
        total_con_descuento = total_sin_descuento - monto_descuento

        resultado = {
            'nombre': nombre,
            'total_sin_descuento': total_sin_descuento,
            'monto_descuento': monto_descuento,
            'total_con_descuento': total_con_descuento
        }

        return render_template('ejercicio1.html', resultado=resultado)
    
    return render_template('ejercicio1.html', resultado=None)

@app.route('/ejercicio2', methods = ['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
        
        usuarios = {
            'Juan': 'admin',
            'Pepe': 'user'
        }
        
        if nombre in usuarios and usuarios[nombre] == password:
            if nombre == 'juan':
                mensaje = f'Bienvenido administrador {nombre}'
            else:
                mensaje = f'Bienvenido usuario {nombre}'
        else:
            mensaje = 'Nombre de usuario o contraseña incorrectos'
        
        return render_template('ejercicio2.html', mensaje=mensaje)
    
    return render_template('ejercicio2.html', mensaje=None)
if __name__ == '__main__':
    app.run(debug=True,port=5000)