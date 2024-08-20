import requests
import re

headers = {
    "cookie": "sessionid=oqnoi7nsdwouemgn5f96wommgnvz56zn",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/13",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
}

def get_cookie():
    url = "https://match.yuanrenxue.cn/match/13"

    payload = ""

    response = requests.request("GET", url, data=payload, headers=headers)

    text = response.text
    # 正则表达式提取 document.cookie 到 location 之前的内容
    match = re.search(r'document\.cookie=(.*?);location', text, re.DOTALL)
    value_after_equal = ''
    if match:
        cookie_content = match.group(1)
        # 正则表达式提取所有 '(' 和 ')' 之间的内容
        matches = re.findall(r"\('(.+?)'\)", cookie_content)

        # 将所有提取到的内容拼接在一起
        result = ''.join(matches)
        return result
    else:
        print("没有找到匹配内容")

    return value_after_equal

def get_page(page_no:int, cookie: str):
    url = f'https://match.yuanrenxue.cn/api/match/13?page={page_no}'
    local_headers = {**headers, "cookie": f"{headers["cookie"]};{cookie}"}

    response = requests.request("GET", url, headers=local_headers)
    return sum(item["value"] for item in response.json()["data"])

if __name__ == "__main__":
    total = 0
    total_page = 5
    cookie = get_cookie()
    for i in range(1, total_page + 1):
        total += get_page(i, cookie)
    print(total)
