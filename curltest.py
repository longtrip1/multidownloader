import os
import subprocess
wd = (os.getcwd())
link = (input('输入链接'))
#downloadthread = input('输入下载线程')
downloadbat = wd+'/download.bat'
file = open(downloadbat,'w')
file.write('curl -O ')
file.write(link)
file.close()
subprocess.call('download.bat')
os.remove('download.bat')