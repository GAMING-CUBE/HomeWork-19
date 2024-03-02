import os
import time

filename = 'input.txt'

last_modified_timestamp = os.path.getmtime(filename)
last_modified_time = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(last_modified_timestamp))

created_timestamp = os.path.getctime(filename)
created_time = time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(created_timestamp))

print("Last modified:", last_modified_time)
print("Created:", created_time)
