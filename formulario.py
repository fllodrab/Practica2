#!/usr/bin/python
# -*- coding: utf-8 -*-

import web
from web import form


urls = (
	'/Formulario', 'Formulario',
	)

Email = form.regexp(r'(\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}\b)', 'El e-mail tiene que tener la forma miemail@servidormail.com')
Visa = form.regexp(r'([0-9]{4}) ([0-9]{4}) ([0-9]{4}) ([0-9]{4})|([0-9]{4})-([0-9]{4})-([0-9]{4})-([0-9]{4})', '4 grupos de 4 digitos separados por un espacio o -')

# Formulario
singUP = form.Form(
	form.Textbox("Nombre", form.notnull, description = "Nombre:"),
	form.Textbox("Apellidos", form.notnull, description = "Apellidos:", value = "Mengano"),
	form.Textbox("email", Email, description = "E-mail:", value = "tu email"),
	form.Dropdown('Dia', [('01', '01'), ('02','02'), ('04','04'), ('05','05'), ('06', '06'), ('07', '07'), ('08', '08'), ('09', '09'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], description="Dia:"),
	form.Dropdown('Mes', [('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo','Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre','Diciembre')], description = "Mes:"),
	form.Dropdown('Ano', [('1995', '1995'), ('1994', '1994'), ('1993', '1993'), ('1992', '1992'), ('1991', '1991'), ('1990', '1990'), ('1989', '1989')], description= "Anio:"),
	form.Textarea("Direccion", form.notnull, description = "Direccion:",),
	form.Password("Contrasena", form.notnull, description = "Contrasenia:"),
	form.Password("ReContrasena", form.notnull, description = "Reescribe contrasenia:"),
	form.Radio("MetodoDePago", [('Reembolso', 'Reembolso'),('VISA','VISA')], form.Validator('Tienes que seleccionar un metodo de pago', lambda x:'MetodoDePago' not in x), description = "Metodo de Pago"),
	form.Textbox("numVisa", Visa, description = "Numero tarjeta VISA:"),
	form.Checkbox("AceptoClausula", form.Validator('Tienes que aceptar las clausulas', lambda i:'AceptoClausula' not in i), description = "Acepto las clausulas de proteccion de datos"),
	form.Button("Enviar"),
	validators = [
		form.Validator("Las contraseñas no coinciden.", lambda y: y.Contrasena == y.ReContrasena)]
)


app = web.application(urls, globals())

class Formulario:
	def GET(self):
		form = singUP()		# Hacemos copia del formulario


		html = """
		<html>
			<head>
				<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
				<title>Formulario</title>
				<link rel="stylesheet" href="static/comun.css">
				<link rel="stylesheet" href="static/formulario.css">
			</head>
			<body>
				<h1>PRÁCTICA 3</h1>

				<p>Introduce tus datos</p>

				<form method="POST">
				%s
				</form>
			</body>
		</html>""" % (str(form.render()))	# Renderizamos el formulario

		return html 


	def POST(self):
		form = singUP()

		form.validates()	 # Validamos el formulario para obtener valores del usuario

		if not form.validates():
			return form.render()
		else:
			html = """
			<html>
				<head>
					<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
					<title>Práctica 3</title>
					<link rel="stylesheet" href="static/comun.css">
					<link rel="stylesheet" href="static/formulario.css">
				</head>
				<body>
					<h1>PRÁCTICA 3</h1>

					<p>Resultado formulario</p>
						<p>Nombre: <code>%s</code></p>
						<p>Apellidos: <code>%s</code></p>
						<p>E-mail: <code>%s</code></p>
						<p>Fecha de nacimiento: <code>%s</code> / <code>%s</code> / <code>%s</code></p>
						<p>Direccion: <code>%s</code></p>
						<p>Contrasena: <code>%s</code></p>
						<p>Metodo de pago: <code>%s</code></p>
						<p>Numero de Visa: <code>%s</code></p>
				</body>
			</html> """ % (str(form.d.Nombre), str(form.d.Apellidos), str(form.d.email), str(form.d.Dia), str(form.d.Mes), str(form.d.Ano), str(form.d.Direccion), str(form.d.Contrasena), str(form.d.MetodoDePago), str(form.d.numVisa))

			return html

if __name__ == '__main__':
    app.run()
