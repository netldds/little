import urllib2,bs4
url="http://www.baidu.com/s?ie=UTF-8&wd=ip"

def get():
    html=urllib2.urlopen(url).read()
    soup=bs4.BeautifulSoup(html)
    IP=soup.find("div",{"id":"1"})["fk"]
    return IP
if __name__=="__main__":
    print get()