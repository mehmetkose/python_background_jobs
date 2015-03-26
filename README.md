# python_background_jobs
an example of python background jobs with bash

try this:

chmod +x ./job.sh
python example.py

-> example.py will call job.sh without outputs 
-> job.sh call atla.py and tut.py. this files are our example workers.
-> atla.py and tut.py will create atla.file and tut.file after 20 seconds, but you're not seen ever callback.
