"""
Author: LeoChoco
CreatTime: 2022/12/25 17:09
Description: ...
"""
import os
import json
import requests
from typing import Tuple

from pic_repo.constance import PIC_PATH


def yukari_api() -> Tuple[str, str]:
    url = 'https://api.yukari.one/setu/'
    req = requests.get(url)
    response_body = json.loads(req.text)

    # data preprocess
    picture_data = response_body.get('data', None)
    for datum in picture_data:
        pid = datum.get("pid", "")
        index = datum.get("index", "")
    return str(pid), str(index)


def get_picture_from_yukari():
    url = 'https://pixiv.yukari.one/'
    pid, index = yukari_api()
    pic = requests.get(url + pid + '/' + index)
    if pic.status_code != 200:
        print(str(pic.status_code) + " 获取失败")
        return "404 not find"
    pic_name = pid + '_' + index + '.jpg'
    with open(os.path.join(PIC_PATH, pic_name), 'wb') as f:
        f.write(pic.content)
    return pic_name

if __name__ == '__main__':
    get_picture_from_yukari()
