'''
manufally see all webs one by one and filter them by needs
'''
import webbrowser as wb


# TV server 
l=["http://103.136.200.246", "http://amrbd.com", "http://otv.ftpbd.net", "http://bdiptv.stream", "http://tv.roarzone.info", "http://103.102.27.172", "http://113.212.111.246", "http://tv.mtbsl.com", "http://livetv.mirpur.online", "http://103.150.6.2", "https://tv.livebdix.com", "https://iptv.race.net.bd", "https://iptv.jadoodigital.com", "https://www.bioscopelive.com", "http://www.jagobd.com", "https://beta.jagobd.com", "https://bongobd.com", "http://tv.bdixsports.com", "http://durbinlive.com", "http://globalbanglatv.com", "https://www.webtvbd.com"]

f="active_server.txt"
with open(f) as f:
    l = f.readlines()


skip_line = 0# TODO: very careful
c = 0
for i in l:
    c+=1
    if c<=skip_line: continue 
    # add filters
    if "facebook" in i: continue 
    
    wb.open(i)
    inp = input(f".    {i} -- press any key .....")
    if inp==".":
        with open("filtered.txt", "a") as f:
            f.write(i+"\n")

