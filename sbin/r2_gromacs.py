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



CLIENT_KEY = "6TCYXyf4lwTh601S1NpgbhlkyYgD5OQLbUvUq9Rf"
CLIENT_SECRET = "fZZC0uZ0aaoDICMeDsA6JXcf0ztSO7HW6t3elbQ3y4MxWdM11xGEG6l2R9zRLGxjntS5NT3bG3RcHDUL0mmJoT76PLJYHFDtSrDQFw5d6zHJ5XsyaZ9kYjX84VY82CYx"

__VERSION__ = "0.1dev"



USER_HOME_FOLDER = os.getenv('HOME')
RSQ_PROJECTS_HOME = os.path.join(USER_HOME_FOLDER, 'rsquarelabsProjects')
RSQ_PROJECTS_CONFIG = os.path.join(RSQ_PROJECTS_HOME, '.config.json')
RSQ_HOME = os.path.join(USER_HOME_FOLDER, '.rsquarelabs')
RSQ_DB_PATH = os.path.join(RSQ_HOME, 'rsquarelabs.db')


if not os.path.exists(RSQ_PROJECTS_HOME):
    os.mkdir(RSQ_PROJECTS_HOME,0755)

if not os.path.exists(RSQ_HOME):
    os.mkdir(RSQ_HOME,0755)

if not os.path.exists(RSQ_PROJECTS_CONFIG): # not very much needed
    os.mkdir(RSQ_PROJECTS_CONFIG, 0755)



from rsquarelabs_core.db_engine import DBEngine

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
        project_data["short_note"] = ""
        project_data["slug"] = ""
        project_data["path"] = ""
        project_data["type"] = TOOL_NAME

        # project_data['config'] = os.path.join(project_data["path"], 'r2_gromacs.json')
        # project_data['log'] = os.path.join(project_data["path"], 'r2_gromacs.log')





        while( project_data["title"].lstrip() == ""):
            project_data["title"] = raw_input("What would be your project Name: (TAK1 Modelling): ")

        while(project_data["tags"].lstrip() == ""):
            project_data["tags"] = raw_input("Please tag your project (eg: Molecular Dynamics, Minimisation, TAK1, GPCR5): ")

        while(project_data["user_email"].lstrip() == ""):
            project_data["user_email"] = raw_input("Your email for notification (eg: me@university.edu ): ")

        while (project_data["short_note"].lstrip() == ""):
            project_data["short_note"] = raw_input("Write a short note : ")

        generated_project_id = project_data["title"].replace(" ","-").replace("_","-")\
            .replace("/","-").replace("\\","-").replace(".","-").replace(",","-").replace(";",'-').replace(":","-").replace("--","-")



        customize_name = raw_input("Creating this project id as [%s], Do you wish to change ? (y/n , default=n): "%generated_project_id)

        if customize_name.lower() == 'n' or customize_name == '':
            project_data["slug"] = generated_project_id
        else:
            while(project_data["slug"].lstrip() == ""):
                project_data["slug"]  = raw_input("Enter the project_key : (tak1-modelling-trail1)")
        project_data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M")


        # join rsq proj home + slug
        PROJECT_PATH = os.path.join(RSQ_PROJECTS_HOME, project_data["slug"])



        if os.path.exists(PROJECT_PATH):
            while(os.path.exists(PROJECT_PATH)):
                project_data["slug"] = raw_input("Project with project key exists, Enter new key for the project : ")
            project_data["slug"] = project_data["slug"].replace(" ","-").replace("_","-")\
            .replace("/","-").replace("\\","-").replace(".","-").replace(",","-").replace(";",'-').replace(":","-").replace("--","-")
            PROJECT_PATH = os.path.join(RSQ_PROJECTS_HOME, project_data["slug"])
            os.mkdir(PROJECT_PATH, 0755)
        else:
            os.mkdir(PROJECT_PATH, 0755)
        project_data["log"] = os.path.join(PROJECT_PATH, 'r2_gromacs.log')
        project_data["config"] = os.path.join(PROJECT_PATH, 'r2_gromacs.config')
        fh_log = open(project_data["log"], 'w', 0755)
        fh = open(project_data["config"], 'w', 0755)
        
        
        # preprocessing data
        project_data["path"] = PROJECT_PATH
        
        
        proj1 = DBEngine(RSQ_DB_PATH)

        cur = proj1.do_insert("INSERT INTO projects (title, tags, user_email, slug, short_note, path, config, log, type, date)\
                        VALUES('%s', '%s', '%s', '%s', '%s','%s', '%s', '%s', '%s', '%s')"
                        % (project_data["title"],
                           project_data["tags"],
                           project_data["user_email"],
                           project_data["slug"],
                           project_data["short_note"],
                           project_data["path"],
                           project_data["config"],
                           project_data["log"],
                           project_data["type"],
                           project_data["date"],
                           ))





        if cur.rowcount: # if created into db
            from random import randint
            project_create_details = project_data # json.loads(project_data)
            project_create_details['project_id'] = randint(1,1000)
            fh_log.write("# RSQUARELABS-CORE v%s \n# Written by Ravi RT Merugu \n# https://github.com/rsquarelabs/rsquarelabs-core\n\n\n"%__VERSION__)

            mesg = """============================================
Project created with id '%s',
============================================""" % cur.lastrowid
            cprint(mesg, "green")
        else:
            os.remove(project_data["log"])
            os.remove(project_data["config"])
            os.rmdir(PROJECT_PATH)
            mesg =  "ERROR \n%s " %project_data['title']
            cprint(mesg, 'red')





    else:
        print "ERROR: please try 'r2_gromacs init'"


if __name__ == '__main__':
    main()