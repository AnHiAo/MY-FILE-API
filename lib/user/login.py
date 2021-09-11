from requests import post as reqPost
from json import dumps as jsonDumps
from urllib3 import disable_warnings
disable_warnings()
loginReq = reqPost(
    "https://my-file.cn/api/v3/user/session",
    headers={
        "Content-type":"application/json;charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
    },
    data=jsonDumps({
        "Password":"yzh20030508",
        "captchaCode":"",
        "userName":"15112519004@163.com"
    })     ,verify=False      )
print(loginReq.headers.get('set-cookie'))