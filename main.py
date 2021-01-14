import os
import subprocess
import requests
wd = (os.getcwd())
link = (input('输入链接'))
Header = input('自定义header,不知道不用填写')
r=requests.head(link)
#文件大小
filesize=r.headers['Content-Length']
block = (filesize / 5)
#第一个bat
downloadbat = wd+'/download.bat'
file = open(downloadbat,'w')
file.write('curl -O ')
if Header == '':
    pass
else:
    file.write('-H ')
    file.write(Header)
    pass
file.write(link)
file.close()
subprocess.call('download.bat')
os.remove('download.bat')