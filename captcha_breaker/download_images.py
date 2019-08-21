import os
import requests
import time
from bs4 import BeautifulSoup

# url = "https://www.e-ezpassny.com/vector/jcaptcha.do"
url ="https://www.ezpassnj.com/vector/jcaptcha.do"
total =0

for i in range(0, 1):
    try:
        r = requests.get(url, timeout=60)
        page_content = BeautifulSoup(r.content, "html.parser")
        p = os.path.sep.join(["downloads", "{}.jpg".format(str(total).zfill(5))])
        f = open(p,"wb")
        f.write(r.content)
        f.close()
        

        print("Downloaded: {}".format(p))
        total+=1

    except:
        print("Error on downloading the image")

    time.sleep(0.1)


