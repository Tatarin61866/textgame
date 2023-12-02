
from flask import Flask, request

app = Flask('lab04')

def make_content_radio_and_list(value):
	content = ''
	if value == "red":
		content += '<font color="#700">Red</font> selected'
	elif value == "red2":
		content += '<font color="#700">Red 2</font> selected'
	elif value == "green":
		content += '<font color="#070">Green</font> selected'
	elif value == "green2":
		content += '<font color="#070">Green 2</font> selected'
	elif value == "blue":
		content += '<font color="#007">Blue</font> selected'
	elif value == "blue2":
		content += '<font color="#007">Blue 2</font> selected'
	else:
		return None
	return content
		

def make_html_doc(name, content):
	doc = f"""
	<!doctype html>
	<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>g12_nemilov lab04</title>
	</head>
	<body>
		<h1>{name}</h1>
		<hr>"""
	doc += content
	doc += """</body>
	</html>
	"""
	return doc

@app.route('/checkboxes', methods=['GET', 'POST'])
def checkboxes():
	if request.method == "GET":
		val1 = request.args.get('red')
		val2 = request.args.get('green')	
		val3 = request.args.get('blue')
	else:
		val1 = request.form.get('red')
		val2 = request.form.get('green')
		val3 = request.form.get('blue')
			
	content = ''
	if val1 == None:
		content += '<font color="#700">Red</font> is NOT selected<br>'
	else:
		content += '<font color="#700">Red</font> selected<br>'
		
	if val2 == None:
		content += '<font color="#070">Green</font> is NOT selected<br>'
	else:
		content += '<font color="#070">Green</font> selected<br>'
	
	if val3 == None:
		content += '<font color="#007">Blue</font> is NOT selected<br>'
	else:
		content += '<font color="#007">Blue</font> selected<br>'
	
	return make_html_doc('Checkboxes', content)
	
@app.route('/radiobuttons_and_lists', methods=['GET', 'POST'])
def radiobuttons_and_lists():
	if request.method == "GET":
		desc = request.args.get('description')
		val1 = request.args.get('box')	
		val2 = request.args.get('box2')
	else:
		desc = request.form.get('description')
		val1 = request.form.get('box')	
		val2 = request.form.get('box2')
		
	content = ''
	
	content1 = make_content_radio_and_list(val1)
	if content1 == None:
		content += 'Color is not selected'
	else:
		content += content1
	content += '<br>'
	content += 'and<br>'
	content2 = make_content_radio_and_list(val2)
	if content2 == None:
		content += 'Second color is not selected'
	else:
		content += content2
	content += '<br>'

	
	return make_html_doc(desc, content)
	

