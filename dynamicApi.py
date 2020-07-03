from flask import Flask
from string import Template
app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello ${place_name}!</h1>

<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}&key=AIzaSyCbRF6hHjyeo7_hEpjedl8K0KLgahVV_5E">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}&key=AIzaSyCbRF6hHjyeo7_hEpjedl8K0KLgahVV_5E">
""")

@app.route('/')
def homepage():
    return """<h1>Hello world!</h1>"""

@app.route('/<some_place>')
def some_place_page(some_place):
    return(HTML_TEMPLATE.substitute(place_name=some_place))

if __name__ == '__main__':
    app.run(debug=True)