const fs = require('fs');
// 读取 .wasm 文件
const wasmBuffer = fs.readFileSync('./module.wasm');

// 实例化 Wasm 模块
WebAssembly.instantiate(wasmBuffer).then(async wasmModule => {
  const { exports } = wasmModule.instance;
  const encode = exports.encode
  const getCode = () => {
    t1 = parseInt(Date.parse(new Date()) / 1000 / 2);
    t2 = parseInt(Date.parse(new Date()) / 1000 / 2 - Math.floor(Math.random() * (50) + 1));
    const code = encode(t1, t2).toString() + '|' + t1 + '|' + t2
    return code
  }


  let options = {
    method: 'GET',
    headers: {
      accept: 'application/json, text/javascript, */*; q=0.01',
      'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,ja;q=0.6,zh-TW;q=0.5',
      'cache-control': 'no-cache',
      cookie: 'sessionid=3nbgy787x0jkhomrxfsi8y7riwye9sc8;',
      pragma: 'no-cache',
      priority: 'u=0, i',
      referer: 'https://match.yuanrenxue.cn/match/15',
      'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
      'x-requested-with': 'XMLHttpRequest'
    }
  };

  const total_page = 5
  let total = 0
  for (let i = 1; i <= total_page; i++) {
    const code = getCode()
    let url = `https://match.yuanrenxue.cn/api/match/15?m=${code}&page=${i}`;
    const res = await fetch(url, options)
    const resJson = await res.json()
    resJson.data.forEach(item => total += item.value)
  }
  console.log(total)
});

