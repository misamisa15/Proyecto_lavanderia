from flask import render_template, request, redirect, url_for, current_app as app

@app.route('/')
def index():
    buttons = [
        {'icon': 'person', 'text': 'Clientes'},
        {'icon': 'database', 'text': 'Produc/Servicios'},
        {'icon': 'file-earmark-check', 'text': 'Nueva Factura'},
        {'icon': 'receipt', 'text': 'Comprobantes'},
        {'icon': 'receipt-cutoff', 'text': 'Nueva Retención'},
        {'icon': 'journal-text', 'text': 'Lista Retenciones'},
        {'icon': 'arrow-clockwise', 'text': 'Nota de Crédito'},
        {'icon': 'file-earmark-minus', 'text': 'Nota de Débito'},
        {'icon': 'journal-album', 'text': 'Liquidación de Compras'},
        {'icon': 'file-earmark-text', 'text': 'Proformas'},
        {'icon': 'cash-stack', 'text': 'Cuentas por Cobrar'}
    ]
    return render_template('pagina_principal.html', buttons=buttons)

@app.route('/pagina_user.html')
def paguser():
    menu = [
        {'text': 'Inicio'},
        {'text': 'Turnos'},
        {'text': 'Servicios'},
        {'text': 'Compras'},
        {'text': 'Facturas'}
    ]
    ima = [
        
        {'image': 'images/car3.jpg'},
        {'image': 'images/logo_lava.jpg'},
        {'image': 'images/car4.jpg'},
        {'image': 'images/publi_lava.jpg'}
    ]


    return render_template('pagina_user.html',menu=menu, ima=ima)

products = [
    {'name': 'Producto 1', 'description': 'Descripción del Producto 1', 'price': 10.0},
    {'name': 'Producto 2', 'description': 'Descripción del Producto 2', 'price': 15.5},
    # Agrega más productos si deseas
]
@app.route('/produc_servicios', methods=['GET', 'POST'])
def produc_servicios():
    if request.method == 'POST':
        # Recibir datos del formulario
        product_name = request.form.get('product_name')
        product_description = request.form.get('product_description')
        
        # Añadir el producto a la lista o base de datos
        products.append({'name': product_name, 'description': product_description})
        
        # Redirigir a la misma página después de añadir el producto
        return redirect(url_for('produc_servicios'))
    
    # Renderizar la plantilla de productos
    return render_template('produc_servicios.html')

@app.route('/clientes', methods=['GET', 'POST'])
def clientes():
    # Lista de clientes (en este caso, lista simulada, puedes cambiarla por una base de datos)
    clientes = [
        {'cedula': '1234567890', 'nombres': 'Juan Pérez', 'telefono': '0987654321', 'correo': 'juan@example.com'},
        {'cedula': '0987654321', 'nombres': 'María López', 'telefono': '0981234567', 'correo': 'maria@example.com'},
    ]

    if request.method == 'POST':
        # Obtener datos del formulario
        cedula = request.form.get('cedula')
        nombres = request.form.get('nombres')
        telefono = request.form.get('telefono')
        correo = request.form.get('correo')
        
        # Agregar nuevo cliente a la lista (o base de datos)
        clientes.append({'cedula': cedula, 'nombres': nombres, 'telefono': telefono, 'correo': correo})
        
        # Redirigir a la misma página para actualizar la lista
        return redirect(url_for('clientes'))
    
    # Renderizar la plantilla de clientes
    return render_template('clientes.html', clientes=clientes)
