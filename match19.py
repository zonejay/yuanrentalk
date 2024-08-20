import httpx
import subprocess

test_cipher = "RSA-AES128-CBC-SHA"
right_cipher = "ECDHE-RSA-AES128-GCM-SHA256"
context = httpx.create_ssl_context()
context.set_ciphers(right_cipher)

url = "https://match.yuanrenxue.cn/api/login"

payload = {"username": "moonSun", "password": "BbjCUtYbUkEm7b9"}
headers = {
    "cookie": "Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1723882321; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1723882363; tk=628001390555153908; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1723907642; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1723909517",
    "accept": "*/*",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "origin": "https://match.yuanrenxue.cn",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://match.yuanrenxue.cn/login",
    "sec-ch-ua": 'Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

with httpx.Client(http2=True, verify=context) as client:
    response = client.post(url=url, data=payload, headers=headers)
    page_url = "https://match.yuanrenxue.cn/api/match/19"
    sessionid = response.cookies.get('sessionid')
    page_total = 1
    total = 0
    for i in range(1, page_total + 1):
        res = client.get(
            page_url,
            params={"page": i},
            headers={**headers, "cookie": f"sessionid={sessionid}"},
        )
        total += sum(item["value"] for item in res.json()["data"])
    print(total)


def get_str_from_node_script():
    node_script = "./getParams.js"

    command = f"node {node_script}"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    output = result.stdout
    print(output)

if __name__ == "__main__":
    get_str_from_node_script()
