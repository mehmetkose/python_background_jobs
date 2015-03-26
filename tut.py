import time
print "basladi tut.py"
time.sleep(20)
print "bitti tut.py"

file_path = './tut.file'
try:
    fp = open(file_path)
except IOError:
    fp = open(file_path, 'w+')
