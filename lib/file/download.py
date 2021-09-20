import re
from requests import put as reqPut , get as reqGet
from json import dumps as jsonDumps
from lib.folder.getDirectory import getDirData
def calc_divisional_range(filesize, chuck=10):
    step = filesize//chuck
    arr = list(range(0, filesize, step))
    result = []
    for i in range(len(arr)-1):
        s_pos, e_pos = arr[i], arr[i+1]-1
        result.append([s_pos, e_pos])
        result[-1][-1] = filesize-1
    return result
def range_download(url,save_name, s_pos, e_pos):
    headers = {
    "Range": f"bytes={ s_pos}-{ e_pos}"}
    res =reqGet(url, headers=headers, stream=True)
    f  = open(save_name, "rb+")
    f.seek(s_pos)
    for chunk in res.iter_content(chunk_size=64*1024):
        if chunk:
            f.write(chunk)
    f.close()

def downloadFile(userinfo,globalData):
    print(userinfo)
    downloadFileId = ""
    for i in globalData['currentDirectoryData']:
        if i[2] == userinfo[0] and i[0] == "file":
            downloadFileId = i[3]
            break
    if not len(downloadFileId):
        print("未找到该文件名字,请检查文件名字")
        return globalData
    res = reqPut(
        f"https://my-file.cn/api/v3/file/download/{downloadFileId}",
       headers={
    "Content-Type": "application/json;charset=UTF-8",
    "Cookie": globalData['userCookie'],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
       } ,
       verify=False)
    if res:
        print(res.json())
        url = str(res.json()['data'])
        save_name = re.search(r'[^\/]+$',userinfo[0]).group(0)
        f = open(save_name, "wb")
        f.close()
        res = reqGet(res.json()['data'], headers={
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"})
        print(res.headers)
        divisional_ranges = calc_divisional_range(int(res.headers["Content-Length"]))
        from concurrent.futures import ThreadPoolExecutor, as_completed
        with ThreadPoolExecutor() as p:
            futures = []
            for s_pos, e_pos in divisional_ranges:
                print(s_pos, e_pos)
                futures.append(p.submit(range_download, url, save_name, s_pos, e_pos))
                as_completed(futures)
            for future in as_completed(futures):
                data = future.result()
                print(f"完成任务")
    else:
        print("文件删除失败  :" + res.text)
    return getDirData(["",globalData['currentPath']],globalData)