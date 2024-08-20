import requests
import base64

url = "https://match.yuanrenxue.cn/api/match/12"

headers = {
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "cookie": "Hm_lvt_434c501fe98c1a8ec74b813751d4e3e3=1723822580; HMACCOUNT=A35C053077533FC9; Hm_lpvt_434c501fe98c1a8ec74b813751d4e3e3=1723879611; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1723882321; tk=628001390555153908; sessionid=oqnoi7nsdwouemgn5f96wommgnvz56zn; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1723882363; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1723882363; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1723882387",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/12",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}


def get_query(page: int, prefix: str):
    input_str = f"{prefix}{page}"
    string_bytes = input_str.encode("utf-8")
    base64_bytes = base64.b64encode(string_bytes)
    base64_str = base64_bytes.decode("utf-8")
    print(base64_str)
    return {"page": page, "m": base64_str}

def send_req(query):
    response = requests.request(
        "GET", url, headers=headers, params=query
    )
    nums = response.json()["data"]
    return sum(item["value"] for item in nums)


def main():
    total_page = 5
    base64_prefix = "yuanrenxue"
    total = 0
    for page in range(1, total_page + 1):
        query = get_query(page, base64_prefix)
        ret = send_req(query)
        print(ret)
        total += ret

    print(total)

if __name__ == "__main__":
    main()

