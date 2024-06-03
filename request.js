const window = require('./window')
const {fun1} = require('./index')
const https = require('https')
const fetch = require('node-fetch')
window['url'] = '/api/match/1'

async function request(page = 1) {
  var timestamp = Date['parse'](new Date()) + 100000000,
    sign = fun1(timestamp['toString']()) + window['f']
  const data = {}
  data['page'] = window['page']
  data['m'] = sign + '丨' + timestamp / 1000
  var payload = data
  console.log(payload)
  const res = await fetch(`https://match.yuanrenxue.cn/api/match/1?m=${payload.m}&page=${page}`, {
    headers: {
      'Content-Type': 'application/json',
      cookie:
        'Hm_lvt_c99546cf032aaa5a679230de9a95c7db=1717037832; no-alert3=true; Hm_lpvt_c99546cf032aaa5a679230de9a95c7db=1717056444'
    }
  })
  const json = await res.json()
  console.log(json)
  return json.data
}

async function calAverage() {
    const totalPage = 5
    const allPrice = []
    for (let i = 1; i <= totalPage; i++) {
       const data = await request(i)
        allPrice.push(...data.map(item => item.value))
    }
    // 计算allPrice的平均值
    const average = allPrice.reduce((a, b) => a + b, 0) / allPrice.length
    console.log(average);
    
}

calAverage()
