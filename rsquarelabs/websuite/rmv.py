__author__ = 'rrmerugu'

from bottle import Bottle, request, static_file, template
import os


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),'websuite')
print BASE_DIR
STATIC_DIR = os.path.join(BASE_DIR, 'static')
print STATIC_DIR


index_html = open(os.path.join(STATIC_DIR, 'index.html')).read()

print index_html

app = Bottle()
@app.route('/websuite/rmv/:name')
def index(name):
    filename = request.GET.get('file', 'protein.121212232.pdb')
    return template(index_html , name=name)


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return "<h1 style='text-align:center;'>Welcome to RSQUARE LABS websuite</h1><br><br><br> <p style='text-align:center; '><a  href='http://rsquarelabs.xyz' target='_blank'>visit website</a></p>"

@app.error(404)
def error404(error):
    return "<h4 style='text-align:center;' >There is no such url. 404 Error!!!</h4>"

def runapp():
    app.run(host='localhost', port=9090, debug=False)