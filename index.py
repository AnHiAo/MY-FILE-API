import requests
import os,sys
from requests_toolbelt import MultipartEncoder,MultipartEncoderMonitor
def my_callback(monitor):
    print(monitor.bytes_read)
import pyperclip
from urllib import  parse
import json
import urllib3
from urllib3 import disable_warnings
from re import I as reI,search as reSearch
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
                sys.stderr.write("\r{percent:3.0f}%".format(percent=percent))
                yield data

    def __len__(self):
        return self.totalsize



from os.path import (
    exists as osExists,
    getsize as getFileSize
)
def uploadFile(filePath):
    fileName = reSearch(r'[\w\.]+$',filePath,reI)
    if not osExists (filePath):
        return "file is  not found"
    fileName = fileName.group(0)
    fileSize = getFileSize(filePath)
    print(fileName)
    res = requests.get((f'https://my-file.cn/api/v3/file/upload/credential?path=%2F临时备份&size={fileSize}&name={fileName}&type=onedrive'),headers={
    "Cookie": "cloudreve-session=MTYzMTI4NjM0M3xOd3dBTkZoVFZ6TmFXVE5LUTFCUk5FUllSMVUwV2toWk5rZEpXamRIVURkV05WYzJORUZPU0VOV1JWSllWVmxNUjFCTVZGcFJRa0U9fDcaN0aUb_YQ4DOXMqNANpssqhCvFVrtIxTDNpxJj3UU; path_tmp=%E4%B8%B4%E6%97%B6%E5%A4%87%E4%BB%BD"
    },verify=False)
    print(res.text)

    class IterableToFileAdapter(object):
        def __init__(self, iterable):
            self.iterator = iter(iterable)
            self.length = len(iterable)

        def read(self, size=-1):  # TBD: add buffer for `len(data) > size` case
            return next(self.iterator, b'')

        def __len__(self):
            return self.length

    finishCallBack = res.json()['data']['token']
    it = upload_in_chunks(fileName,10)
    res = requests.put(res.json()['data']['policy'],
                       data=IterableToFileAdapter(it),
                       # open(fileName,"rb").read(),
                       headers={
                           "content-type": "application/octet-stream",
                           "content-range":f"bytes 0-{fileSize-1}/{fileSize}",
    "Cookie": "cloudreve-session=cloudreve-session=MTYzMTI4NzQxMXxOd3dBTkZoVFZ6TmFXVE5LUTFCUk5FUllSMVUwV2toWk5rZEpXamRIVURkV05WYzJORUZPU0VOV1JWSllWVmxNUjFCTVZGcFJRa0U9fPd4sRuM_Uqgbyoj6-LoRbUQs7aRHZzmgyoZCd9gjnDh"
                       },verify=False)
    lastData = json.dumps(res.json())
    print(res.json())
    pyperclip.copy(lastData)
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
    "Referer": "https://my-file.cn/home?path=%2F%E4%B8%B4%E6%97%B6%E5%A4%87%E4%BB%BD",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "path_tmp=%E4%B8%B4%E6%97%B6%E5%A4%87%E4%BB%BD; cloudreve-session=MTYzMTI4NzQxMXxOd3dBTkZoVFZ6TmFXVE5LUTFCUk5FUllSMVUwV2toWk5rZEpXamRIVURkV05WYzJORUZPU0VOV1JWSllWVmxNUjFCTVZGcFJRa0U9fPd4sRuM_Uqgbyoj6-LoRbUQs7aRHZzmgyoZCd9gjnDh"

    },verify=False,data=lastData)
    print((res.text))
if __name__ == "__main__":
    uploadFile("QQbotPresenter1221.7z")