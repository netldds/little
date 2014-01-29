# -*- coding: cp936 -*-
'''
author:郎芭
QQ：149737748
'''
import os,urllib2,time,sys,re
import thread
from bs4 import BeautifulSoup
start_time=time.clock()
za='<div.*</div>'
a=thread.allocate()#多线程用的锁
a.acquire()  #设置第二部份锁为阻塞
b=thread.allocate()
b.acquire()#第三部分
c=thread.allocate()
c.acquire()#第四部分
d=thread.allocate()
d.acquire()


def runa(qi,zhi,wurl,x,y):
    result=''
    soup=bsp(wurl)
    lzname=soup.find('div',{'class':'atl-menu clearfix js-bbs-act'})['js_activityusername']
    for i in xrange(int(qi),int(zhi)+1):
        newurl='http://bbs.tianya.cn/post-%s-%s-%s.shtml'%(x,y,i)
        txt=pagecollect(newurl,lzname)
        if txt:print u'The page %s  is completed!\r'%i,
        else:  print u'The page %s  is None!     \r'%i,
        result +=txt
    #优先写入第一部分内容，再解锁第二部分阻塞！    
    writf(result,title)
    a.release()#解锁

def runb(qi,zhi,wurl,x,y):
    result=''
    soup=bsp(wurl)
    lzname=soup.find('div',{'class':'atl-menu clearfix js-bbs-act'})['js_activityusername']
    for i in xrange(int(qi),int(zhi)+1):
        newurl='http://bbs.tianya.cn/post-%s-%s-%s.shtml'%(x,y,i)
        txt=pagecollect(newurl,lzname)
        if txt:print u'The page %s  is completed!\r'%i,
        else:  print u'The page %s  is None!     \r'%i,
        result +=txt
    a.acquire()#状态为阻塞，不能执行下一步，等待上步完成后解锁！
    writf(result,title)
    b.release()

def runc(qi,zhi,wurl,x,y):
    result=''
    soup=bsp(wurl)
    lzname=soup.find('div',{'class':'atl-menu clearfix js-bbs-act'})['js_activityusername']
    for i in xrange(int(qi),int(zhi)+1):
        newurl='http://bbs.tianya.cn/post-%s-%s-%s.shtml'%(x,y,i)
        txt=pagecollect(newurl,lzname)
        if txt:print u'The page %s  is completed!\r'%i,
        else:  print u'The page %s  is None!     \r'%i,
        result +=txt
    b.acquire()#状态为阻塞，不能执行下一步，等待上步完成后解锁！
    writf(result,title)
    c.release()

def rund(qi,zhi,wurl,x,y):
    result=''
    soup=bsp(wurl)
    lzname=soup.find('div',{'class':'atl-menu clearfix js-bbs-act'})['js_activityusername']
    for i in xrange(int(qi),int(zhi)+1):
        newurl='http://bbs.tianya.cn/post-%s-%s-%s.shtml'%(x,y,i)
        txt=pagecollect(newurl,lzname)
        if txt:print u'The page %s  is completed!\r'%i,
        else:  print u'The page %s  is None!     \r'%i,
        result +=txt
    c.acquire()#状态为阻塞，不能执行下一步，等待上步完成后解锁！
    writf(result,title)
    d.release()

def writf(result,title):#写入文件
    dirs=os.getcwd()
    fname='%s.txt'%(title)
    ff=open(fname,'a')
    ff.write(result)
    ff.close()
        
def pagecollect(url,lzname): #获得当前页内容
    soup=bsp(url)
    txt=[]
    lzpost=soup.findAll('div',{'_host':lzname})
    for i in xrange(len(lzpost)):
        post=lzpost[i].find('div',{'class':'atl-content'}).text.encode('utf-8')
        txt.append(re.sub(za,'',post))
    return ''.join(txt)


def bsp(url):
    turl=urllib2.urlopen(url,timeout=10).read()
    rsp=BeautifulSoup(turl)
    return rsp

def pagenum(wurl):#获得URL数字位1，2，3和总页数
    soup=bsp(wurl)
    surl=wurl.split('-')
    z=re.search('(\d+)',surl[3]).group(0)
    fom=soup.find('form',{'action':'','method':'get'})['onsubmit'].split(',')
    zong=re.search('(\d+)',fom[3]).group(0)
    return surl[1],surl[2],z,zong

if __name__=='__main__':
    wurl=raw_input('>>')
    x,y,z,zong=pagenum(wurl)
    soup=bsp(wurl)
    title=re.sub('_.*','',soup.title.text)
    print title
    print x,'-',y,'-',z,'Pages:',zong
    z=int(z)
    if int(zong)-z>=12:  #判断页数大于等于12页则用多线程
        fen=(int(zong)-z)/4
        fen=int(fen)
        thread.start_new_thread(runa,(z,z+1*fen,wurl,x,y))
        thread.start_new_thread(runb,(z+1*fen+1,z+2*fen,wurl,x,y))
        thread.start_new_thread(runc,(z+2*fen+1,z+3*fen,wurl,x,y))
        thread.start_new_thread(rund,(z+3*fen+1,zong,wurl,x,y))
    else:
        runa(z,zong,wurl,x,y)
    d.acquire()
    print 'Used %.2fs           '%(time.clock()-start_time)
