from re import (
    I as reI,
    search as reSearch,
findall
)

from lib.user.login import login

def todo(data):
    print("todo")
    print(data)
def main(order,data):
    if data == None:
        data = {}
    globalData = dict(data)
    def getGlobalData(test,testdata):
        print(globalData)
    data = {
        "getData":getGlobalData,
        "git":{
            "pull":{
                "origin":"god"
            },
            "todo":todo
        },
        "login":login
    }
    matchWordsList = (findall(r'[^\s]+', order, reI))
    nowData = data
    for i in range(len(matchWordsList)):
        if type(nowData) != dict:
            break
        if matchWordsList[i] in nowData.keys():
            nowData = nowData[matchWordsList[i]]
    if(type(nowData) == dict):
        return print("not found , try again ")
    return nowData(matchWordsList[i:],globalData)
