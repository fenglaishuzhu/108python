import webbrowser
import time

for i in range(5, 10):
    url = "https://xue.cn/hub/app/books/" + str(i)
    webbrowser.open(url)
    time.sleep(1)

print("All is done")
