import requests
import subprocess


def get_str_from_node_script():
    node_script = "./getParams.js"

    command = f"node {node_script}"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    output = result.stdout
    print(output)
    parse_output = output.split(",")
    return {"m": parse_output[0], "t": parse_output[1]}


url = "https://match.yuanrenxue.cn/api/match/16"

querystring = {
    "page": "2",
    "m": "W8td5Hy6j3fSEnB75321998c1570545b40b35c5b3b6c42d5XGwTCnGRi",
    "t": "1724079616000",
}

payload = ""
headers = {
    "cookie": "Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1723882363; sessionid=3nbgy787x0jkhomrxfsi8y7riwye9sc8; Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1723882321,1724078608; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1724078608; HMACCOUNT=F87F51EC0676D756",
    "accept": "application/json, text/javascript, */*; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=0, i",
    "referer": "https://match.yuanrenxue.cn/match/16",
    "sec-ch-ua": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
    "x-requested-with": "XMLHttpRequest",
}

response = requests.request(
    "GET", url, headers=headers, params={"page": "2", **get_str_from_node_script()}
)

print(response.text)
