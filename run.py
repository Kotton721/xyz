import subprocess

subprocess.run(['git','init'])
subprocess.run(['git','add','music/test.wav','locations.csv','gpsexa.gpx','app.py'])
subprocess.run(['git','commit','-m','"afafa"'])