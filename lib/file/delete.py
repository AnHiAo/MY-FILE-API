from requests import delete as reqDelete
from json import dumps as jsonDumps
from lib.folder.getDirectory import getDirData
def deleteFile(userinfo,globalData):
    removeFileId = ""
    for i in globalData['currentDirectoryData']:
        if i[2] == userinfo[0] and i[0] == "file":
            removeFileId = i[3]
            break
    if not len(removeFileId):
        print("未找到该文件名字,请检查文件名字")
        return globalData
    res = reqDelete(
        "https://my-file.cn/api/v3/object",
       headers={
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": globalData['userCookie'],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
       } ,
        data=jsonDumps({
            "dirs":[],
            "items":[removeFileId]
        }),verify=False)
    if res:
        print("文件删除成功")
    else:
        print("文件删除失败  :" + res.text)
    return getDirData(["",globalData['currentPath']],globalData)
