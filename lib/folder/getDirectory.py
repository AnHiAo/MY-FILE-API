# 'https://my-file.cn/api/v3/directory%2F'
from urllib3 import disable_warnings
from requests import get as reqGet
from urllib.parse import quote
outputStrList = [];
res = reqGet(
    ("https://my-file.cn/api/v3/directory/"),
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
        "Cookie": "path_tmp=; cloudreve-session=MTYzMTM0MzY2OHxOd3dBTkZoVFZ6TmFXVE5LUTFCUk5FUllSMVUwV2toWk5rZEpXamRIVURkV05WYzJORUZPU0VOV1JWSllWVmxNUjFCTVZGcFJRa0U9fK-bvzV1evIOkVNJ2LBnuxeofNbqRN7jWNzcccp_eARH"
    },
    verify=False
)
if res:
    for i in res.json()['data']['objects']:
        outputStrList.append(f' ( {i["type"]} )    {i["date"]}{" "*4}{i["name"]}')
print("\n".join(outputStrList))