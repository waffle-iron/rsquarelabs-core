import subprocess, sys, shlex

try:
    pop = subprocess.Popen(shlex.split("hostname"), stdout=subprocess.PIPE)

    ret = pop.poll()
    pro_id = pop.pid

    if ret == None:
        print 'Completed!'
        print pro_id

    else:
        print "HEADS UP: Killed by signal :(", -ret
        sys.exit()

except Exception as e:
    print "HEADS UP: Command failed"
    sys.exit()
#print ret


