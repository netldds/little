#coding:utf8
'''
	www.pubyun.con动态域名IP更新脚本
	DATE：2014.1.27

'''
import base64,urllib,urllib2,httplib
Yusername='netldds'					#帐号
Ypassword='zhangliu110'				#密码
b64=base64.encodestring(("%s:%s"%(Yusername,Ypassword)))
Author="Basic %s"%b64 				#BASE64编码为Authorization格式	
print 'Authorization:',Author 		#为了处理Authorization
									# =================
hostname='netldds.3322.org'
myip=''								#空为默认当前IP，可选
wildcard='ON' 						#ON为支持泛域名，可选
mx=''								#指明 Mail eXchanger解析到一个IP，可选
backmx='YES'						#致命前面的MX参数会被设置成备份邮件服务器。可选
offline='YES'						#使域名暂时失效

url='/dyndns/update?'				#为HTTPlib预留
uurl='http://members.3322.net/dyndns/update?'
									#用urllib2的URL

Ypo={'hostname':hostname,'wildcard':wildcard}
									#http://www.pubyun.com/wiki/%E5%B8%AE%E5%8A%A9:api
head={'Host': 'members.3322.net',	#这里的header最重要
'Authorization': Author,			#Authorization需要BASE64编码看上面
'User-Agent': 'PythonUpdateTool@netldds'}
									#这里是写软件信息的，自己弄。

po=urllib.urlencode(Ypo)
uurl+=po
print 'URL:',uurl

# HTTPlib方式预留
# conn=httplib.HTTPConnection('members.3322.net')
# conn.request("GET",url,'',head)
# print head
# httpres=conn.getresponse()
# print httpres.read()
# conn.close()


RE=urllib2.Request(uurl,None,head)
print 'Request\'s Headers:',RE.headers
Res=urllib2.urlopen(RE)
print Res.read()


