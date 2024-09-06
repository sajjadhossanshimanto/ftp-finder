import requests 
import re 
import json


url="https://sites.google.com/view/bdixftpserverlist/live-tv-servers"
url="https://sites.google.com/view/bdixftpserverlist/media-ftp-servers"

def save_web_html(url, filename):
  r = requests.get(url)
  with open(filename, "w") as f:
    f.write(r.text)

l=[]
fs = open("active_server.txt", "a")
def check_server(url):
    try:
        r = requests.get(url, timeout=3)
    except requests.exceptions.Timeout:
        return 
    except requests.exceptions.ConnectionError:
        return
    #print(r.status_code)
    if r.status_code==200:
        if "facebook" in i: return 
        
        # data saving part
        fs.write(f"\n{url}")
        fs.flush()
        l.append(url)
        print()# to fix raw line

file = "ftp_server.html"
#save_web_html(url, file)
with open(file) as f:
    html = f.read()

# p=len(html)
pattern = '<div class="NsaAfc"><p>(.+?)</p>'
c=0
for link in re.finditer(pattern, html):
    p=link.group(1)
    check_server(p)
    c+=1
    print(".    ", c, p, end="\r")
#    break

f.close()
#with open("active_server.txt", "w") as f:
#    json.dump(l, f)
 

