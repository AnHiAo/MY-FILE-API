from re import (
    I as reI,
    search as reSearch,
findall
)
from os import system as osSys,_exit as os_exit,listdir as osListdir,getcwd as osGetcwd
from lib.user.login import login
from lib.folder.getDirectory import  getDir
from lib.folder.enterDirectory import  enterDir
from lib.folder.makeDirectory import makeDir
from lib.folder.removeDirectory import rmDir
from lib.file.upload import uploadFile
from lib.file.delete import deleteFile
from lib.file.download import downloadFile


globalData = {}
def systemOperation(method,params):
    global globalData
    method(params)
    return globalData
orders = {
    "rmdir":rmDir,
    "mkdir":makeDir,
    "del":deleteFile,
    "download":downloadFile,
    "up":uploadFile,
    "getData":lambda x,y:systemOperation(print,globalData),
    "clear": lambda  x,y:systemOperation(osSys,"cls"),
    "cls":lambda x,y:systemOperation(osSys,"cls"),
    "exit":lambda x,y:systemOperation(os_exit,0),
    "dir":lambda x,y:systemOperation(print,"\n".join(osListdir( osGetcwd()))),
    "cd":enterDir,
    "ls":getDir,
    "login":login
    }
def getGlobalData(test,testdata):
        print(globalData)
        return globalData
def main(order,data):
    global globalData
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
