__author__ = 'rrmerugu'

# from optparse import OptionParser
from termcolor import colored, cprint
import sys, os, json, requests
from datetime import datetime
# get argument list using sys module

# TODO - Need improvements
sys.argv
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)
from rsquarelabs_core.db_engine import DBEngine


CLIENT_KEY = "6TCYXyf4lwTh601S1NpgbhlkyYgD5OQLbUvUq9Rf"
CLIENT_SECRET = "fZZC0uZ0aaoDICMeDsA6JXcf0ztSO7HW6t3elbQ3y4MxWdM11xGEG6l2R9zRLGxjntS5NT3bG3RcHDUL0mmJoT76PLJYHFDtSrDQFw5d6zHJ5XsyaZ9kYjX84VY82CYx"

__VERSION__ = "0.1dev"



USER_HOME_FOLDER = os.getenv('HOME')
RSQ_PROJECTS_HOME = os.path.join(USER_HOME_FOLDER, 'rsquarelabsProjects')
RSQ_PROJECTS_CONFIG = os.path.join(RSQ_PROJECTS_HOME, '.config.json')
RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')
RSQ_DB_PATH = os.path.join(RSQ_HOME, 'tables.db')

TOOL_NAME = "r2_gromacs"

def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    # Get the arguments list
    cmdargs = str(sys.argv)
    #print cmdargs

    if 'init' in cmdargs:
        print "Lets start the project"

        # check and create folder rsquarelabsProjects in $HOME
        


        current_folder =  os.getcwd()

        project_data = {}
        project_data["title"] = ""
        project_data["tags"] = ""
        project_data["user_email"] = ""
        project_data["slug"] = ""
        project_data["path"] = os.getcwd()
        project_data["type"] = TOOL_NAME

        project_data['config'] = os.path.join(project_data["path"], 'r2_gromacs.json')
        project_data['log'] = os.path.join(project_data["path"], 'r2_gromacs.log')


        if os.path.exists(project_data['config']) :
            mesg = "ERROR: A Project already exist in this folder\n============================================="
            cprint(mesg, 'red')
            exit()
        else:
            fh = open(project_data['config'] , 'w', 0755)
            fh_log = open(project_data['log'],'w', 0755)



        while( project_data["title"].lstrip() == ""):
            project_data["title"] = raw_input("What would be your project Name: (TAK1 Modelling): ")

        while(project_data["tags"].lstrip() == ""):
            project_data["tags"] = raw_input("Please tag your project (eg: Molecular Dynamics, Minimisation, TAK1, GPCR5): ")

        while(project_data["user_email"].lstrip() == ""):
            project_data["user_email"] = raw_input("Your email for notification (eg: me@university.edu ): ")

        generated_project_id = project_data["title"].replace(" ","-").replace("_","-")\
            .replace("/","-").replace("\\","-").replace(".","-").replace(",","-").replace(";",'-').replace(":","-").replace("--","-")



        customize_name = raw_input("Creating this project id as [%s], Do you wish to change ? (y/n , default=n): "%generated_project_id)

        if customize_name.lower() == 'n' or customize_name == '':
            project_data["slug"] = generated_project_id
        else:
            while(project_data["slug"].lstrip() == ""):
                project_data["slug"]  = raw_input("Enter the project_key : (tak1-modelling-trail1)")

        project_data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")




        if os.path.exists(RSQ_HOME):
            pass
        else:
            os.mkdir(RSQ_HOME, 0755)

        # now save this config info to ~/.rsquarelabs/projects.json
        # if os.path.exists(RSQ_HOME_PROJECTS_LIST):
        #     old_data = open(RSQ_HOME_PROJECTS_LIST).read()
        #     projects_list_fh = open(RSQ_HOME_PROJECTS_LIST) ## dont open in write mode
        # else:
        #     projects_list_fh = open(RSQ_HOME_PROJECTS_LIST,"w",755)
        #     old_data = ""
        #
        proj1 = DBEngine('tables.db')

        cur = proj1.do_insert("INSERT INTO projects (title, tags, user_email, slug, path, config, log, type, date)\
                        VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"
                        % (project_data["title"],
                           project_data["tags"],
                           project_data["user_email"],
                           project_data["slug"],
                           project_data["path"],
                           project_data["config"],
                           project_data["log"],
                           project_data["type"],
                           project_data["date"],
                           ))
        print cur


        # print old_data
        # print len(old_data)
        # if len(old_data) != 0:
        #     projects_list_fh = open(RSQ_HOME_PROJECTS_LIST, "w", 755)
        #     # convert string to dict
        #     data_from_file = json.loads(old_data)
        #     old_projects_data = data_from_file['projects']
        #     old_projects_data.append(project_data)
        #
        #     thedata = {}
        #     thedata['projects'] = old_projects_data
        #     thedata['last_update'] =  current_date()
        #
        # else:
        #     projects_list_fh = open(RSQ_HOME_PROJECTS_LIST,"w",755)
        #     thedata = {}
        #     thedata['projects'] = []
        #     thedata['last_update'] =  current_date()
        #     thedata['projects'].append(project_data)
            # projects_list_fh.write(json.dumps(thedata))


        # print project_data

        ## sending this info to rsquarelabs-apis
        # headers = {'content-type': 'application/json'}
        # req = requests.post("http://localhost:8000/restful/project/",  headers=headers, data= json.dumps(project_data))


        if True: # if created into db
            from random import randint
            project_create_details = project_data # json.loads(project_data)
            project_create_details['project_id'] = randint(1,1000)
            fh_log.write("# RSQUARELABS-CORE v%s \n# Written by Ravi RT Merugu \n# https://github.com/rsquarelabs/rsquarelabs-core\n\n\n"%__VERSION__)

            mesg = """============================================
Project created with id '%s',
============================================""" % cur.lastrowid
            cprint(mesg, "green")
        else:

            mesg =  "ERROR \n%s " %project_data['title']
            cprint(mesg, 'red')
            os.remove(project_data['config'])




    else:
        print "ERROR: please try 'r2_gromacs init'"


if __name__ == '__main__':
    main()