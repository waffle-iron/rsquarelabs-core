__author__ = 'rrmerugu'

from bottle import Bottle, request, static_file, template
import os


BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)),'websuite')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
DOCS_DIR = os.path.join(STATIC_DIR, 'docs')
CSS_DIR = os.path.join(STATIC_DIR, 'css')
JS_DIR      = os.path.join(STATIC_DIR, 'js')


print BASE_DIR
print STATIC_DIR
print DOCS_DIR





# print index_html

app = Bottle()
@app.route('/websuite/rmv/:name')
def index(name):
    filename = request.GET.get('file', 'protein.121212232.pdb')
    content = open(os.path.join(STATIC_DIR, 'index.html')).read()
    return template(content , name=name)


@app.route('/index')
@app.route('/home')
@app.route('/')
def index():
    return "<h1 style='text-align:center;'>Welcome to RSQUARE LABS websuite</h1><br><br><br> <p style='text-align:center; '><a  href='http://rsquarelabs.xyz' target='_blank'>visit website</a></p>"

@app.route('/docs/rmv')
def docs():
    content =  open(os.path.join(DOCS_DIR, 'rmv.html')).read()
    return template(content)


@app.error(404)
def error404(error):
    return "<h4 style='text-align:center;' >There is no such url. 404 Error!!!</h4>"

@app.route('/assets/css/<filename>')
def server_static(filename):
    return static_file(filename, root=CSS_DIR)

def runapp():
    app.run(host='localhost', port=9090, debug=False, liveport=9090)
