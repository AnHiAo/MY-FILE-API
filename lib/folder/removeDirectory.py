from requests import delete as reqDelete
from json import dumps as jsonDumps
def rmDir(userinfo,globalData):
    userinfo[0]
    removeFolderId = ""
    for i in globalData['currentDirectoryData']:
        if i[2] == userinfo[0]:
            removeFolderId = i[3]
            break
    print(removeFolderId)
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
    return globalData