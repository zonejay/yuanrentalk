import httpx

url = "https://match.yuanrenxue.cn/api/match/17"

querystring = {"page":"5"}

payload = ""
headers = {
    "cookie": "Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1723822580; HMACCOUNT=A35C053077533FC9; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1723879611; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1723882321; tk=628001390555153908; sessionid=oqnoi7nsdwouemgn5f96wommgnvz56zn; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1723882363; yuanrenxue_cookie=1723891273|RFFXHzVkgCeJ4rNtPOlKaOOfa21JD9oTtqL; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1723891286; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1723891316",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/17",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest"
}

with httpx.Client(http2=True) as client:
    total = 0
    total_no = 5
    for i in range(1, total_no + 1):
        response = client.get(url, headers=headers, params={"page": f"{i}"})
        total += sum(item["value"] for item in response.json()["data"])

    print(total)

