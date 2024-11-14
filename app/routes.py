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
        {'icon': 'truck', 'text': 'Guía de Remisión'},
        {'icon': 'arrow-clockwise', 'text': 'Nota de Crédito'},
        {'icon': 'file-earmark-minus', 'text': 'Nota de Débito'},
        {'icon': 'journal-album', 'text': 'Liquidación de Compras'},
        {'icon': 'file-earmark-text', 'text': 'Proformas'},
        {'icon': 'cash-stack', 'text': 'Cuentas por Cobrar'}
    ]
    return render_template('pagina_principal.html', buttons=buttons)
