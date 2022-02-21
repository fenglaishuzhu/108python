import webbrowser
import time

urls = (
    'https://xue.cn/',
    'https://baidu.com/',
    'https://zhihu.com/')

for url in urls:
    webbrowser.open(url)
    time.sleep(1)

print("All is done.")
