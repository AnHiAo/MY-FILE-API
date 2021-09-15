from requests import put as reqPut
from json import dumps as jsonDumps
def makeDir(userinfo,globalData):
    newFolderPath = userinfo[0]
    if not userinfo[0].startswith("/"):
        # 则是直接加上当前路径定位
        newFolderPath = globalData['currentPath'] +"/"+userinfo[0]
        if globalData['currentPath'] == "/":
            newFolderPath = globalData['currentPath'] +userinfo[0]
    res = reqPut("https://my-file.cn/api/v3/directory",data=jsonDumps({
        "path":newFolderPath
    }),headers={
        "content - type": "application / json;charset = UTF - 8",
        "Cookie":globalData['userCookie']
    })
    print("创建文件夹成功")
    return globalData