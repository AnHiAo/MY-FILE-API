from requests import delete as reqDelete
from json import dumps as jsonDumps
from lib.folder.getDirectory import getDirData
def rmDir(userinfo,globalData):
    # userinfo[0]
    removeFolderId = ""
    for i in globalData['currentDirectoryData']:
        if i[2] == userinfo[0] and i[0] == "dir":
            removeFolderId = i[3]
            break
    if not len(removeFolderId):
        print("未找到该文件夹名字,请检查文件夹名字")
        return globalData
    res = reqDelete("https://my-file.cn/api/v3/object",data=jsonDumps({
        "dirs":[removeFolderId],
        "items":[]
    }),headers={
         "content - type": "application / json;charset = UTF - 8",
        "Cookie":globalData['userCookie']
    })
    print(res.text)
    if res:
        print("删除成功")
    return getDirData(["",globalData['currentPath']],globalData)
