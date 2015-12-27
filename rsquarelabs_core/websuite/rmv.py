__author__ = 'rrmerugu'

from bottle import Bottle, request, static_file, template, redirect
import os
import bottle as bottle2
from rsquarelabs_core.utils import start_the_process
import json

from datetime import datetime
BASE_DIR    = os.path.join(os.path.dirname(os.path.dirname(__file__)),'websuite')
STATIC_DIR  = os.path.join(BASE_DIR, 'static')

HTML_DIR  = os.path.join(STATIC_DIR, 'html')
DOCS_DIR    = os.path.join(STATIC_DIR, 'docs')
CSS_DIR     = os.path.join(STATIC_DIR, 'css')
JS_DIR      = os.path.join(STATIC_DIR, 'js')


USER_HOME_FOLDER = os.getenv('HOME')
RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')
RSQ_HOME_PROJECTS_LIST = os.path.join(RSQ_HOME, 'projects-list.json')

# print BASE_DIR
# print STATIC_DIR
# print DOCS_DIR





# print index_html

app = Bottle()
#
bottle2.TEMPLATE_PATH.insert(0,HTML_DIR)


@app.route('/websuite/rmv.html')
def rmv():
    # print request.url_args
    print request.url
    print request.query_string
    # print request.urlparts
    # print request.get('file')
    # print request.params
    # print request.query
    qs_string = request.query_string
    file_name = None
    if 'file=' in qs_string:
        file_name = qs_string.split('file=')[1].split('&')[0]
        print file_name
    content = open(os.path.join(HTML_DIR, 'rmv.html')).read()
    return template(content, file_name=file_name)



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
    return template(content)

@app.route('/docs/rmv')
def goto_rmv():
    redirect('/docs/rmv.html')

@app.route('/docs/rmv.html')
def docs():
    content =  open(os.path.join(DOCS_DIR, 'rmv.html')).read()
    return template(content)


@app.route('/websuite/projects.html')
def projects_list():
    projects_list = open(RSQ_HOME_PROJECTS_LIST).read()
    projects_data = json.loads(projects_list)
    content =  open(os.path.join(HTML_DIR, 'projects.html')).read()
    return template(content, projects_list=projects_data)


@app.route('/websuite/project/:project_id')
def projects_list(project_id):

    qs_string = request.query_string
    project_path = None
    if 'project_path=' in qs_string:
        project_path = qs_string.split('project_path=')[1].split('&')[0]

    print project_id
    print project_path


    projects_list = open(RSQ_HOME_PROJECTS_LIST).read()
    projects_data = json.loads(projects_list)
    project_log_updated_time = None
    project_log = None
    project_user_email = None
    project_config = None

    for project in projects_data['projects']:
        if project['project_path'] == project_path and project['project_id'] == project_id:
            # found this :D
            pass
            print "Found this :D"
            project_log = open(os.path.join(project['project_path'], "%s.log"%project['project_type'] )).read()
            project_config = open(os.path.join(project['project_path'], "%s.json"%project['project_type'] )).read()
            project_user_email = project['project_user_email']
            project_log_updated_time = os.path.getmtime(os.path.join(project['project_path'], "%s.log"%project['project_type'] ))

            project_log_updated_time = datetime.fromtimestamp(project_log_updated_time).strftime('%Y-%m-%d %H:%M:%S')
            print project_log
    content =  open(os.path.join(HTML_DIR, 'project-status.html')).read()
    return template(content, project_log=project_log, project_config=project_config, project_user_email = project_user_email, project_log_updated_time=project_log_updated_time)



@app.route('/docs/filebrowser')
def goto_filebrowser():
    redirect('/docs/filebrowser.html')

@app.route('/websuite/filebrowser.html')
def filebrowser():
    content = open(os.path.join(HTML_DIR, 'file_browser.html')).read()
    folder_path = os.path.dirname(__file__)
    folder_name = os.path.split(folder_path)[1]
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    return template(content, files_data = files, folder_name = folder_name, folder_path= folder_path )


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
    app.run(host='localhost', port=9090, debug=False) #, quiet=True


def server_start_cmd():
    cmd = "nohup python %s/../bin/r2_server_start.py > /dev/null & " %(os.path.dirname(os.path.dirname(__file__)) )
    start_the_process(cmd)


