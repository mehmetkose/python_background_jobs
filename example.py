import subprocess,os

os.chdir(os.path.abspath('./'))

print "hello example application here."
subprocess.Popen('./job.sh > /dev/null 2>&1 &', stdout=subprocess.PIPE, shell=True)
print "tasks added."
