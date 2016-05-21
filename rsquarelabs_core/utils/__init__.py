__author__ = 'rrmerugu'
import subprocess, shlex, sys, webbrowser
from rsquarelabs_core.engines.db_engine import  DBEngine
from rsquarelabs_core.config import RSQ_DB_PATH
from datetime import datetime

db_object = DBEngine(RSQ_DB_PATH)

def check_process():
    pass


def run_process(step_no, step_name, command, tool_name, log_file):
    """
    This method will
    step1: save the incoming command request info into db
    step2: executes the command
    step3: saves the pid of running and changes the command status to executing
    (whether executed or not is checked by other method 'check_process()' )

    :param step_no: Step number in the workflow (this helps us in tracking how many times the user failed at this step
    and also we use the last of this step no from the records as the final command that worked for the user :) )
    :param step_name: Step name in the workflow - an identifier
    :param command: the command to execute
    :return:
    """
    print "INFO: Attempting to execute " + step_name + \
          " [STEP:" + step_no + "]"
    try:

        ## insert the command into the db with status (inactive)
        cur = db_object.do_insert("""
        insert into project_activity(tool_name,step_no, step_name , command, status, log_file, created_at )
        VALUES ('%s','%s','%s','%s','%s','%s','%s')
        """ %(tool_name, step_no, step_name, command, 'to_run', log_file, datetime.now()  ))

        pop = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE)
        ret = pop.poll()
        pro_id = pop.pid


        if ret == None:
            print 'Completed!'
            return pro_id

        else:
            print "HEADS UP: Killed by signal :(", -ret
            sys.exit()

    except Exception as e:
        print "HEADS UP: Command failed"
        sys.exit()




def browser_register():
    webbrowser.register('r2labs_browser')

def brower_open(url):
    print "Opening the link '%s' " %url
    webbrowser.open_new(url)
    return webbrowser
