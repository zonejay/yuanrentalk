const fs = require('fs')
const readline = require('readline')

function decodeHexString(hexString) {
  return hexString.replace(/\\x([0-9A-Fa-f]{2})/g, (match, hex) => {
    return String.fromCharCode(parseInt(hex, 16))
  })
}

const inputFile = 'input.txt'
const outputFile = 'output.txt'

const rl = readline.createInterface({
  input: fs.createReadStream(inputFile),
  output: fs.createWriteStream(outputFile),
  terminal: false
})

rl.on('line', (line) => {
  const decodedLine = decodeHexString(line)
  rl.output.write(decodedLine + '\n')
})

rl.on('close', () => {
  console.log('File processing completed.')
})
