from flask import render_template, current_app as app

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
        {'image': 'images/car4.jpg'}
    ]


    return render_template('pagina_user.html',menu=menu, ima=ima)