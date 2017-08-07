# Load the modules   
import os, sys 

if os.getuid() !=0: 
	raise Exception ('This script must be run as root')

# Just for sanity
script_name = sys.argv[0]

# Get the file path -- CLI arg is in 1
path = sys.argv[1]
def main(); 
	print ('Hola bunbuns, como estas?', sys.argv[1])

# Define the path structure 
service_name = path.split('/')[-2]

# One process
supervisor_conf = """[program:%(service_name)s]
command=%(path)s
numprocs=1
autostart=true
autorestart=true""" % {'path': path, 'service_name': service_name}

# Automatic deploy via supervisor 
f = open('/etc/supervisor/conf.d/%s.conf' % service_name, 'w')
f.write(supervisor_conf)
f.close()

# Don't lose your way! 