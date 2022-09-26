import subprocess

subprocess.run(['git','init'])
subprocess.run(['git','add','.'])
subprocess.run(['git','commit','-m','"afafa"'])
subprocess.run(['git','push','heroku','master'])