from re import (
    I as reI,
    search as reSearch,
findall
)
from lib.user.login import login
import os
from lib.folder.getDirectory import  getDir
from lib.folder.enterDirectory import  enterDir
from lib.folder.makeDirectory import makeDir
from lib.folder.removeDirectory import rmDir
from lib.file.upload import uploadFile
from lib.file.delete import deleteFile
globalData = {}
orders = {
    "rmdir":rmDir,
    "mkdir":makeDir,
    "del":deleteFile,
    "up":uploadFile,
    "getData":lambda  x,y:print(globalData),
    "clear":lambda  x,y:os.system("cls"),
    "cls":lambda  x,y:os.system("cls"),
    "exit":lambda x,y: os._exit(0),
    "cd":enterDir,
    "ls":getDir,
    "login":login
    }
def getGlobalData(test,testdata):
        print(globalData)
        return globalData
def main(order,data):
    global globalData
    # data
    globalData = data
    orders['getData'] = getGlobalData
    matchWordsList = (findall(r'[^\s]+', order, reI))
    nowData = orders
    for i in range(len(matchWordsList)):
        if type(nowData) != dict:
            break
        if matchWordsList[i] in nowData.keys():
            nowData = nowData[matchWordsList[i]]
    if(type(nowData) == dict):
        print("not found , try again ")
        return globalData
    return nowData(matchWordsList[i:],globalData)
