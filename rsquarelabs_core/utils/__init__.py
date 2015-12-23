__author__ = 'rrmerugu'



import subprocess, webbrowser




def start_the_process(cmd):
    """
    log this to ~/.r2_labs/processes.log
    """
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    out, err = p.communicate()
    result = out.split('\n')
    # for lin in result:
    #     if not lin.startswith('#'):
    #         print(lin)



def browser_register():
    webbrowser.register('r2labs_browser')

def brower_open(url):
    print "Opening the link '%s' " %url
    webbrowser.open_new(url)
    return webbrowser
