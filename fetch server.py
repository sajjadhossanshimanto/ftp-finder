import requests 
import re 
import json


url="https://sites.google.com/view/bdixftpserverlist/live-tv-servers"
blocklist = "blocklist_tv-server.txt"

url="https://sites.google.com/view/bdixftpserverlist/media-ftp-servers"
blocklist = "blocklist_media.txt"


with open(blocklist) as f:
    # block = f.read()
    block = set(map(lambda x:x[:-1], f.readlines()))
# print("http://www.bnet-bd.com" in block)


def save_web_html(url, filename):
  r = requests.get(url)
  with open(filename, "w", encoding="utf-8") as f:
    f.write(r.text)

fs = open("active_server.txt", "a", encoding="utf-8")
def check_server(url):
    try:
        r = requests.get(url, timeout=3)
    except requests.exceptions.Timeout:
        return 

    #print(r.status_code)
    if r.status_code==200:
        if "facebook" in url or url in block: return 
        
        # data saving part
        fs.write(f"\n{url}")
        fs.flush()
        print()# to fix raw line

file = "ftp_server.html"
save_web_html(url, file)
with open(file, encoding="utf-8") as f:
    html = f.read()

# p=len(html)
pattern = '<div class="NsaAfc"><p>(.+?)</p>'
c=0
for link in re.finditer(pattern, html):
    c+=1
    print(".    ", c, p, end="\r")
    p=link.group(1)
    check_server(p)
    
    # break

f.close()
