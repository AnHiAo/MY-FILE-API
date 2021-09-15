# 'https://my-file.cn/api/v3/directory%2F'
from urllib3 import disable_warnings
from requests import get as reqGet
from urllib.parse import quote
def getDirData(userinfo,globalData):
    if ("userCookie" in globalData.keys() and len(globalData['userCookie'])):
        outputStrList = [];
        if len(userinfo) == 1:  # 查询当前用户所在的目录
            userinfo.append(globalData['currentPath'])
        res = reqGet(
            (f"https://my-file.cn/api/v3/directory{userinfo[1]}"),
            headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
                "Cookie": globalData['userCookie']
            },
            verify=False
        )
        if res:
            for i in res.json()['data']['objects']:
                outputStrList.append([i['type'],i['date'],i['name'],i['id']])
                # outputStrList.append(f' ( {i["type"]} )    {i["date"]}{" "*4}{i["name"]}')
        globalData['currentDirectoryData'] = outputStrList
        return globalData



    # 以下是后期可以获取指定目录
def getDir(userinfo,globalData):
    if ("userCookie" in globalData.keys() and len(globalData['userCookie'])):
        outputStrList = [];
        if len(userinfo) ==  1: # 查询当前用户所在的目录
            userinfo.append(globalData['currentPath'])
        res = reqGet(
        (f"https://my-file.cn/api/v3/directory{userinfo[1]}"),
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
            "Cookie": globalData['userCookie']
        },
             verify=False
         )
        if res:
            for i in res.json()['data']['objects']:
                outputStrList.append(f' ( {i["type"]} )    {i["date"]}{" "*4}{i["name"]}')
        print("\n".join(outputStrList))
        return globalData