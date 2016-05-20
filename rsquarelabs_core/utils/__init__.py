__author__ = 'rrmerugu'
import subprocess, shlex, sys, webbrowser


def run_process(step_no, step_name, command):
    print "INFO: Attempting to execute " + step_name + \
          " [STEP:" + step_no + "]"
    try:
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
