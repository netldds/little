#coding:utf8
'''
	www.pubyun.con动态域名IP更新脚本
	DATE：2014.2.4
	#规范版本

'''
import base64,urllib,urllib2,httplib
class update():
    def __init__(self):
    	try:
    		self.Yusername=raw_input("account:")					#帐号
        	self.Ypassword=raw_input("password:")				#密码
        except:
        	print "IOError(error)"
        self.b64=base64.encodestring(("%s:%s"%(self.Yusername,self.Ypassword)))
        self.Author="Basic %s"%self.b64 				#BASE64编码为Authorization格式	
        print 'Authorization:',self.Author 		#为了处理Authorization
        # =================
        self.hostname='netldds.3322.org'
        try:
            import GETIP
            self.myip=GETIP.get()
        except:
            print "Please import GETIP.py"
            self.myip=None
        self.wildcard='ON' 						#ON为支持泛域名，可选
        self.mx=''								#指明 Mail eXchanger解析到一个IP，可选
        self.backmx='YES'						#致命前面的MX参数会被设置成备份邮件服务器。可选
        self.offline='YES'						#使域名暂时失效

        self.url='/dyndns/update?'				#为HTTPlib预留
        self.uurl='http://members.3322.net/dyndns/update?'
        #用urllib2的URL

        self.Ypo={'hostname':self.hostname,'wildcard':self.wildcard,"myip":self.myip}
        #http://www.pubyun.com/wiki/%E5%B8%AE%E5%8A%A9:api
        self.head={'Host': 'members.3322.net','Authorization': self.Author,'User-Agent': 'PythonUpdateTool@netldds'}
        #这里的header最重要 			#Authorization需要BASE64编码看上面
        self.encodeurl()

    def encodeurl(self):
        self.po=urllib.urlencode(self.Ypo)
        self.uurl+=self.po
        print "URL:",self.uurl
    def post(self):
        RE=urllib2.Request(self.uurl,None,self.head)
        print 'Request\'s Headers:',RE.headers
        Res=urllib2.urlopen(RE)
        print Res.read()
if __name__=="__main__":
    ug=update()
    ug.post()
    
        