__author__ = 'rrmerugu'

import os, sys
# BIN_DIR = os.path.dirname(os.path.abspath(__file__))
# CORE_DIR = os.path.join(BIN_DIR, '../')
# sys.path.append(CORE_DIR)


import os, sys
BIN_DIR = os.path.dirname(os.path.abspath(__file__))
CORE_DIR = os.path.join(BIN_DIR, '../')
sys.path.append(CORE_DIR)


from rsquarelabs_core.websuite.rmv import server_start_cmd


server_start_cmd()


## 

# import threading
# def background(f):
#     '''
#     a threading decorator
#     use @background above the function you want to run in the background
#     '''
#     def bg_f(*a, **kw):
#         threading.Thread(target=f, args=a, kwargs=kw).start()
#     return bg_f
#
#
#
# @background
# runapp()
#
# import threading
# threading.Thread(target=server_start).start()






#
# import thread
#
# def someFunc():
#     print "someFunc was called"
#
# thread.start_new_thread(server_start, ())
#
# print "Helo"


#
# from multiprocessing import Process
#
# Process(group=None,target=runapp,name=None, args=(), kwargs={}).run()
# print "Hello"

# open_browser_run()
#
# cmd = "nohup python /Users/rrmerugu/PycharmProjects/rsquarelabs/bin/r2_server_start.py > /dev/null &"
#
# # import subprocess
# # # cmd = 'python script.py'
# #
# # p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
# # out, err = p.communicate()
# """
# Log this into r2_server.log in ~/.r2_websuite/
# """
# # result = out.split('\n')
# # for lin in result:
# #     if not lin.startswith('#'):
# #         print(lin)
