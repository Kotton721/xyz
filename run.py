import subprocess

subprocess.run(['git','init'])
subprocess.run(['sudo','git','add','music/test.wav','locations.csv','gpsexa.gpx','app.py'])
subprocess.run(['sudo','git','commit','-m','"afafa"'])