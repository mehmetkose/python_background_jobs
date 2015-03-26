import time
print "basladi atla.py"
time.sleep(20)
print "bitti atla.py"

file_path = './atla.file'
try:
    fp = open(file_path)
except IOError:
    fp = open(file_path, 'w+')
