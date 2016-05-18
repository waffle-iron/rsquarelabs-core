__author__ = 'rrmerugu'

import os
import sys
from datetime import datetime

import bottle as bottle2
from bottle import Bottle, request, static_file, template, redirect

from rsquarelabs_core.utils import start_the_process

BASE_DIR    = os.path.join(os.path.dirname(os.path.dirname(__file__)),'websuite')
STATIC_DIR  = os.path.join(BASE_DIR, 'static')

HTML_DIR  = os.path.join(STATIC_DIR, 'html')
DOCS_DIR    = os.path.join(STATIC_DIR, 'docs')
CSS_DIR     = os.path.join(STATIC_DIR, 'css')
JS_DIR      = os.path.join(STATIC_DIR, 'js')


# USER_HOME_FOLDER = os.getenv('HOME')
# RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')
# RSQ_HOME_PROJECTS_LIST = os.path.join(RSQ_HOME, 'projects-list.json')


BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)
from rsquarelabs_core.engines.db_engine import DBEngine


# print BASE_DIR
# print STATIC_DIR
# print DOCS_DIR

USER_HOME_FOLDER = os.getenv('HOME')
RSQ_PROJECTS_HOME = os.path.join(USER_HOME_FOLDER, 'rsquarelabsProjects')
RSQ_PROJECTS_CONFIG = os.path.join(RSQ_PROJECTS_HOME, '.config.json') # not very much needed
RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')
RSQ_DB_PATH = os.path.join(RSQ_HOME, 'rsquarelabs.db')


proj1 = DBEngine(RSQ_DB_PATH)


# print index_html

app = Bottle()
#
now = datetime.now().strftime("%Y %b, %d %H:%M:%S %p")
bottle2.TEMPLATE_PATH.insert(0,HTML_DIR)


@app.route('/websuite/rmv.html')
def rmv():
    qs_string = request.query_string
    file_name = None
    if 'file=' in qs_string:
        file_name = qs_string.split('file=')[1].split('&')[0]
        print file_name
    content = open(os.path.join(HTML_DIR, 'rmv.html')).read()
    return template(content, file_name=file_name,now=now)



# @app.route('/websuite/rmv/:name')
# def rmv_external(name):
#
#     content = open(os.path.join(HTML_DIR, 'rmv.html')).read()
#     return template(content , name=name)


@app.route('/index')
@app.route('/home')
@app.route('/')
@app.route('/websuite')
# @app.route('/websuite/')
def goto_index():
    redirect('/websuite/index.html')


@app.route('/websuite/index.html')
def index():
    print HTML_DIR
    print BASE_DIR
    content = open(os.path.join(HTML_DIR, 'websuite_index.html')).read()
    return template(content, now=now)

@app.route('/docs/rmv')
def goto_rmv():
    redirect('/docs/rmv.html')

@app.route('/docs/rmv.html')
def docs():
    content =  open(os.path.join(DOCS_DIR, 'rmv.html')).read()
    return template(content,now=now)


@app.route('/websuite/projects.html')
def projects_list():
    # projects_list = open(RSQ_HOME_PROJECTS_LIST).read()
    # projects_data = json.loads(projects_list)
    projects_data = proj1.do_select("SELECT id, slug, title, tags, user_email, type, path, log, date from projects")
    content =  open(os.path.join(HTML_DIR, 'projects.html')).read()
    return template(content, projects_list=projects_data,now=now)


@app.route('/websuite/project/:project_id')
def projects_status(project_id):
    project_data = proj1.do_select("SELECT  id, slug, title, short_note, tags, user_email, type, path, log, config, date from projects where id = %s"%(int(project_id))).fetchone()

    if project_data is None:
        project_log= None
        project_config = None
        file_list = None
    else:
        project_log = open(project_data[8], 'r').read()
        project_config = open(project_data[9], 'r').read()
        file_list = os.listdir(project_data[7])
    content = open(os.path.join(HTML_DIR, 'project-status.html')).read()
    return template(content, file_list=file_list, project_log=project_log, project_config=project_config, project_data=project_data, now=now)



@app.route('/docs/filebrowser')
def goto_filebrowser():
    redirect('/docs/filebrowser.html')

@app.route('/websuite/filebrowser.html')
def filebrowser():
    content = open(os.path.join(HTML_DIR, 'file_browser.html')).read()
    folder_path = os.path.dirname(__file__)
    folder_name = os.path.split(folder_path)[1]
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    return template(content, files_data = files, folder_name = folder_name, folder_path= folder_path,now=now )


@app.error(404)
def error404(error):
    content = open(os.path.join(HTML_DIR, '404_error.html')).read()
    return template(content)

@app.route('/assets/css/<filename>')
def server_static(filename):
    return static_file(filename, root=CSS_DIR)



def server_run():
    """
    Named _run to make this component more reusable
    """
    app.run(host='localhost', port=9090, debug=False, reloader=True, liveport=9999) #, quiet=True


def server_start_cmd():
    cmd = "nohup python %s/../bin/r2_server_start.py > /dev/null & " %(os.path.dirname(os.path.dirname(__file__)) )
    start_the_process(cmd)


