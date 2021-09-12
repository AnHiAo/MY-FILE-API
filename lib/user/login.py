from requests import post as reqPost
from json import dumps as jsonDumps
from urllib3 import disable_warnings
from lib.folder.getDirectory import  getDirData
from lib.folder.enterDirectory import  enterDir
disable_warnings()
def login(userinfo,globalData):
    if len(userinfo) < 2:
        print("你输入的账号密码不全,请按照以下重新输入...\n")
        userinfo = [input("请输入你的账号 :"),input("请输入你的密码 :")]
    username = userinfo[0]
    password = userinfo[1]
    loginReq = reqPost(
    "https://my-file.cn/api/v3/user/session",
    headers={
        "Content-type":"application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    },
    data=jsonDumps({
        "Password":password,
        "captchaCode":"",
        "userName":username
    })     ,verify=False      )
    if(len(loginReq.text)):
        resJson = loginReq.json()
        if int(resJson['code']) != 0:
            print(resJson['msg'])
            return globalData
        print("login successful !")
        globalData['userCookie'] = loginReq.headers.get('set-cookie')
        globalData['userName'] = loginReq.json()['data']['user_name']
        globalData['currentPath'] = '/'
        # return globalData
        return getDirData(["ls"],globalData)
