from re import search as reSearch
def enterDir(userinfo,globalData):
    # cd abcd / asdlfjk;asdf /asdfsdfj; /
    # currentDirectory
    # 首先验证是否为目录
     # order params

    # 暂时只能进当前同等级目录
    if reSearch(r'^(\.\./|\.\.)$',userinfo[0]) != None:
        replaceText = reSearch(r'((?<=^\/)[^\/]+$)|(?<=.\/)[^\/]+$',globalData['currentPath'])
        globalData['currentPath'] = globalData['currentPath'].replace(replaceText.group(0),"")
        return  globalData
    isFIndFolder = False
    for file in globalData['currentDirectoryData']:
        if file[2] == userinfo[0] and file[0] == "dir":
            isFIndFolder = True
            break
    if(not isFIndFolder):
        print("该名下不是目录请稍后尝试")
        return globalData
    globalData['currentPath'] = "/" + userinfo[0].replace("./","")
    return globalData
