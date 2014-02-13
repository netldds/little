#python3
import urllib.request, urllib.error,bs4
url="http://www.baidu.com/s?ie=UTF-8&wd=ip"

def get():
    html=urllib.request.urlopen(url).read()
    soup=bs4.BeautifulSoup(html)
    IP=soup.find("div",{"id":"1"})["fk"]
    return IP
if __name__=="__main__":
    print(get())