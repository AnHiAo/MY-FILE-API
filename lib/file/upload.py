import requests
import os,sys
def my_callback(monitor):
    print(monitor.bytes_read)
import json
from urllib3 import disable_warnings
from re import I as reI,search as reSearch
from os.path import (
    exists as osExists,
    getsize as getFileSize
)
from urllib.parse import quote
disable_warnings()   # cancel requests warnings...


class upload_in_chunks(object):
    def __init__(self, filename, chunksize=1 << 13):
        self.filename = filename
        self.chunksize = chunksize
        self.totalsize = os.path.getsize(filename)
        self.readsofar = 0

    def __iter__(self):
        with open(self.filename, 'rb') as file:
            while True:
                data = file.read(self.chunksize)
                if not data:
                    sys.stderr.write("\n")
                    break
                self.readsofar += len(data)
                percent = self.readsofar * 1e2 / self.totalsize
                sys.stderr.write("\r灌满(上传)进度： {percent:3.0f}%".format(percent=percent))
                yield data

    def __len__(self):
        return self.totalsize

def uploadFile(userinfo,globalData):
    filePath =  userinfo[0]
    userCookie =  globalData['userCookie']
    fileName = reSearch(r'[\w\.]+$',filePath,reI)
    if not osExists (filePath):
        print("file is  not found")
        return globalData
    fileName = fileName.group(0)
    fileSize = getFileSize(filePath)
    res = requests.get((f'https://my-file.cn/api/v3/file/upload/credential?path={globalData["currentPath"]}&size={fileSize}&name={fileName}&type=onedrive'),headers={
    "Cookie": "cloudreve-session=MTYzMTI4NjM0M3xOd3dBTkZoVFZ6TmFXVE5LUTFCUk5FUllSMVUwV2toWk5rZEpXamRIVURkV05WYzJORUZPU0VOV1JWSllWVmxNUjFCTVZGcFJRa0U9fDcaN0aUb_YQ4DOXMqNANpssqhCvFVrtIxTDNpxJj3UU; path_tmp=%E4%B8%B4%E6%97%B6%E5%A4%87%E4%BB%BD"
    },verify=False)
    print(f"文件名: {fileName}  状态:申请文件占位成功\n")

    class IterableToFileAdapter(object):
        def __init__(self, iterable):
            self.iterator = iter(iterable)
            self.length = len(iterable)

        def read(self, size=-1):  # TBD: add buffer for `len(data) > size` case
            return next(self.iterator, b'')

        def __len__(self):
            return self.length

    if not len(res.json()['data']['policy']):
        # 这里就是针对小文件上传 大概分割线的标准是4MB
        it = upload_in_chunks(fileName, 2097152)  # 2 * 1024 * 1024
        res = requests.post(
            "https://my-file.cn/api/v3/file/upload?chunk=0&chunks=1",
            data=IterableToFileAdapter(it),
            # open(fileName,"rb").read(),
            headers={
                "x-filename": quote(fileName),
                "x-path": quote(globalData["currentPath"]),
                "content-type": "application/octet-stream",
                "Cookie": userCookie
            }, verify=False)
        print(res.text)
        # lastData = json.dumps(res.json())
        if res:
            print(f"文件名: {fileName}  状态:成功")
        return globalData
    finishCallBack = res.json()['data']['token']
    it = upload_in_chunks(fileName,2097152) # 2 * 1024 * 1024
    res = requests.put(
        res.json()['data']['policy'],
        data=IterableToFileAdapter(it),
        # open(fileName,"rb").read(),
        headers={
            "content-type": "application/octet-stream",
            "content-range":f"bytes 0-{fileSize-1}/{fileSize}",
         "Cookie": userCookie
        },verify=False)
    lastData = json.dumps(res.json())
    res  = requests.post(finishCallBack,headers={
    "Host": "my-file.cn",
    "Connection": "keep-alive",
    "sec-ch-ua": '''Google Chrome';v="93", " Not;A Brand";v="99", "Chromium";v="93"''',
    "sec-ch-ua-mobile": "?0",
    "User-Agent":'''Mozilla"/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36''',
    "Content-Type": "text/plain;charset=UTF-8",
    "Origin": "https://my-file.cn",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode":"cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": userCookie

    },verify=False,data=lastData)
    if res:
        print(f"文件名: {fileName}  状态:成功")
    return globalData
# 这个地方应该本身需要做两种 第一种就是针对小文件的传输 第二种就是针对大文件采用流上传
# uploadFile("QQbotPresenter1221.7z")