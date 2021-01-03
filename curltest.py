import os
import subprocess
import requests
wd = (os.getcwd())
link = (input('输入链接'))
r=requests.head(link)
#文件大小
filesize=r.headers['Content-Length']
downloadbat = wd+'/download.bat'
file = open(downloadbat,'w')
file.write('curl -O ')
file.write(link)
file.close()
subprocess.call('download.bat')
os.remove('download.bat')