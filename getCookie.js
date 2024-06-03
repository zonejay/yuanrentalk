const axios = require('axios')
const {wrapper} = require('axios-cookiejar-support')
const tough = require('tough-cookie')
// 创建 axios 实例
const options = {
  method: 'GET',
  headers: {
    accept: 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    Cookie: 'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1717399607; Hm_lvt_9bcbda9cbf86757998a2339a0437208e=1717399607; Hm_lpvt_9bcbda9cbf86757998a2339a0437208e=1717399607; sessionid=5499mx5wpasgo78h8v49rs6wb32mkb0o; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1717401882',
    pragma: 'no-cache',
    priority: 'u=0, i',
    referer: 'https://match.yuanrenxue.cn/match/3',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent':
      'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
  }
}
const instance = axios.create({
  baseURL: 'https://match.yuanrenxue.cn/',
  timeout: 1000,
  headers: options.headers,
  withCredentials: true, // 允许携带和管理 cookies
  jar: new tough.CookieJar() // 使用 tough-cookie 管理 cookies
})

// 启用 axios-cookiejar-support
wrapper(instance)

instance.post('/jssm').then((res) => {
  console.log(res.cookie)
  instance.get('/api/match/3').then((res) => {
    // console.log(res)
  })
})
