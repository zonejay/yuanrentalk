const fs = require('fs')
const readline = require('readline')

function decodeUnicodeString(unicodeString) {
  return unicodeString.replace(/\\u([\dA-Fa-f]{4})/g, (match, unicode) => {
    return String.fromCharCode(parseInt(unicode, 16))
  })
}

const inputFile = 'output.txt'
const outputFile = 'request.js'

const rl = readline.createInterface({
  input: fs.createReadStream(inputFile),
  output: fs.createWriteStream(outputFile),
  terminal: false
})

rl.on('line', (line) => {
  const decodedLine = decodeUnicodeString(line)
  rl.output.write(decodedLine + '\n')
})

rl.on('close', () => {
  console.log('File processing completed.')
})
