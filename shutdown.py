import os

f = open('test.bat','w')
f.write('shutdown /s')
f = open('test.bat','r')

os.system('test.bat')
