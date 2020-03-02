import requests
from bs4 import BeautifulSoup

#自己的账号密码 
#0开头的要用字符串 '*****'
username=******
password=******


userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
logUrl = "http://yiqing.ctgu.edu.cn/wx/index/loginSubmit.do"


header={
    #origin:http://yiqing.ctgu.edu.cn
    # "Content-Type": "application/json;charset=UTF-8",
    'Referer':"http://yiqing.ctgu.edu.cn/wx/index/login.do?currSchool=ctgu&CURRENT_YEAR=2019",
    'User-Agent':userAgent
}

yiqingSession = requests.session()

postData={
    "username":username,
    "password":password
}

# ****************登录*******************

responseRes = yiqingSession.post(logUrl,data = postData, headers = header)

# *******从提交页面获取 表单信息**********

getFormurl =  "http://yiqing.ctgu.edu.cn/wx/health/toApply.do"

responseRes = yiqingSession.get(getFormurl)

formHtml = responseRes.text

supe = BeautifulSoup(formHtml,"html.parser")

getFormlist = supe.find_all('input')

#构建表单（当然 默认身体健康）

postData={
    "ttoken":  '',
    "province":  "",
    "city":      "",
    "district":  "",
    "adcode":    "",
    "longitude": "0",
    "latitude":  "0",
    "sfqz": "否",
    "sfys": "否",
    "sfzy": "否",
    "sfgl": "否",
    "status": "1",
    "sfgr": "否",
    "szdz": "",
    "sjh": "",
    "lxrxm": '',
    "lxrsjh": '',
    "sffr": "否",
    "sffy":"否",
    "sfgr": "否",
    "qzglsj": '',
    "qzgldd": '',
    "glyy": '',
    "mqzz": '',
    "sffx": "否",
    "qt":"",
}

#从提交页面获取表单信息

getFormlist=getFormlist[0:15]

for Formdata in getFormlist :
    postData[Formdata.attrs['name']] = Formdata.attrs['value']


#*************提交最终表单***********

postFormurl = "http://yiqing.ctgu.edu.cn/wx/health/saveApply.do"


header['Referer'] = "http://yiqing.ctgu.edu.cn/wx/health/toApply.do"


responseRes=yiqingSession.post(postFormurl,data=postData,headers=header)

print(responseRes.text)
















