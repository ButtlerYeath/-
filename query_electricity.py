import os
import requests

query_url = "http://catsd.kddziot.online/electricmeter/index.html#/pages/meterlist/meterquery?wechatUserOpenid=osXdnwxbMuHqu_8u5HlkBznM9NWc&meterId=11488&elemeterTypeRemark=%E9%A2%84%E4%BB%98%E8%B4%B9%E8%BF%9C%E6%8E%A7%E5%85%AC%E5%AF%93%E4%B8%89%E5%9B%9E%E8%B7%AF&sign=e27b724af6444bcb8938cff2acc790d9"

app_token = os.getenv("APP_TOKEN")
uid = os.getenv("UID")

def get_electricity_info():
    response = requests.get(query_url)
    if response.status_code == 200:
        return "查询成功，可以根据内容解析电费信息！"
    else:
        return f"查询失败，状态码：{response.status_code}"

def send_wxpusher_notification(content):
    url = "https://wxpusher.zjiecode.com/api/send/message"
    data = {
        "appToken": app_token,
        "content": content,
        "summary": "电费提醒",
        "contentType": 1,
        "uids": [uid],
    }
    response = requests.post(url, json=data)
    print("推送结果:", response.text)

if __name__ == "__main__":
    info = get_electricity_info()
    send_wxpusher_notification(info)
