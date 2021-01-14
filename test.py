import os
import subprocess
import requests
wd = (os.getcwd())
link = (input('输入链接'))
Header = input('自定义header,不知道不用填写')
r=requests.head(link)
#文件大小
filesize=int(r.headers['Content-Length'])
block = (filesize / 5)
print (block)