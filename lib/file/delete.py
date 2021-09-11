from requests import delete as reqDelete
from json import dumps as jsonDumps
res = reqDelete(
    "https://my-file.cn/api/v3/object",
   headers={
"Content-Type": "application/json;charset=UTF-8",
"Cookie": "cloudreve-session=MTYzMTM0MzY2OHxOd3dBTkZoVFZ6TmFXVE5LUTFCUk5FUllSMVUwV2toWk5rZEpXamRIVURkV05WYzJORUZPU0VOV1JWSllWVmxNUjFCTVZGcFJRa0U9fK-bvzV1evIOkVNJ2LBnuxeofNbqRN7jWNzcccp_eARH; path_tmp=%E4%B8%B4%E6%97%B6%E5%A4%87%E4%BB%BD",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
   } ,
    data=jsonDumps({
        "dirs":["qdZOia"],
        "items":[]
    }),verify=False)
print(res.text)
