# -*- coding: cp936 -*-
'''
author:�ɰ�
QQ��149737748
'''
import os,urllib2,time,sys,re
import thread
from bs4 import BeautifulSoup
start_time=time.clock()
za='<div.*</div>'
a=thread.allocate()#���߳��õ���
a.acquire()  #���õڶ�������Ϊ����
b=thread.allocate()
b.acquire()#��������
c=thread.allocate()
c.acquire()#���Ĳ���
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
    #����д���һ�������ݣ��ٽ����ڶ�����������    
    writf(result,title)
    a.release()#����

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
    a.acquire()#״̬Ϊ����������ִ����һ�����ȴ��ϲ���ɺ������
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
    b.acquire()#״̬Ϊ����������ִ����һ�����ȴ��ϲ���ɺ������
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
    c.acquire()#״̬Ϊ����������ִ����һ�����ȴ��ϲ���ɺ������
    writf(result,title)
    d.release()

def writf(result,title):#д���ļ�
    dirs=os.getcwd()
    fname='%s.txt'%(title)
    ff=open(fname,'a')
    ff.write(result)
    ff.close()
        
def pagecollect(url,lzname): #��õ�ǰҳ����
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

def pagenum(wurl):#���URL����λ1��2��3����ҳ��
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
    if int(zong)-z>=12:  #�ж�ҳ�����ڵ���12ҳ���ö��߳�
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
