__author__ = 'rrmerugu'
__VERSION__ = "0.1dev"

import os, sys
from datetime import datetime
from termcolor import cprint


"""
adds the rsquarelabs-core module to this script path to access the modules inside rsquarelabs-core
"""
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)


"""
rsquarelabs_core should be imported after the CORE_DIR is added to sys.path
"""
from rsquarelabs_core.config import RSQ_PROJECTS_HOME, RSQ_DB_PATH
from rsquarelabs_core.engines.db_engine import DBEngine
from rsquarelabs_core.engines.gromacs.gromacs import ProteinLigMin, import_files


"""
Used to check if the command is executed in side a project or not.
If the command is executed inside a project, 'init' will be disabled and the rest will be active.
"""
CURRENT_PATH = os.getcwd()
TOOL_NAME = "r2_gromacs"
db_object = DBEngine(RSQ_DB_PATH)


def current_date():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
def show_comands():
    """
    Displays the command arguements available
    """
    available_commands = ['init', 'help', 'importfiles', 'createtopology', 'createwaterbox', 'neutralisecomplex', 'minimize']
    print "Available commands : \n"
    for command in available_commands:
        print command

def main():
    # Get the arguments list
    cmdargs = str(sys.argv)
    # check if config file exist in the working dir

    files_list = os.listdir(CURRENT_PATH)
    is_config_file_avaliable = False

    for file in files_list:
        if file == "r2_gromacs.config":
            is_config_file_avaliable = True
            project_key = CURRENT_PATH.split('/')[-1]
            project_id = db_object.do_select("select id from projects where slug='%s'"%project_key).fetchone()[0]
            print project_id


    obj = ProteinLigMin(
        ligand_file='ligand.gro',
        ligand_topology_file='ligand.itp',
        protein_file='protein.pdb',
        working_dir='./',
        verbose=True,
        quiet=False
    )

#
    if 'init' in cmdargs:
        if is_config_file_avaliable:
            print "ERROR! You can't start project in this directory"
            exit()
        print "Lets start the project"

        # check and create folder rsquarelabsProjects in $HOME
        project_data = {}
        project_data["title"] = ""
        project_data["tags"] = ""
        project_data["user_email"] = ""
        project_data["short_note"] = ""
        project_data["slug"] = ""
        project_data["path"] = ""
        project_data["type"] = TOOL_NAME



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
        fh_config = open(project_data["config"], 'w', 0755)

        # preprocessing data
        project_data["path"] = PROJECT_PATH



        cur = db_object.do_insert("INSERT INTO projects (title, tags, user_email, slug, short_note, path, config, log, type, date)\
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
            fh_config.write(cur.lastrowid)
            cprint(mesg, "green")
        else:
            os.remove(project_data["log"])
            os.remove(project_data["config"])
            os.rmdir(PROJECT_PATH)
            mesg =  "ERROR \n%s " %project_data['title']
            cprint(mesg, 'red')



    elif 'help' in cmdargs:
        show_comands()

    elif 'importfiles' in cmdargs:
        if is_config_file_avaliable:

            import_files(CURRENT_PATH, project_id)
        else:
            print "ERROR! This directory do not have project details"

    elif 'createtopology' in cmdargs:

        obj.create_topology()

    elif 'createwaterbox' in cmdargs:

        obj.prepare_system()
        obj.solvate_complex()

    elif 'neutralisecomplex' in cmdargs:

        obj.write_em_mdp()
        obj.add_ions()

    elif 'minimize' in cmdargs:

        obj.write_emreal_mdp()
        obj.minimize()

    else:
        print "ERROR: "
        show_comands()



if __name__ == '__main__':
    main()