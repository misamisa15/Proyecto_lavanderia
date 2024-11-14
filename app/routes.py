from flask import render_template, current_app as app

@app.route('/')
def index():
    buttons = [
        {'icon': 'house', 'text': 'Inicio'},
        {'icon': 'gear', 'text': 'Configuración'},
        {'icon': 'person', 'text': 'Perfil'},
    ]
    return render_template('pagina_principal.html', buttons=buttons)
